'use client';

import React, { useState } from 'react';

interface QuestionProps {
  question: {
    type: string;
    question: {
      en: string;
      hi: string;
    };
    answer: {
      en: string;
      hi: string;
    };
    marks: string;
  };
  index: number;
}

const QuestionCard: React.FC<QuestionProps> = ({ question, index }) => {
  const [showAnswer, setShowAnswer] = useState(false);

  return (
    <div className="bg-white shadow-md rounded-lg p-6 mb-4 border border-gray-200 hover:shadow-lg transition-shadow duration-300">
      <div className="flex justify-between items-start mb-4">
        <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded uppercase">
          {question.type}
        </span>
        <span className="text-gray-500 text-sm font-medium">
          Marks: {question.marks}
        </span>
      </div>

      <div className="mb-4">
        <h3 className="text-lg font-semibold text-gray-900 mb-2">
          {index + 1}. {question.question.en}
        </h3>
        {question.question.hi && (
          <p className="text-gray-700 italic font-medium">
            ({question.question.hi})
          </p>
        )}
      </div>

      <button
        onClick={() => setShowAnswer(!showAnswer)}
        className="text-white bg-indigo-600 hover:bg-indigo-700 focus:ring-4 focus:ring-indigo-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 focus:outline-none transition-colors"
      >
        {showAnswer ? 'Hide Answer' : 'Show Answer'}
      </button>

      {showAnswer && (
        <div className="mt-4 p-4 bg-green-50 rounded-md border border-green-200 animate-fade-in">
          <p className="font-semibold text-green-900 mb-2">Ans. {question.answer.en}</p>
          {question.answer.hi && (
            <p className="text-green-800">({question.answer.hi})</p>
          )}
        </div>
      )}
    </div>
  );
};

export default QuestionCard;
