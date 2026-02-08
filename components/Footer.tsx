import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-6 mt-auto">
      <div className="container mx-auto px-4 text-center">
        <p className="text-sm text-gray-400">
          &copy; {new Date().getFullYear()} SST Shekhavati Mission 100. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
