const fs = require('fs');
const path = require('path');

const RAW_DIR = 'raw_data';
const OUT_DIR = 'data';

const SUBJECTS = {
  'History.json': 'history',
  'Geography.json': 'geography',
  'PoliticalScience.json': 'political-science',
  'Economics.json': 'economics',
};

function normalizeChapterId(chapter) {
  if (typeof chapter === 'number') return String(chapter);
  if (!chapter) return 'unknown';
  return chapter.toString().toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

function processFile(filename) {
  const filepath = path.join(RAW_DIR, filename);
  const rawData = fs.readFileSync(filepath, 'utf8');
  const data = JSON.parse(rawData);

  let questions = [];

  if (filename === 'History.json') {
    if (data.sections) {
      data.sections.forEach(section => {
        if (section.questions) {
          questions = questions.concat(section.questions);
        }
      });
    }
  } else {
    questions = data;
  }

  // Group by chapter
  const chapters = {};

  questions.forEach(q => {
    const chapterRaw = q.Chapter;
    const chapterId = normalizeChapterId(chapterRaw);

    if (!chapters[chapterId]) {
      chapters[chapterId] = {
        id: chapterId,
        title: `Chapter ${chapterRaw}`, // Or infer from content if possible, but raw "Chapter X" or "Model Paper" is fine
        questions: []
      };
      // If chapterRaw is "Model Paper" or something similar, use that as title
      if (isNaN(chapterRaw)) {
         chapters[chapterId].title = chapterRaw;
      }
    }

    chapters[chapterId].questions.push({
      type: q['Questions type'],
      question: {
        en: q['Question in English'],
        hi: q['Question in Hindi']
      },
      answer: {
        en: q['Answer in English'],
        hi: q['Answer in Hindi']
      },
      marks: q['Marks']
    });
  });

  // Convert map to array and sort
  const sortedChapters = Object.values(chapters).sort((a, b) => {
      // Try to sort numerically if possible
      const numA = parseInt(a.id);
      const numB = parseInt(b.id);
      if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
      return a.id.localeCompare(b.id);
  });

  const subjectName = SUBJECTS[filename];
  const outPath = path.join(OUT_DIR, `${subjectName}.json`);

  fs.writeFileSync(outPath, JSON.stringify({
    subject: subjectName,
    chapters: sortedChapters
  }, null, 2));

  console.log(`Processed ${filename} -> ${outPath}`);
}

if (!fs.existsSync(OUT_DIR)){
    fs.mkdirSync(OUT_DIR);
}

Object.keys(SUBJECTS).forEach(filename => {
  if (fs.existsSync(path.join(RAW_DIR, filename))) {
    processFile(filename);
  } else {
    console.warn(`File not found: ${filename}`);
  }
});
