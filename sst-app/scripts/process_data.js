const fs = require('fs');
const path = require('path');

const RAW_DATA_DIR = path.join(__dirname, '../raw_data');
const DATA_DIR = path.join(__dirname, '../data');

const SUBJECTS = {
  'History.json': 'history',
  'Geography.json': 'geography',
  'PoliticalScience.json': 'political-science',
  'Economics.json': 'economics',
};

function slugify(text) {
  return text.toString().toLowerCase().trim()
    .replace(/\s+/g, '-')
    .replace(/[^\w\-]+/g, '')
    .replace(/\-\-+/g, '-');
}

if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR);
}

const manifest = {};

for (const [filename, subjectSlug] of Object.entries(SUBJECTS)) {
  const filePath = path.join(RAW_DATA_DIR, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    continue;
  }

  console.log(`Processing ${filename}...`);
  const rawContent = fs.readFileSync(filePath, 'utf-8');
  let data;
  try {
    data = JSON.parse(rawContent);
  } catch (e) {
    console.error(`Error parsing JSON for ${filename}:`, e);
    continue;
  }

  let questions = [];
  if (subjectSlug === 'history') {
    if (data.sections && data.sections[0] && data.sections[0].questions) {
      questions = data.sections[0].questions;
    } else {
      console.error(`Unexpected structure for History.json`);
      // Try treating as flat array just in case
      if (Array.isArray(data)) {
          questions = data;
      }
    }
  } else {
    questions = data;
  }

  // Group by chapter
  const chapters = {};
  questions.forEach(q => {
    const chapterName = q.Chapter;
    if (!chapterName) return;
    const chapterSlug = slugify(chapterName);

    if (!chapters[chapterSlug]) {
      chapters[chapterSlug] = {
        id: chapterSlug,
        title: chapterName.toString(), // Keep original title for display
        questions: []
      };
    }
    chapters[chapterSlug].questions.push(q);
  });

  // Write chapter files
  const subjectDir = path.join(DATA_DIR, subjectSlug);
  if (!fs.existsSync(subjectDir)) {
    fs.mkdirSync(subjectDir);
  }

  const subjectManifest = [];

  for (const [chapterSlug, chapterData] of Object.entries(chapters)) {
    const chapterFile = path.join(subjectDir, `${chapterSlug}.json`);
    fs.writeFileSync(chapterFile, JSON.stringify(chapterData, null, 2));
    subjectManifest.push({
      slug: chapterSlug,
      title: chapterData.title
    });
  }

  // Sort chapters numerically if possible, otherwise alphabetically
  subjectManifest.sort((a, b) => {
      const numA = parseInt(a.slug);
      const numB = parseInt(b.slug);
      if (!isNaN(numA) && !isNaN(numB)) {
          return numA - numB;
      }
      return a.slug.localeCompare(b.slug);
  });

  manifest[subjectSlug] = subjectManifest;
}

fs.writeFileSync(path.join(DATA_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2));
console.log('Data processing complete.');
