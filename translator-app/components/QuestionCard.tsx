'use client';

import { useState } from 'react';
import { Question } from '@/types';
import { Eye, EyeOff } from 'lucide-react';
import clsx from 'clsx';

interface QuestionCardProps {
  question: Question;
  index: number;
}

export default function QuestionCard({ question, index }: QuestionCardProps) {
  const [showAnswer, setShowAnswer] = useState(false);

  const isProveThat = question.text.toLowerCase().startsWith('prove that');

  return (
    <div className="bg-white dark:bg-zinc-900 rounded-lg shadow-md border border-zinc-200 dark:border-zinc-800 p-6 mb-4 transition-all hover:shadow-lg">
      <div className="flex justify-between items-start gap-4">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-2">
            <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">
              Q{index + 1}
            </span>
            <span className="text-xs text-zinc-500 uppercase tracking-wider font-medium">
              {question.type.replace(/-/g, ' ')}
            </span>
          </div>

          <h3 className="text-lg font-medium text-zinc-900 dark:text-zinc-100 mb-1">
            {question.text}
          </h3>

          {question.originalText && (
            <p className="text-sm text-zinc-500 dark:text-zinc-400 font-hindi mb-3">
              {question.originalText}
            </p>
          )}

          {question.diagramUrl && (
            <div className="my-4">
              <img
                src={question.diagramUrl}
                alt="Question Diagram"
                className="max-w-full h-auto rounded border border-zinc-200"
              />
            </div>
          )}

          {question.options && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mt-3">
              {question.options.map((option, idx) => (
                <div
                  key={idx}
                  className={clsx(
                    "p-2 rounded text-sm border",
                    showAnswer && option.includes(question.answer.split(')')[0]) // Simple check if option matches answer key
                      ? "bg-green-50 border-green-200 text-green-700 font-medium"
                      : "bg-zinc-50 border-zinc-100 text-zinc-700"
                  )}
                >
                  {option}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {!isProveThat && (
        <div className="mt-4 pt-4 border-t border-zinc-100 dark:border-zinc-800">
          <button
            onClick={() => setShowAnswer(!showAnswer)}
            className="flex items-center gap-2 text-sm font-medium text-blue-600 hover:text-blue-700 transition-colors"
          >
            {showAnswer ? (
              <>
                <EyeOff className="w-4 h-4" /> Hide Answer
              </>
            ) : (
              <>
                <Eye className="w-4 h-4" /> Show Answer
              </>
            )}
          </button>

          {showAnswer && (
            <div className="mt-3 bg-zinc-50 dark:bg-zinc-800/50 rounded p-3 text-zinc-800 dark:text-zinc-200 text-sm animate-in fade-in slide-in-from-top-2">
              <span className="font-semibold text-zinc-900 dark:text-zinc-100 block mb-1">Answer:</span>
              {question.answer}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
