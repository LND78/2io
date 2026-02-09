import fs from 'fs';
import path from 'path';
import Link from 'next/link';
import { notFound } from 'next/navigation';

const DATA_DIR = path.join(process.cwd(), 'data');

async function getChapters(subject: string) {
  const manifestPath = path.join(DATA_DIR, 'manifest.json');
  if (!fs.existsSync(manifestPath)) return null;
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  return manifest[subject] || null;
}

export async function generateStaticParams() {
  const manifestPath = path.join(DATA_DIR, 'manifest.json');
  if (!fs.existsSync(manifestPath)) return [];
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  return Object.keys(manifest).map((subject) => ({
    subject: subject,
  }));
}

export default async function SubjectPage({ params }: { params: Promise<{ subject: string }> }) {
  const { subject } = await params;
  const chapters = await getChapters(subject);

  if (!chapters) {
    notFound();
  }

  const subjectTitle = subject.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  let colorClass = 'text-gray-900';
  if (subject === 'history') colorClass = 'text-red-700';
  if (subject === 'geography') colorClass = 'text-green-700';
  if (subject === 'political-science') colorClass = 'text-blue-700';
  if (subject === 'economics') colorClass = 'text-yellow-700';

  return (
    <div className="max-w-6xl mx-auto">
      <div className="mb-8">
        <Link href="/" className="text-gray-600 hover:text-gray-900 mb-4 inline-flex items-center text-sm font-medium transition-colors">
          <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7" />
          </svg>
          Back to Home
        </Link>
        <h1 className={`text-3xl md:text-4xl font-extrabold ${colorClass} mt-2`}>
          {subjectTitle}
        </h1>
        <p className="text-gray-500 mt-2">Select a chapter to practice.</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {chapters.map((chapter: any) => (
          <Link
            key={chapter.slug}
            href={`/${subject}/${chapter.slug}`}
            className="block p-6 bg-white rounded-xl shadow-sm hover:shadow-lg border border-gray-100 transition-all duration-300 hover:-translate-y-1 group"
          >
            <div className="flex items-center justify-between mb-4">
              <span className={`text-xs font-semibold px-2 py-1 rounded bg-gray-100 text-gray-600 uppercase tracking-wide`}>
                Chapter
              </span>
              <span className="text-gray-400 group-hover:text-gray-600 transition-colors">
                 &rarr;
              </span>
            </div>
            <h3 className="text-xl font-bold text-gray-800 group-hover:text-blue-600 mb-2">
              {chapter.title}
            </h3>
            <p className="text-sm text-gray-500">
              Practice questions
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
