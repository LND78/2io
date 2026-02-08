import fs from 'fs';
import path from 'path';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import QuestionCard from '@/components/QuestionCard';

export async function generateStaticParams() {
  const subjects = ['history', 'geography', 'political-science', 'economics'];
  let params: { subject: string; chapter: string }[] = [];

  for (const subject of subjects) {
    const filePath = path.join(process.cwd(), 'data', `${subject}.json`);
    try {
      const fileContent = fs.readFileSync(filePath, 'utf8');
      const data = JSON.parse(fileContent);
      data.chapters.forEach((chapter: any) => {
        params.push({ subject, chapter: chapter.id });
      });
    } catch (e) {
      console.error(e);
    }
  }
  return params;
}

interface PageProps {
  params: Promise<{
    subject: string;
    chapter: string;
  }>;
}

export default async function ChapterPage({ params }: PageProps) {
  const { subject, chapter } = await params;

  const validSubjects = ['history', 'geography', 'political-science', 'economics'];
  if (!validSubjects.includes(subject)) {
    notFound();
  }

  const filePath = path.join(process.cwd(), 'data', `${subject}.json`);

  let data;
  try {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    data = JSON.parse(fileContent);
  } catch (error) {
    notFound();
  }

  const chapterData = data.chapters.find((c: any) => c.id === chapter);

  if (!chapterData) {
    notFound();
  }

  return (
    <div>
      <div className="mb-8">
        <Link href={`/${subject}`} className="text-indigo-600 hover:text-indigo-800 flex items-center mb-4 transition-colors w-fit">
          <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7"></path>
          </svg>
          Back to {data.subject.replace('-', ' ')}
        </Link>
        <h1 className="text-3xl font-bold text-gray-900 capitalize border-b pb-4 border-gray-200">
          {chapterData.title}
        </h1>
        <p className="text-gray-600 mt-4">
          Practice questions for {chapterData.title}. Total questions: {chapterData.questions.length}
        </p>
      </div>

      <div className="space-y-6">
        {chapterData.questions.map((question: any, index: number) => (
          <QuestionCard key={index} question={question} index={index} />
        ))}
      </div>
    </div>
  );
}
