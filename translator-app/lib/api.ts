import { Chapter } from '@/types';
import fs from 'fs';
import path from 'path';

export async function getChapter(id: string): Promise<Chapter | null> {
  const filePath = path.join(process.cwd(), 'data', `chapter${id}.json`);

  try {
    const fileContents = fs.readFileSync(filePath, 'utf8');
    const chapter: Chapter = JSON.parse(fileContents);
    return chapter;
  } catch (error) {
    console.error(`Error loading chapter ${id}:`, error);
    return null;
  }
}

export async function getAllChapters(): Promise<{id: string, title: string, hindiTitle: string}[]> {
  const dataDir = path.join(process.cwd(), 'data');
  const files = fs.readdirSync(dataDir);

  const chapters = files
    .filter(file => file.startsWith('chapter') && file.endsWith('.json'))
    .map(file => {
      const content = fs.readFileSync(path.join(dataDir, file), 'utf8');
      const json = JSON.parse(content);
      return {
        id: json.id,
        title: json.title,
        hindiTitle: json.hindiTitle
      };
    })
    .sort((a, b) => parseInt(a.id) - parseInt(b.id));

  return chapters;
}
