import Link from 'next/link';
import { getAllChapters } from '@/lib/api';
import { BookOpen, ChevronRight } from 'lucide-react';

export default async function Home() {
  const chapters = await getAllChapters();

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950">
      <div className="max-w-4xl mx-auto px-4 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-zinc-900 dark:text-zinc-100 mb-4">
            Social Science Translator
          </h1>
          <p className="text-lg text-zinc-600 dark:text-zinc-400">
            Hindi to English Translation of Shekhawati Mission 100
          </p>
        </div>

        <div className="grid gap-4 md:grid-cols-2">
          {chapters.map((chapter) => (
            <Link
              key={chapter.id}
              href={`/chapter/${chapter.id}`}
              className="block group"
            >
              <div className="bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-6 hover:shadow-lg transition-all hover:border-blue-500 dark:hover:border-blue-500">
                <div className="flex justify-between items-start">
                  <div>
                    <span className="inline-block px-3 py-1 bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300 rounded-full text-xs font-semibold mb-3">
                      Chapter {chapter.id}
                    </span>
                    <h2 className="text-xl font-bold text-zinc-900 dark:text-zinc-100 mb-1 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                      {chapter.title}
                    </h2>
                    <p className="text-zinc-500 dark:text-zinc-400 font-hindi">
                      {chapter.hindiTitle}
                    </p>
                  </div>
                  <ChevronRight className="w-5 h-5 text-zinc-400 group-hover:text-blue-500 transition-colors" />
                </div>
              </div>
            </Link>
          ))}

          {chapters.length === 0 && (
            <div className="col-span-2 text-center py-12 text-zinc-500">
              No chapters loaded yet.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
