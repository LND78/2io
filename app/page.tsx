import Link from 'next/link';

const subjects = [
  { id: 'history', name: 'History', description: 'Explore past events and civilizations.', color: 'bg-red-500' },
  { id: 'geography', name: 'Geography', description: 'Study the lands, features, inhabitants, and phenomena of Earth.', color: 'bg-green-500' },
  { id: 'political-science', name: 'Political Science', description: 'Analyze political activities, political thoughts, and political behavior.', color: 'bg-blue-500' },
  { id: 'economics', name: 'Economics', description: 'Understand the production, distribution, and consumption of goods and services.', color: 'bg-yellow-500' },
];

export default function Home() {
  return (
    <div className="flex flex-col items-center">
      <h1 className="text-4xl font-extrabold text-gray-900 mb-8 text-center">
        Welcome to SST Question Bank
      </h1>
      <p className="text-lg text-gray-600 mb-12 text-center max-w-2xl">
        Select a subject to browse chapters and practice questions for your exams.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl">
        {subjects.map((subject) => (
          <Link href={`/${subject.id}`} key={subject.id} className="group">
            <div className={`h-full p-6 rounded-xl shadow-md transition-all duration-300 transform hover:-translate-y-1 hover:shadow-xl bg-white border border-gray-100 flex flex-col`}>
              <div className={`h-2 w-full rounded-full mb-4 ${subject.color}`}></div>
              <h2 className="text-2xl font-bold text-gray-800 mb-2 group-hover:text-indigo-600 transition-colors">
                {subject.name}
              </h2>
              <p className="text-gray-600 flex-grow">
                {subject.description}
              </p>
              <div className="mt-4 text-indigo-600 font-medium flex items-center">
                Start Learning
                <svg className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7"></path>
                </svg>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
