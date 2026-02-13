import { getChapter, getAllChapters } from '@/lib/api';
import ChapterView from '@/components/ChapterView';
import { notFound } from 'next/navigation';

interface PageProps {
  params: Promise<{ id: string }>;
}

export async function generateStaticParams() {
  const chapters = await getAllChapters();
  return chapters.map((chapter) => ({
    id: chapter.id,
  }));
}

export default async function ChapterPage({ params }: PageProps) {
  const { id } = await params;
  const chapter = await getChapter(id);

  if (!chapter) {
    notFound();
  }

  return <ChapterView chapter={chapter} />;
}
