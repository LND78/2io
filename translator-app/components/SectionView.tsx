import { Section } from '@/types';
import QuestionCard from './QuestionCard';

interface SectionViewProps {
  section: Section;
}

export default function SectionView({ section }: SectionViewProps) {
  return (
    <div className="mb-12">
      <div className="mb-6 border-b border-zinc-200 dark:border-zinc-800 pb-2">
        <h2 className="text-2xl font-bold text-zinc-900 dark:text-zinc-100">
          {section.title}
        </h2>
        <p className="text-zinc-500 dark:text-zinc-400 font-hindi">
          {section.hindiTitle}
        </p>
      </div>

      <div>
        {section.questions.map((question, index) => (
          <QuestionCard
            key={question.id}
            question={question}
            index={index}
          />
        ))}
      </div>
    </div>
  );
}
