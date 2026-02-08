import fs from 'fs';
import path from 'path';
import Link from 'next/link';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  return [
    { subject: 'history' },
    { subject: 'geography' },
    { subject: 'political-science' },
    { subject: 'economics' },
  ];
}

interface PageProps {
  params: Promise<{
    subject: string;
  }>;
}

export default async function SubjectPage({ params }: PageProps) {
  const { subject } = await params;

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
    console.error(`Error reading file for subject ${subject}:`, error);
    notFound();
  }

  return (
    <div>
      <div className="mb-8">
        <Link href="/" className="text-indigo-600 hover:text-indigo-800 flex items-center mb-4 transition-colors w-fit">
          <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7"></path>
          </svg>
          Back to Subjects
        </Link>
        <h1 className="text-3xl font-bold text-gray-900 capitalize border-b pb-4 border-gray-200">
          {data.subject.replace('-', ' ')}
        </h1>
        <p className="text-gray-600 mt-4 text-lg">
          Select a chapter to start practicing questions.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {data.chapters.map((chapter: any) => (
          <Link href={`/${subject}/${chapter.id}`} key={chapter.id} className="group block h-full">
            <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 hover:border-indigo-400 hover:shadow-md transition-all duration-300 h-full flex flex-col justify-between">
              <div>
                <h3 className="text-xl font-semibold text-gray-800 mb-3 group-hover:text-indigo-700 transition-colors">
                  {chapter.title}
                </h3>
                <div className="flex items-center text-sm text-gray-500">
                  <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  {chapter.questions.length} Questions
                </div>
              </div>
              <div className="mt-6 flex justify-end items-center">
                <span className="text-indigo-600 text-sm font-medium group-hover:translate-x-1 transition-transform flex items-center">
                  Start Practice
                  <svg className="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
                  </svg>
                </span>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
