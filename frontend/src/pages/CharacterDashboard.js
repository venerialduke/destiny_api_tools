import React, { useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import CharacterList from '../components/shared/CharacterList';
import { userService } from '../services/userService';
import { Loader, RefreshCw, AlertCircle } from 'lucide-react';
import toast from 'react-hot-toast';

const CharacterDashboard = () => {
  const { isAuthenticated, characters: authCharacters, user, primaryMembership } = useAuth();
  const [characters, setCharacters] = useState(authCharacters || []);
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [error, setError] = useState(null);

  // Redirect if not authenticated
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  useEffect(() => {
    // Initialize with auth context characters
    if (authCharacters && authCharacters.length > 0) {
      setCharacters(authCharacters);
      // Set the first character as selected by default
      setSelectedCharacter(authCharacters[0]);
    }
  }, [authCharacters]);

  const refreshCharacterData = async () => {
    if (!primaryMembership) {
      toast.error('No primary membership found');
      return;
    }

    setIsRefreshing(true);
    setError(null);

    try {
      const characterData = await userService.getCharacters(
        primaryMembership.membershipType,
        primaryMembership.membershipId
      );
      
      setCharacters(characterData.characters);
      toast.success('Character data refreshed');
    } catch (err) {
      console.error('Failed to refresh character data:', err);
      setError(err.message);
      toast.error('Failed to refresh character data');
    } finally {
      setIsRefreshing(false);
    }
  };

  const handleCharacterSelect = (character) => {
    setSelectedCharacter(character);
  };

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <Loader className="w-12 h-12 text-blue-600 mx-auto animate-spin mb-4" />
          <p className="text-lg text-gray-600">Loading character data...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header Section */}
      <div className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                Character Dashboard
              </h1>
              <p className="text-lg text-gray-600 mt-1">
                Welcome back, {user?.displayName || 'Guardian'}
              </p>
            </div>
            
            <button
              onClick={refreshCharacterData}
              disabled={isRefreshing}
              className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
            >
              <RefreshCw className={`w-4 h-4 mr-2 ${isRefreshing ? 'animate-spin' : ''}`} />
              Refresh Data
            </button>
          </div>
        </div>
      </div>

      {/* Error Banner */}
      {error && (
        <div className="bg-red-50 border-l-4 border-red-400 p-4">
          <div className="flex">
            <AlertCircle className="w-5 h-5 text-red-400" />
            <div className="ml-3">
              <p className="text-sm text-red-700">{error}</p>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {characters.length === 0 ? (
          <div className="text-center py-12">
            <div className="bg-white rounded-lg shadow-sm p-8">
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                No Characters Found
              </h3>
              <p className="text-gray-600 mb-4">
                We couldn't find any Destiny 2 characters on your account.
              </p>
              <button
                onClick={refreshCharacterData}
                className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
              >
                Retry
              </button>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Character List */}
            <div className="lg:col-span-2">
              <CharacterList
                characters={characters}
                selectedCharacter={selectedCharacter}
                onCharacterSelect={handleCharacterSelect}
                isLoading={isRefreshing}
              />
            </div>

            {/* Character Details Sidebar */}
            <div className="lg:col-span-1">
              {selectedCharacter ? (
                <div className="bg-white rounded-lg shadow-sm p-6 sticky top-8">
                  <h3 className="text-lg font-semibold text-gray-900 mb-4">
                    Character Details
                  </h3>
                  
                  {/* Character Info */}
                  <div className="space-y-4">
                    <div>
                      <label className="text-sm font-medium text-gray-500">Class</label>
                      <p className="text-lg font-semibold text-gray-900">
                        {selectedCharacter.character_class_name}
                      </p>
                    </div>
                    
                    <div>
                      <label className="text-sm font-medium text-gray-500">Race</label>
                      <p className="text-lg text-gray-700">
                        {selectedCharacter.race_name}
                      </p>
                    </div>
                    
                    <div>
                      <label className="text-sm font-medium text-gray-500">Power Level</label>
                      <p className="text-2xl font-bold text-blue-600">
                        {selectedCharacter.light_level}
                      </p>
                    </div>
                    
                    <div>
                      <label className="text-sm font-medium text-gray-500">Level</label>
                      <p className="text-lg text-gray-700">
                        {selectedCharacter.level}
                      </p>
                    </div>
                    
                    {selectedCharacter.minutes_played_total && (
                      <div>
                        <label className="text-sm font-medium text-gray-500">Playtime</label>
                        <p className="text-lg text-gray-700">
                          {Math.floor(selectedCharacter.minutes_played_total / 60)} hours
                        </p>
                      </div>
                    )}
                    
                    <div>
                      <label className="text-sm font-medium text-gray-500">Last Played</label>
                      <p className="text-sm text-gray-700">
                        {new Date(selectedCharacter.date_last_played).toLocaleDateString()}
                      </p>
                    </div>
                  </div>
                  
                  {/* Action Buttons */}
                  <div className="mt-6 space-y-3">
                    <button className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors">
                      View Inventory
                    </button>
                    <button className="w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors">
                      Manage Loadouts
                    </button>
                    <button className="w-full bg-purple-600 text-white py-2 px-4 rounded-lg hover:bg-purple-700 transition-colors">
                      View Stats
                    </button>
                  </div>
                </div>
              ) : (
                <div className="bg-white rounded-lg shadow-sm p-6">
                  <p className="text-gray-600 text-center">
                    Select a character to view details
                  </p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CharacterDashboard;