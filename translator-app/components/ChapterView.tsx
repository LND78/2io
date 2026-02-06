import { Chapter } from '@/types';
import SectionView from './SectionView';
import Link from 'next/link';
import { ChevronLeft, ChevronRight } from 'lucide-react';

interface ChapterViewProps {
  chapter: Chapter;
}

export default function ChapterView({ chapter }: ChapterViewProps) {
  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <div className="mb-8">
        <Link
          href="/"
          className="inline-flex items-center text-sm text-zinc-500 hover:text-zinc-900 mb-4 transition-colors"
        >
          <ChevronLeft className="w-4 h-4 mr-1" /> Back to Dashboard
        </Link>
        <h1 className="text-4xl font-extrabold text-zinc-900 dark:text-zinc-100 mb-2">
          {chapter.title}
        </h1>
        <h2 className="text-xl text-zinc-500 dark:text-zinc-400 font-hindi">
          {chapter.hindiTitle}
        </h2>
      </div>

      {chapter.sections.map((section) => (
        <SectionView key={section.id} section={section} />
      ))}

      <div className="mt-12 flex justify-between pt-8 border-t border-zinc-200 dark:border-zinc-800">
        <button disabled className="flex items-center text-zinc-400 cursor-not-allowed">
          <ChevronLeft className="w-4 h-4 mr-2" /> Previous Chapter
        </button>
        <button disabled className="flex items-center text-zinc-400 cursor-not-allowed">
          Next Chapter <ChevronRight className="w-4 h-4 ml-2" />
        </button>
      </div>
    </div>
  );
}
