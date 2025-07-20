import React from 'react';
import { Shield, Zap, Clock } from 'lucide-react';

const CharacterCard = ({ character, isSelected = false, onClick, showPlatform = true }) => {
  // Class icons/colors mapping
  const classStyles = {
    0: { // Titan
      color: 'from-orange-500 to-red-600',
      icon: Shield,
      name: 'Titan'
    },
    1: { // Hunter
      color: 'from-blue-500 to-indigo-600',
      icon: Zap,
      name: 'Hunter'
    },
    2: { // Warlock
      color: 'from-purple-500 to-pink-600',
      icon: Zap,
      name: 'Warlock'
    }
  };

  // Platform names mapping
  const platformNames = {
    1: 'Xbox',
    2: 'PlayStation',
    3: 'Steam',
    4: 'Blizzard',
    5: 'Stadia',
    6: 'Epic Games'
  };

  const classStyle = classStyles[character.character_class] || classStyles[0];
  const ClassIcon = classStyle.icon;

  const handleClick = () => {
    if (onClick) {
      onClick(character);
    }
  };

  return (
    <div 
      className={`
        relative bg-white rounded-xl shadow-lg overflow-hidden cursor-pointer transition-all duration-200 hover:shadow-xl hover:scale-105
        ${isSelected ? 'ring-2 ring-blue-500 ring-offset-2' : ''}
      `}
      onClick={handleClick}
    >
      {/* Emblem Background */}
      <div className={`relative h-32 bg-gradient-to-r ${classStyle.color}`}>
        {character.emblem_background_path && (
          <img 
            src={`https://www.bungie.net${character.emblem_background_path}`}
            alt="Character emblem background"
            className="w-full h-full object-cover"
            onError={(e) => {
              e.target.style.display = 'none';
            }}
          />
        )}
        
        {/* Overlay */}
        <div className="absolute inset-0 bg-black bg-opacity-30"></div>
        
        {/* Platform Badge */}
        {showPlatform && (
          <div className="absolute top-2 right-2">
            <span className="bg-black bg-opacity-50 text-white text-xs px-2 py-1 rounded-full">
              {platformNames[character.membership_type] || 'Unknown'}
            </span>
          </div>
        )}
        
        {/* Character Class Info */}
        <div className="absolute bottom-4 left-4 text-white">
          <div className="flex items-center space-x-2 mb-1">
            <ClassIcon className="w-5 h-5" />
            <h3 className="text-lg font-bold">{character.character_class_name}</h3>
          </div>
          <p className="text-sm opacity-90">
            {character.race_name} • {character.gender_name}
          </p>
        </div>
        
        {/* Power Level */}
        <div className="absolute bottom-4 right-4 text-white text-right">
          <div className="text-2xl font-bold">{character.light_level}</div>
          <div className="text-xs opacity-90">Power</div>
        </div>
        
        {/* Selected Indicator */}
        {isSelected && (
          <div className="absolute top-2 left-2">
            <div className="bg-blue-500 text-white rounded-full p-1">
              <Shield className="w-4 h-4" />
            </div>
          </div>
        )}
      </div>

      {/* Character Stats */}
      <div className="p-4">
        <div className="grid grid-cols-2 gap-4 text-sm">
          <div>
            <span className="text-gray-500">Level</span>
            <div className="font-semibold text-gray-900">{character.level}</div>
          </div>
          
          <div>
            <span className="text-gray-500">Base Level</span>
            <div className="font-semibold text-gray-900">{character.base_character_level}</div>
          </div>
        </div>
        
        {/* Playtime */}
        {character.minutes_played_total && (
          <div className="mt-3 pt-3 border-t border-gray-200">
            <div className="flex items-center text-sm text-gray-600">
              <Clock className="w-4 h-4 mr-1" />
              <span>
                {Math.floor(character.minutes_played_total / 60)}h played
              </span>
            </div>
          </div>
        )}
        
        {/* Last Played */}
        <div className="mt-2">
          <div className="text-xs text-gray-500">
            Last played: {new Date(character.date_last_played).toLocaleDateString()}
          </div>
        </div>
        
        {/* Progress to next level */}
        {character.percent_to_next_level > 0 && (
          <div className="mt-3">
            <div className="flex justify-between text-xs text-gray-600 mb-1">
              <span>Level Progress</span>
              <span>{character.percent_to_next_level}%</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div 
                className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                style={{ width: `${character.percent_to_next_level}%` }}
              ></div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CharacterCard;