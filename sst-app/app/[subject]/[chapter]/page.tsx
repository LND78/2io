import fs from 'fs';
import path from 'path';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import QuestionCard from '@/components/QuestionCard';

const DATA_DIR = path.join(process.cwd(), 'data');

async function getChapterData(subject: string, chapter: string) {
  const filePath = path.join(DATA_DIR, subject, `${chapter}.json`);
  if (!fs.existsSync(filePath)) return null;
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(fileContent);
}

export async function generateStaticParams() {
  const manifestPath = path.join(DATA_DIR, 'manifest.json');
  if (!fs.existsSync(manifestPath)) return [];
  const fileContent = fs.readFileSync(manifestPath, 'utf-8');
  const manifest = JSON.parse(fileContent);

  const params: { subject: string, chapter: string }[] = [];

  for (const subject of Object.keys(manifest)) {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    manifest[subject].forEach((chapter: any) => {
      params.push({
        subject: subject,
        chapter: chapter.slug,
      });
    });
  }
  return params;
}

export default async function ChapterPage({ params }: { params: Promise<{ subject: string, chapter: string }> }) {
  const { subject, chapter } = await params;
  const data = await getChapterData(subject, chapter);

  if (!data) {
    notFound();
  }

  const subjectTitle = subject.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <Link href={`/${subject}`} className="text-blue-600 hover:underline mb-4 inline-block">&larr; Back to {subjectTitle}</Link>
        <h1 className="text-3xl font-bold text-gray-900">Chapter {data.title}</h1>
        <p className="text-gray-500 mt-2">{data.questions.length} Questions</p>
      </div>

      <div className="space-y-6">
        {/* eslint-disable-next-line @typescript-eslint/no-explicit-any */}
        {data.questions.map((q: any, index: number) => (
          <QuestionCard key={index} question={q} />
        ))}
      </div>
    </div>
  );
}
