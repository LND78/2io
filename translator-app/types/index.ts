export interface Question {
  id: string;
  text: string;
  originalText: string;
  options?: string[];
  answer: string;
  type: 'objective' | 'fill-in-the-blank' | 'short-answer' | 'essay';
  diagramUrl?: string;
}

export interface Section {
  id: string;
  title: string;
  hindiTitle: string;
  questions: Question[];
}

export interface Chapter {
  id: string;
  title: string;
  hindiTitle: string;
  sections: Section[];
}
