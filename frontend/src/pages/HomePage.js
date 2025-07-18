import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Package, 
  Settings, 
  BarChart3, 
  Users, 
  ShoppingCart,
  Shield,
  Zap,
  Star
} from 'lucide-react';

const HomePage = () => {
  const tools = [
    {
      id: 'inventory',
      name: 'Inventory Manager',
      description: 'Manage your weapons, armor, and items across all characters',
      icon: Package,
      path: '/tools/inventory',
      color: 'bg-blue-500',
      features: ['Transfer items', 'View all characters', 'Vault management']
    },
    {
      id: 'loadouts',
      name: 'Loadout Manager',
      description: 'Create, save, and quickly switch between equipment loadouts',
      icon: Settings,
      path: '/tools/loadouts',
      color: 'bg-green-500',
      features: ['Save loadouts', 'Quick equip', 'Build optimizer']
    },
    {
      id: 'stats',
      name: 'Stats Tracker',
      description: 'Track your performance and view detailed statistics',
      icon: BarChart3,
      path: '/tools/stats',
      color: 'bg-purple-500',
      features: ['Activity history', 'Performance metrics', 'Leaderboards']
    },
    {
      id: 'fireteam',
      name: 'Fireteam Finder',
      description: 'Find and create fireteams for activities',
      icon: Users,
      path: '/tools/fireteam',
      color: 'bg-orange-500',
      features: ['LFG system', 'Activity matching', 'Team coordination']
    },
    {
      id: 'vendors',
      name: 'Vendor Tracker',
      description: 'Track vendor inventories and get notified of good rolls',
      icon: ShoppingCart,
      path: '/tools/vendors',
      color: 'bg-red-500',
      features: ['Vendor monitoring', 'Roll alerts', 'Inventory tracking']
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-700 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Destiny API Tools
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-blue-100">
              Comprehensive tools for Destiny 2 players to manage inventory, 
              track stats, and enhance your Guardian experience
            </p>
            <div className="flex justify-center items-center space-x-4">
              <Shield className="w-8 h-8" />
              <Zap className="w-8 h-8" />
              <Star className="w-8 h-8" />
            </div>
          </div>
        </div>
      </div>

      {/* Tools Grid */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Choose Your Tool
          </h2>
          <p className="text-lg text-gray-600">
            Select from our collection of specialized tools designed to enhance your Destiny 2 experience
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {tools.map((tool) => {
            const IconComponent = tool.icon;
            return (
              <div 
                key={tool.id}
                className="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 overflow-hidden"
              >
                <div className="p-6">
                  <div className="flex items-center mb-4">
                    <div className={`${tool.color} p-3 rounded-lg text-white mr-4`}>
                      <IconComponent className="w-6 h-6" />
                    </div>
                    <h3 className="text-xl font-semibold text-gray-900">
                      {tool.name}
                    </h3>
                  </div>
                  
                  <p className="text-gray-600 mb-4">
                    {tool.description}
                  </p>
                  
                  <div className="mb-6">
                    <h4 className="text-sm font-medium text-gray-900 mb-2">Features:</h4>
                    <ul className="text-sm text-gray-600 space-y-1">
                      {tool.features.map((feature, index) => (
                        <li key={index} className="flex items-center">
                          <span className="w-1.5 h-1.5 bg-blue-500 rounded-full mr-2"></span>
                          {feature}
                        </li>
                      ))}
                    </ul>
                  </div>
                  
                  <Link
                    to={tool.path}
                    className="block w-full bg-gray-900 text-white text-center py-3 px-4 rounded-lg hover:bg-gray-800 transition-colors duration-200 font-medium"
                  >
                    Launch Tool
                  </Link>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Features Section */}
      <div className="bg-gray-900 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">
              Built for Guardians, by Guardians
            </h2>
            <p className="text-xl text-gray-300">
              Our tools are designed with the Destiny 2 community in mind
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-blue-600 p-4 rounded-full w-16 h-16 mx-auto mb-4">
                <Shield className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Secure & Private</h3>
              <p className="text-gray-300">
                Your data is protected with industry-standard security measures
              </p>
            </div>
            
            <div className="text-center">
              <div className="bg-green-600 p-4 rounded-full w-16 h-16 mx-auto mb-4">
                <Zap className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Fast & Reliable</h3>
              <p className="text-gray-300">
                Optimized for speed with real-time updates from the Bungie API
              </p>
            </div>
            
            <div className="text-center">
              <div className="bg-purple-600 p-4 rounded-full w-16 h-16 mx-auto mb-4">
                <Star className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Community Driven</h3>
              <p className="text-gray-300">
                Built with feedback from the Destiny 2 community
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;