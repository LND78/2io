import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import Link from 'next/link';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'SST Shekhavati Mission 100',
  description: 'Question Bank for SST Shekhavati Mission 100',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="flex flex-col min-h-screen bg-gray-50 text-gray-900">
          <header className="bg-white shadow-sm sticky top-0 z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
              <Link href="/" className="text-xl font-bold text-gray-900">
                SST Shekhavati Mission 100
              </Link>
              <nav className="hidden md:flex space-x-4 text-sm font-medium text-gray-500">
                <Link href="/" className="hover:text-gray-900 transition-colors">
                  Home
                </Link>
                <Link href="/history" className="hover:text-red-600 transition-colors">
                  History
                </Link>
                <Link href="/geography" className="hover:text-green-600 transition-colors">
                  Geography
                </Link>
                <Link href="/political-science" className="hover:text-blue-600 transition-colors">
                  Pol. Science
                </Link>
                <Link href="/economics" className="hover:text-yellow-600 transition-colors">
                  Economics
                </Link>
              </nav>
              {/* Mobile menu could be added here, simplified for now */}
            </div>
          </header>

          <main className="flex-grow w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {children}
          </main>

          <footer className="bg-white border-t border-gray-200 mt-auto">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 text-center text-sm text-gray-500">
              &copy; {new Date().getFullYear()} SST Shekhavati Mission 100. All rights reserved.
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}
