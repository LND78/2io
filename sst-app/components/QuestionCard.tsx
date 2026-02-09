'use client';

import React, { useState } from 'react';
import { Question } from '../types';

interface QuestionCardProps {
  question: Question;
}

export default function QuestionCard({ question }: QuestionCardProps) {
  const [showAnswer, setShowAnswer] = useState(false);

  return (
    <div className="bg-white p-6 rounded-lg shadow-md mb-6 border border-gray-200">
      <div className="flex justify-between items-center mb-4 text-sm text-gray-500 font-medium">
        <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full">
          {question["Questions type"]}
        </span>
        <span className="bg-gray-100 text-gray-800 px-3 py-1 rounded-full">
          Marks: {question.Marks}
        </span>
      </div>

      <div className="mb-4">
        <h3 className="text-lg font-semibold text-gray-900 mb-2">{question["Question in English"]}</h3>
        <p className="text-gray-700 italic">{question["Question in Hindi"]}</p>
      </div>

      <button
        onClick={() => setShowAnswer(!showAnswer)}
        className="text-blue-600 hover:text-blue-800 font-medium text-sm focus:outline-none mb-4 transition-colors duration-200"
      >
        {showAnswer ? 'Hide Answer' : 'Show Answer'}
      </button>

      {showAnswer && (
        <div className="bg-green-50 p-4 rounded-md border border-green-200 mt-2 animate-fadeIn">
          <p className="text-green-800 font-medium mb-2">Ans. {question["Answer in English"]}</p>
          <p className="text-green-700 italic">{question["Answer in Hindi"]}</p>
        </div>
      )}
    </div>
  );
}
