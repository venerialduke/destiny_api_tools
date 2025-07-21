import React, { useState, useEffect } from 'react';
import OptimizedImage from '../shared/OptimizedImage';
import demoApiService from '../../services/demo/demoApiService';

const ItemDetail = ({ item, onBack }) => {
  const [fullItemData, setFullItemData] = useState(item);
  const [isLoading, setIsLoading] = useState(false);
  const [imagePerformance, setImagePerformance] = useState(null);
  const [showPerformanceComparison, setShowPerformanceComparison] = useState(false);

  useEffect(() => {
    // Load full item details if we only have basic info
    if (item && !item.rawData) {
      loadFullItemDetails();
    }
    
    // Test image performance
    if (item?.displayProperties?.icon) {
      testImagePerformance();
    }
  }, [item]);

  const loadFullItemDetails = async () => {
    setIsLoading(true);
    try {
      const fullData = await demoApiService.getItemDetails(item.hash);
      setFullItemData(fullData);
    } catch (error) {
      console.error('Failed to load full item details:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const testImagePerformance = async () => {
    try {
      const iconPath = typeof item.displayProperties.icon === 'string' 
        ? item.displayProperties.icon 
        : item.displayProperties.icon.original?.replace('https://bungie.net', '');
      
      if (iconPath) {
        const results = await demoApiService.testImagePerformance(iconPath, ['webp', 'jpg']);
        setImagePerformance(results);
      }
    } catch (error) {
      console.error('Failed to test image performance:', error);
    }
  };

  const getTierColor = (tierType) => {
    switch (tierType) {
      case 6: return 'from-yellow-400 to-yellow-600'; // Exotic
      case 5: return 'from-purple-400 to-purple-600'; // Legendary
      case 4: return 'from-blue-400 to-blue-600'; // Rare
      case 3: return 'from-green-400 to-green-600'; // Uncommon
      default: return 'from-gray-400 to-gray-600'; // Common
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

  const displayProperties = fullItemData?.displayProperties || {};
  const categories = fullItemData?.categories || {};

  return (
    <div className="space-y-8">
      {/* Header with Back Button */}
      <div className="flex items-center space-x-4">
        <button
          onClick={onBack}
          className="flex items-center space-x-2 px-4 py-2 bg-gray-800 hover:bg-gray-700 rounded-lg transition-colors"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7" />
          </svg>
          <span>Back to Search</span>
        </button>
        
        <button
          onClick={() => setShowPerformanceComparison(!showPerformanceComparison)}
          className="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg transition-colors text-sm"
        >
          {showPerformanceComparison ? 'Hide' : 'Show'} Performance Stats
        </button>
      </div>

      {/* Main Item Header */}
      <div className={`relative overflow-hidden rounded-xl bg-gradient-to-br ${getTierColor(fullItemData.tierType)} p-1`}>
        <div className="bg-gray-900 rounded-xl p-8">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-center">
            {/* Large Item Image */}
            <div className="lg:col-span-1">
              <div className="w-48 h-48 mx-auto bg-gray-800 rounded-xl overflow-hidden shadow-2xl">
                <OptimizedImage
                  icon={displayProperties.icon}
                  alt={displayProperties.name}
                  size="large"
                  className="w-full h-full"
                  priority={true}
                  showPerformanceInfo={true}
                />
              </div>
            </div>

            {/* Item Information */}
            <div className="lg:col-span-2 space-y-4">
              <div>
                <div className="flex items-center space-x-3 mb-2">
                  <h1 className="text-3xl font-bold text-white">
                    {displayProperties.name || 'Unknown Item'}
                  </h1>
                  <span className={`px-3 py-1 rounded-full text-sm font-medium bg-gradient-to-r ${getTierColor(fullItemData.tierType)} text-white`}>
                    {getTierName(fullItemData.tierType)}
                  </span>
                </div>
                
                <p className="text-gray-300 text-lg leading-relaxed">
                  {displayProperties.description || 'No description available'}
                </p>
              </div>

              {/* Item Stats */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4">
                <div className="text-center">
                  <div className="text-2xl font-bold text-white">{fullItemData.itemType || 0}</div>
                  <div className="text-sm text-gray-400">Item Type</div>
                </div>
                
                <div className="text-center">
                  <div className="text-2xl font-bold text-white">{fullItemData.classType || 'Any'}</div>
                  <div className="text-sm text-gray-400">Class</div>
                </div>
                
                {fullItemData.powerCap && (
                  <div className="text-center">
                    <div className="text-2xl font-bold text-white">{fullItemData.powerCap}</div>
                    <div className="text-sm text-gray-400">Power Cap</div>
                  </div>
                )}
                
                <div className="text-center">
                  <div className="text-2xl font-bold text-white">{fullItemData.hash}</div>
                  <div className="text-sm text-gray-400">Hash</div>
                </div>
              </div>

              {/* Item Categories */}
              <div className="flex flex-wrap gap-2 pt-4">
                {categories.isWeapon && (
                  <span className="px-3 py-1 bg-red-600/20 text-red-300 rounded-full text-sm">
                    ⚔️ Weapon
                  </span>
                )}
                {categories.isArmor && (
                  <span className="px-3 py-1 bg-blue-600/20 text-blue-300 rounded-full text-sm">
                    🛡️ Armor
                  </span>
                )}
                {categories.isConsumable && (
                  <span className="px-3 py-1 bg-green-600/20 text-green-300 rounded-full text-sm">
                    💊 Consumable
                  </span>
                )}
                {categories.isMod && (
                  <span className="px-3 py-1 bg-purple-600/20 text-purple-300 rounded-full text-sm">
                    🔧 Mod
                  </span>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Performance Comparison */}
      {showPerformanceComparison && imagePerformance && (
        <div className="bg-gray-800 rounded-xl p-6">
          <h3 className="text-xl font-semibold text-white mb-4">Image Performance Comparison</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {Object.entries(imagePerformance).map(([format, data]) => (
              <div key={format} className="bg-gray-700 rounded-lg p-4">
                <div className="flex items-center justify-between mb-3">
                  <h4 className="font-medium text-white capitalize">{format} Format</h4>
                  {data.cacheStatus && (
                    <span className={`px-2 py-1 rounded text-xs ${
                      data.cacheStatus === 'HIT' ? 'bg-green-600 text-white' : 'bg-orange-600 text-white'
                    }`}>
                      {data.cacheStatus}
                    </span>
                  )}
                </div>
                
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between">
                    <span className="text-gray-400">Load Time:</span>
                    <span className="text-white font-medium">{data.duration}ms</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-400">File Size:</span>
                    <span className="text-white font-medium">{data.sizeFormatted}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-400">Format:</span>
                    <span className="text-white font-medium">{format.toUpperCase()}</span>
                  </div>
                </div>

                {/* Performance Bar */}
                <div className="mt-4">
                  <div className="bg-gray-600 rounded-full h-2">
                    <div 
                      className={`h-2 rounded-full ${format === 'webp' ? 'bg-green-500' : 'bg-blue-500'}`}
                      style={{ 
                        width: `${Math.min(100, (data.size / Math.max(...Object.values(imagePerformance).map(d => d.size || 0))) * 100)}%` 
                      }}
                    ></div>
                  </div>
                  <div className="text-xs text-gray-400 mt-1">
                    {format === 'webp' && 'Optimized format'} 
                    {format === 'jpg' && 'Standard format'}
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Optimization Summary */}
          {imagePerformance.webp && imagePerformance.jpg && (
            <div className="mt-6 p-4 bg-green-900/20 border border-green-700 rounded-lg">
              <h4 className="font-medium text-green-300 mb-2">Optimization Benefits</h4>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
                <div>
                  <span className="text-gray-400">Size Reduction:</span>
                  <span className="ml-2 text-green-300 font-medium">
                    {Math.round((1 - imagePerformance.webp.size / imagePerformance.jpg.size) * 100)}%
                  </span>
                </div>
                <div>
                  <span className="text-gray-400">Speed Improvement:</span>
                  <span className="ml-2 text-green-300 font-medium">
                    {Math.round(imagePerformance.jpg.duration / imagePerformance.webp.duration)}x faster
                  </span>
                </div>
                <div>
                  <span className="text-gray-400">Format:</span>
                  <span className="ml-2 text-green-300 font-medium">WebP optimized</span>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Mock Perks Section */}
      <div className="bg-gray-800 rounded-xl p-6">
        <h3 className="text-xl font-semibold text-white mb-4">Available Perks & Traits</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          {/* Mock perk icons - in a real implementation, these would come from the API */}
          {[1, 2, 3, 4, 5, 6].map((index) => (
            <div key={index} className="bg-gray-700 rounded-lg p-3 text-center hover:bg-gray-600 transition-colors">
              <div className="w-12 h-12 mx-auto mb-2 bg-gray-600 rounded-lg flex items-center justify-center">
                <OptimizedImage
                  icon={{
                    optimized: {
                      small: `/api/images/proxy/common/destiny2_content/icons/804b3ab35037730a4f93cc33a9282081.jpg?format=webp&size=small`
                    }
                  }}
                  alt={`Perk ${index}`}
                  size="small"
                  className="w-full h-full"
                />
              </div>
              <div className="text-xs text-gray-300">Perk {index}</div>
            </div>
          ))}
        </div>
        <p className="text-gray-400 text-sm mt-4">
          * Perk data integration coming soon. This demonstrates optimized icon loading for game assets.
        </p>
      </div>

      {/* Mock Sockets Section */}
      <div className="bg-gray-800 rounded-xl p-6">
        <h3 className="text-xl font-semibold text-white mb-4">Mod Sockets & Compatibility</h3>
        <div className="space-y-4">
          {[1, 2, 3].map((socket) => (
            <div key={socket} className="bg-gray-700 rounded-lg p-4">
              <div className="flex items-center space-x-4">
                <div className="w-8 h-8 bg-gray-600 rounded-lg flex items-center justify-center">
                  <span className="text-xs font-medium">{socket}</span>
                </div>
                <div className="flex-1">
                  <h4 className="font-medium text-white">Socket {socket}</h4>
                  <p className="text-sm text-gray-400">Compatible with various enhancement mods</p>
                </div>
                <div className="flex space-x-2">
                  {[1, 2, 3, 4].map((mod) => (
                    <div key={mod} className="w-8 h-8 bg-gray-600 rounded">
                      <OptimizedImage
                        icon={{
                          optimized: {
                            small: `/api/images/proxy/common/destiny2_content/icons/804b3ab35037730a4f93cc33a9282081.jpg?format=webp&size=small`
                          }
                        }}
                        alt={`Mod ${mod}`}
                        size="small"
                        className="w-full h-full"
                      />
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
        <p className="text-gray-400 text-sm mt-4">
          * Socket data integration coming soon. This demonstrates how mod icons would load with optimization.
        </p>
      </div>

      {/* Loading State */}
      {isLoading && (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4 text-gray-400">Loading additional item details...</p>
        </div>
      )}
    </div>
  );
};

export default ItemDetail;