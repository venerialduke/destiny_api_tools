import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { Shield, LogOut, User } from 'lucide-react';

const Header = () => {
  const { isAuthenticated, user, characters, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo and Brand */}
          <Link to="/" className="flex items-center space-x-2">
            <Shield className="w-8 h-8 text-blue-600" />
            <span className="text-xl font-bold text-gray-900">
              Destiny API Tools
            </span>
          </Link>

          {/* Navigation */}
          <nav className="hidden md:flex space-x-8">
            <Link 
              to="/" 
              className="text-gray-700 hover:text-blue-600 transition-colors"
            >
              Home
            </Link>
            <Link 
              to="/explore" 
              className="text-gray-700 hover:text-blue-600 transition-colors"
            >
              Explore
            </Link>
            <Link 
              to="/manifest-explorer" 
              className="text-gray-700 hover:text-blue-600 transition-colors"
            >
              Manifest Explorer
            </Link>
            <Link 
              to="/equipable-sets" 
              className="text-gray-700 hover:text-blue-600 transition-colors"
            >
              Equipable Sets
            </Link>
            {isAuthenticated && (
              <>
                <Link 
                  to="/tools/inventory" 
                  className="text-gray-700 hover:text-blue-600 transition-colors"
                >
                  Inventory
                </Link>
                <Link 
                  to="/tools/loadouts" 
                  className="text-gray-700 hover:text-blue-600 transition-colors"
                >
                  Loadouts
                </Link>
                <Link 
                  to="/tools/stats" 
                  className="text-gray-700 hover:text-blue-600 transition-colors"
                >
                  Stats
                </Link>
              </>
            )}
          </nav>

          {/* Auth Section */}
          <div className="flex items-center space-x-4">
            {isAuthenticated ? (
              <div className="flex items-center space-x-4">
                <div className="flex items-center space-x-2">
                  <User className="w-5 h-5 text-gray-600" />
                  <div className="text-right">
                    <div className="text-sm font-medium text-gray-900">
                      {user?.displayName || 'Guardian'}
                    </div>
                    {characters.length > 0 && (
                      <div className="text-xs text-gray-500">
                        {characters.length} character{characters.length !== 1 ? 's' : ''}
                      </div>
                    )}
                  </div>
                </div>
                <button
                  onClick={handleLogout}
                  className="flex items-center space-x-2 text-gray-700 hover:text-red-600 transition-colors"
                >
                  <LogOut className="w-5 h-5" />
                  <span>Logout</span>
                </button>
              </div>
            ) : (
              <Link
                to="/login"
                className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
              >
                Login with Bungie
              </Link>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;