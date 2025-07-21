import React, { useState, useEffect } from 'react';
import { Search, Database, Link, ChevronRight, Hash, Eye } from 'lucide-react';
import { explorationService } from '../services/explorationService';

const ExplorationPage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState(null);
  const [selectedEntity, setSelectedEntity] = useState(null);
  const [entityDetails, setEntityDetails] = useState(null);
  const [connections, setConnections] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [manifestStructure, setManifestStructure] = useState(null);
  const [explorationPath, setExplorationPath] = useState([]);

  // Load manifest structure on component mount
  useEffect(() => {
    const loadStructure = async () => {
      try {
        const structure = await explorationService.getManifestStructure();
        setManifestStructure(structure);
      } catch (err) {
        setError('Failed to load manifest structure');
      }
    };
    loadStructure();
  }, []);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    setLoading(true);
    setError(null);
    
    try {
      const results = await explorationService.universalSearch(searchQuery);
      console.log('Search results:', results);
      setSearchResults(results);
    } catch (err) {
      console.error('Search error:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleEntitySelect = async (entity) => {
    setSelectedEntity(entity);
    setLoading(true);
    setError(null);

    try {
      const [details, entityConnections] = await Promise.all([
        explorationService.getEntityDetails(entity.table, entity.hash),
        explorationService.findConnections(entity.table, entity.hash)
      ]);
      
      setEntityDetails(details);
      setConnections(entityConnections);
      
      // Add to exploration path if not already there
      if (!explorationPath.some(item => item.hash === entity.hash && item.table === entity.table)) {
        setExplorationPath(prev => [...prev, {
          hash: entity.hash,
          table: entity.table,
          name: entity.name,
          type: entity.type
        }]);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const clearExploration = () => {
    setSearchResults(null);
    setSelectedEntity(null);
    setEntityDetails(null);
    setConnections(null);
    setExplorationPath([]);
    setError(null);
  };

  return (
    <div className="max-w-7xl mx-auto p-6">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Manifest Explorer</h1>
        <p className="text-gray-600">
          Discover relationships between Destiny content. Search for armor sets, weapon families, 
          quest chains, and explore how game entities connect to each other.
        </p>
      </div>

      {/* Manifest Structure Overview */}
      {manifestStructure && (
        <div className="bg-blue-50 rounded-lg p-4 mb-6">
          <div className="flex items-center gap-2 mb-3">
            <Database className="h-5 w-5 text-blue-600" />
            <h2 className="text-lg font-semibold text-blue-900">Database Overview</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
            <div>
              <span className="font-medium">Tables:</span> {manifestStructure.database_info.total_tables}
            </div>
            <div>
              <span className="font-medium">Total Records:</span> {manifestStructure.database_info.total_records.toLocaleString()}
            </div>
            <div>
              <span className="font-medium">Relationship Types:</span> {manifestStructure.relationship_info.common_patterns.length}
            </div>
          </div>
        </div>
      )}

      {/* Search Interface */}
      <div className="bg-white rounded-lg shadow-sm border p-6 mb-6">
        <form onSubmit={handleSearch} className="flex gap-4">
          <div className="flex-1">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search for items, activities, vendors... (e.g., 'armor set', 'exotic', 'raid')"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <button
            type="submit"
            disabled={loading || !searchQuery.trim()}
            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
          >
            <Search className="h-4 w-4" />
            Search
          </button>
          {(searchResults || selectedEntity) && (
            <button
              type="button"
              onClick={clearExploration}
              className="px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600"
            >
              Clear
            </button>
          )}
        </form>
      </div>

      {/* Exploration Path */}
      {explorationPath.length > 0 && (
        <div className="bg-green-50 rounded-lg p-4 mb-6">
          <h3 className="font-semibold text-green-900 mb-2">Exploration Path</h3>
          <div className="flex items-center gap-2 flex-wrap">
            {explorationPath.map((item, index) => (
              <React.Fragment key={`${item.table}-${item.hash}`}>
                <button
                  onClick={() => handleEntitySelect(item)}
                  className="px-3 py-1 bg-green-100 text-green-800 rounded-lg hover:bg-green-200 text-sm"
                >
                  {item.name}
                </button>
                {index < explorationPath.length - 1 && (
                  <ChevronRight className="h-4 w-4 text-green-600" />
                )}
              </React.Fragment>
            ))}
          </div>
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
          <p className="text-red-800">{error}</p>
        </div>
      )}

      {loading && (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
          <p className="text-gray-600 mt-2">Searching...</p>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Search Results */}
        {searchResults && (
          <div className="bg-white rounded-lg shadow-sm border">
            <div className="p-4 border-b">
              <h2 className="text-lg font-semibold">Search Results</h2>
              <p className="text-sm text-gray-600">
                Found {searchResults.total_found} results across {searchResults.tables_searched} tables
              </p>
              {searchResults.total_found === 0 && (
                <div className="mt-2 p-3 bg-yellow-50 border border-yellow-200 rounded">
                  <p className="text-yellow-800 text-sm">
                    No results found. This could be because:
                    <ul className="mt-1 ml-4 text-xs">
                      <li>• The search term doesn't match any items</li>
                      <li>• Database tables might be empty or have different structure</li>
                      <li>• Check browser console for API errors</li>
                    </ul>
                  </p>
                </div>
              )}
            </div>
            <div className="p-4 max-h-96 overflow-y-auto">
              {Object.entries(searchResults.results).map(([tableName, tableData]) => (
                <div key={tableName} className="mb-4">
                  <h3 className="font-medium text-gray-900 mb-2 capitalize">
                    {tableData.type}s ({tableData.count})
                  </h3>
                  <div className="space-y-2">
                    {tableData.results.map((item) => (
                      <button
                        key={`${item.table}-${item.hash}`}
                        onClick={() => handleEntitySelect(item)}
                        className="w-full text-left p-3 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
                      >
                        <div className="font-medium text-gray-900">{item.name}</div>
                        <div className="text-sm text-gray-600 mt-1">{item.description}</div>
                        <div className="flex items-center gap-2 mt-2 text-xs text-gray-500">
                          <Hash className="h-3 w-3" />
                          {item.hash}
                          <span className="text-gray-400">•</span>
                          {item.type}
                        </div>
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Entity Details & Connections */}
        {selectedEntity && entityDetails && (
          <div className="bg-white rounded-lg shadow-sm border">
            <div className="p-4 border-b">
              <h2 className="text-lg font-semibold flex items-center gap-2">
                <Eye className="h-5 w-5" />
                Entity Details
              </h2>
              <p className="text-sm text-gray-600">{selectedEntity.name}</p>
            </div>
            <div className="p-4 max-h-96 overflow-y-auto">
              {/* Basic Info */}
              <div className="mb-4">
                <h3 className="font-medium text-gray-900 mb-2">Basic Information</h3>
                <div className="text-sm space-y-1">
                  <div><span className="font-medium">Hash:</span> {entityDetails.entity.hash}</div>
                  <div><span className="font-medium">Table:</span> {entityDetails.entity.table}</div>
                  <div><span className="font-medium">Description:</span> {entityDetails.entity.description || 'None'}</div>
                </div>
              </div>

              {/* Relationships */}
              {entityDetails.relationships && entityDetails.relationships.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-medium text-gray-900 mb-2">
                    Relationships ({entityDetails.relationships.length})
                  </h3>
                  <div className="space-y-2 max-h-40 overflow-y-auto">
                    {entityDetails.relationships.map((rel, index) => (
                      <div key={index} className="text-sm p-2 bg-gray-50 rounded">
                        <div className="font-medium">{rel.field}</div>
                        <div className="text-gray-600">Hash: {rel.hash}</div>
                        <div className="text-xs text-gray-500">{rel.path}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Connections */}
              {connections && (
                <div>
                  <h3 className="font-medium text-gray-900 mb-2 flex items-center gap-2">
                    <Link className="h-4 w-4" />
                    Connections
                  </h3>
                  
                  {connections.connections.references_from.length > 0 && (
                    <div className="mb-3">
                      <h4 className="text-sm font-medium text-gray-700 mb-2">
                        References ({connections.connections.references_from.length})
                      </h4>
                      <div className="space-y-1 max-h-32 overflow-y-auto">
                        {connections.connections.references_from.map((conn, index) => (
                          <button
                            key={index}
                            onClick={() => handleEntitySelect({
                              hash: conn.hash,
                              table: conn.table,
                              name: conn.name,
                              type: conn.table.includes('item') ? 'item' : 
                                   conn.table.includes('activity') ? 'activity' : 'entity'
                            })}
                            className="w-full text-left p-2 bg-blue-50 rounded text-sm hover:bg-blue-100"
                          >
                            <div className="font-medium">{conn.name}</div>
                            <div className="text-xs text-gray-600">{conn.relationship_context}</div>
                          </button>
                        ))}
                      </div>
                    </div>
                  )}

                  {connections.connections.references_to.length > 0 && (
                    <div>
                      <h4 className="text-sm font-medium text-gray-700 mb-2">
                        Referenced By ({connections.connections.references_to.length})
                      </h4>
                      <div className="space-y-1 max-h-32 overflow-y-auto">
                        {connections.connections.references_to.map((conn, index) => (
                          <button
                            key={index}
                            onClick={() => handleEntitySelect({
                              hash: conn.hash,
                              table: conn.table,
                              name: conn.name,
                              type: conn.table.includes('item') ? 'item' : 
                                   conn.table.includes('activity') ? 'activity' : 'entity'
                            })}
                            className="w-full text-left p-2 bg-orange-50 rounded text-sm hover:bg-orange-100"
                          >
                            <div className="font-medium">{conn.name}</div>
                            <div className="text-xs text-gray-600">{conn.relationship_context}</div>
                          </button>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ExplorationPage;