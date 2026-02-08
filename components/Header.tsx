import React from 'react';
import Link from 'next/link';

const Header = () => {
  return (
    <header className="bg-indigo-700 text-white shadow-lg sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4 flex justify-between items-center flex-wrap">
        <Link href="/" className="text-xl font-bold tracking-tight hover:text-indigo-200 transition-colors mb-2 md:mb-0">
          SST Shekhavati Mission 100
        </Link>
        <nav className="flex space-x-4 text-sm md:text-base">
          <Link href="/history" className="hover:text-indigo-200 transition-colors">History</Link>
          <Link href="/geography" className="hover:text-indigo-200 transition-colors">Geography</Link>
          <Link href="/political-science" className="hover:text-indigo-200 transition-colors">Pol. Sci.</Link>
          <Link href="/economics" className="hover:text-indigo-200 transition-colors">Economics</Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;
