import Link from 'next/link';

const subjects = [
  { name: 'History', slug: 'history', color: 'bg-red-500', hoverBorder: 'hover:border-red-500', text: 'text-red-700' },
  { name: 'Geography', slug: 'geography', color: 'bg-green-500', hoverBorder: 'hover:border-green-500', text: 'text-green-700' },
  { name: 'Political Science', slug: 'political-science', color: 'bg-blue-500', hoverBorder: 'hover:border-blue-500', text: 'text-blue-700' },
  { name: 'Economics', slug: 'economics', color: 'bg-yellow-500', hoverBorder: 'hover:border-yellow-500', text: 'text-yellow-700' },
];

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh]">
      <div className="text-center mb-16">
        <h1 className="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6 tracking-tight">
          SST Shekhavati Mission 100
        </h1>
        <p className="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto">
          Your comprehensive question bank for Class 10 Social Science.
          Select a subject below to start revising.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl px-4">
        {subjects.map((subject) => (
          <Link
            key={subject.slug}
            href={`/${subject.slug}`}
            className={`group relative overflow-hidden rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 bg-white border-2 border-transparent ${subject.hoverBorder}`}
          >
            <div className={`absolute top-0 left-0 w-2 h-full ${subject.color}`} />
            <div className="p-8">
              <h2 className={`text-2xl font-bold mb-2 ${subject.text}`}>
                {subject.name}
              </h2>
              <p className="text-gray-500">
                Access chapter-wise questions and answers for {subject.name}.
              </p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
