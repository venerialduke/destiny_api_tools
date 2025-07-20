import React, { useState } from 'react';
import CharacterCard from './CharacterCard';
import { Grid, List, Filter, Search } from 'lucide-react';

const CharacterList = ({ 
  characters = [], 
  selectedCharacter, 
  onCharacterSelect, 
  isLoading = false,
  showFilters = true,
  showSearch = true 
}) => {
  const [viewMode, setViewMode] = useState('grid'); // 'grid' or 'list'
  const [filterClass, setFilterClass] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('lastPlayed'); // 'lastPlayed', 'powerLevel', 'class', 'playtime'

  // Filter and sort characters
  const filteredAndSortedCharacters = characters
    .filter(character => {
      // Class filter
      if (filterClass !== 'all' && character.character_class !== parseInt(filterClass)) {
        return false;
      }
      
      // Search filter
      if (searchTerm) {
        const searchLower = searchTerm.toLowerCase();
        return (
          character.character_class_name.toLowerCase().includes(searchLower) ||
          character.race_name.toLowerCase().includes(searchLower) ||
          character.gender_name.toLowerCase().includes(searchLower)
        );
      }
      
      return true;
    })
    .sort((a, b) => {
      switch (sortBy) {
        case 'powerLevel':
          return b.light_level - a.light_level;
        case 'class':
          return a.character_class_name.localeCompare(b.character_class_name);
        case 'playtime':
          return (b.minutes_played_total || 0) - (a.minutes_played_total || 0);
        case 'lastPlayed':
        default:
          return new Date(b.date_last_played) - new Date(a.date_last_played);
      }
    });

  const handleCharacterClick = (character) => {
    if (onCharacterSelect) {
      onCharacterSelect(character);
    }
  };

  if (isLoading) {
    return (
      <div className="space-y-4">
        {[1, 2, 3].map(i => (
          <div key={i} className="animate-pulse">
            <div className="bg-gray-200 rounded-xl h-48"></div>
          </div>
        ))}
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Your Characters</h2>
          <p className="text-gray-600">
            {characters.length} character{characters.length !== 1 ? 's' : ''} found
          </p>
        </div>
        
        {/* View Mode Toggle */}
        <div className="flex items-center space-x-2">
          <button
            onClick={() => setViewMode('grid')}
            className={`p-2 rounded-lg ${
              viewMode === 'grid' 
                ? 'bg-blue-100 text-blue-600' 
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            <Grid className="w-5 h-5" />
          </button>
          <button
            onClick={() => setViewMode('list')}
            className={`p-2 rounded-lg ${
              viewMode === 'list' 
                ? 'bg-blue-100 text-blue-600' 
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            <List className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Filters and Search */}
      {(showFilters || showSearch) && (
        <div className="bg-white rounded-lg shadow-sm p-4">
          <div className="flex flex-col sm:flex-row gap-4">
            {/* Search */}
            {showSearch && (
              <div className="flex-1">
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                  <input
                    type="text"
                    placeholder="Search characters..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
              </div>
            )}
            
            {/* Filters */}
            {showFilters && (
              <div className="flex gap-4">
                {/* Class Filter */}
                <select
                  value={filterClass}
                  onChange={(e) => setFilterClass(e.target.value)}
                  className="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option value="all">All Classes</option>
                  <option value="0">Titan</option>
                  <option value="1">Hunter</option>
                  <option value="2">Warlock</option>
                </select>
                
                {/* Sort */}
                <select
                  value={sortBy}
                  onChange={(e) => setSortBy(e.target.value)}
                  className="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option value="lastPlayed">Last Played</option>
                  <option value="powerLevel">Power Level</option>
                  <option value="class">Class</option>
                  <option value="playtime">Playtime</option>
                </select>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Character Grid/List */}
      {filteredAndSortedCharacters.length === 0 ? (
        <div className="text-center py-12">
          <div className="bg-white rounded-lg shadow-sm p-8">
            <Filter className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              No characters found
            </h3>
            <p className="text-gray-600">
              Try adjusting your search or filter criteria.
            </p>
          </div>
        </div>
      ) : (
        <div className={
          viewMode === 'grid' 
            ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'
            : 'space-y-4'
        }>
          {filteredAndSortedCharacters.map((character) => (
            <CharacterCard
              key={character.character_id}
              character={character}
              isSelected={selectedCharacter?.character_id === character.character_id}
              onClick={handleCharacterClick}
              showPlatform={characters.some(c => c.membership_type !== character.membership_type)}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default CharacterList;