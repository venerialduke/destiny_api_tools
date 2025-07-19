import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';

const Sidebar = ({ isOpen, onClose }) => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) return null;

  return (
    <div className={`fixed inset-y-0 left-0 z-50 w-64 bg-gray-800 text-white transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0`}>
      <div className="flex items-center justify-between h-16 px-4 bg-gray-900">
        <span className="text-xl font-semibold">Tools</span>
        <button
          onClick={onClose}
          className="lg:hidden text-gray-400 hover:text-white"
        >
          ×
        </button>
      </div>
      <nav className="mt-8">
        <div className="px-4 space-y-2">
          <Link
            to="/characters"
            className="block px-4 py-2 rounded hover:bg-gray-700"
            onClick={onClose}
          >
            Characters
          </Link>
          <div className="text-gray-400 text-sm uppercase tracking-wide px-4 py-2 mt-4">
            Tools (Coming Soon)
          </div>
          <div className="text-gray-500 px-4 py-2 text-sm">
            • Inventory Manager
          </div>
          <div className="text-gray-500 px-4 py-2 text-sm">
            • Loadout Manager
          </div>
          <div className="text-gray-500 px-4 py-2 text-sm">
            • Stats Tracker
          </div>
          <div className="text-gray-500 px-4 py-2 text-sm">
            • Vendor Tracker
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Sidebar;