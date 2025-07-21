import React, { useState } from 'react';
import OptimizedImage from '../shared/OptimizedImage';

const ItemCard = ({ item, onClick, priority = false }) => {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [loadTime, setLoadTime] = useState(null);

  const handleImageLoad = (duration) => {
    setImageLoaded(true);
    setLoadTime(duration);
  };

  const getTierColor = (tierType) => {
    switch (tierType) {
      case 6: return 'border-yellow-400 bg-yellow-400/10'; // Exotic
      case 5: return 'border-purple-400 bg-purple-400/10'; // Legendary
      case 4: return 'border-blue-400 bg-blue-400/10'; // Rare
      case 3: return 'border-green-400 bg-green-400/10'; // Uncommon
      default: return 'border-gray-400 bg-gray-400/10'; // Common
    }
  };

  const getTierName = (tierType) => {
    switch (tierType) {
      case 6: return 'Exotic';
      case 5: return 'Legendary';
      case 4: return 'Rare';
      case 3: return 'Uncommon';
      default: return 'Common';
    }
  };

  const getItemTypeIcon = (item) => {
    if (item.categories?.isWeapon) return '⚔️';
    if (item.categories?.isArmor) return '🛡️';
    if (item.categories?.isConsumable) return '💊';
    if (item.categories?.isMod) return '🔧';
    if (item.categories?.isEmblem) return '🎖️';
    if (item.categories?.isGhost) return '👻';
    if (item.categories?.isShip) return '🚀';
    if (item.categories?.isSparrow) return '🏍️';
    if (item.categories?.isShader) return '🎨';
    return '📦';
  };

  const displayProperties = item.displayProperties || {};
  const icon = displayProperties.icon;
  const name = displayProperties.name || 'Unknown Item';
  const description = displayProperties.description || 'No description available';

  return (
    <div
      onClick={onClick}
      className={`group relative bg-gray-800 rounded-lg border-2 ${getTierColor(
        item.tierType
      )} p-4 cursor-pointer transition-all duration-200 hover:scale-105 hover:shadow-lg hover:shadow-current/20`}
    >
      {/* Image Container */}
      <div className="relative mb-3">
        <div className="w-16 h-16 mx-auto bg-gray-700 rounded-lg overflow-hidden">
          {icon && (
            <OptimizedImage
              icon={icon}
              alt={name}
              size="small"
              className="w-full h-full object-cover"
              priority={priority}
              onLoadComplete={handleImageLoad}
            />
          )}
        </div>

        {/* Loading Indicator */}
        {!imageLoaded && icon && (
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-500"></div>
          </div>
        )}

        {/* Performance Badge */}
        {imageLoaded && loadTime !== null && (
          <div className="absolute -top-2 -right-2 bg-green-600 text-white text-xs px-2 py-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
            {loadTime}ms
          </div>
        )}

        {/* Item Type Icon */}
        <div className="absolute -bottom-1 -right-1 text-lg">
          {getItemTypeIcon(item)}
        </div>
      </div>

      {/* Item Info */}
      <div className="text-center space-y-2">
        {/* Item Name */}
        <h3 className="font-medium text-white text-sm leading-tight line-clamp-2" title={name}>
          {name}
        </h3>

        {/* Tier Type */}
        <div className="flex items-center justify-center space-x-2">
          <span className="text-xs font-medium text-current">
            {getTierName(item.tierType)}
          </span>
          {item.powerCap && (
            <span className="text-xs text-gray-400">
              {item.powerCap}
            </span>
          )}
        </div>

        {/* Item Categories */}
        {item.categories && (
          <div className="flex justify-center space-x-1">
            {item.categories.isWeapon && (
              <span className="text-xs bg-red-600/20 text-red-300 px-2 py-1 rounded">
                Weapon
              </span>
            )}
            {item.categories.isArmor && (
              <span className="text-xs bg-blue-600/20 text-blue-300 px-2 py-1 rounded">
                Armor
              </span>
            )}
          </div>
        )}
      </div>

      {/* Hover Overlay */}
      <div className="absolute inset-0 bg-white/5 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none" />

      {/* Click Hint */}
      <div className="absolute bottom-2 left-2 right-2 text-center opacity-0 group-hover:opacity-100 transition-opacity">
        <span className="text-xs text-gray-300">Click for details</span>
      </div>
    </div>
  );
};

export default ItemCard;