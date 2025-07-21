import { apiClient } from './apiClient';

class ExplorationService {
  constructor() {
    this.baseURL = '/manifest/explore';
  }

  /**
   * Get manifest database structure overview
   */
  async getManifestStructure() {
    try {
      const response = await apiClient.get('/manifest/structure');
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to get manifest structure');
    }
  }

  /**
   * Universal search across all manifest tables
   * @param {string} query - Search query
   * @param {Object} options - Search options
   * @param {string} options.table - Limit search to specific table
   * @param {number} options.limit - Maximum results
   */
  async universalSearch(query, options = {}) {
    try {
      const params = new URLSearchParams({ q: query });
      
      if (options.table) {
        params.append('table', options.table);
      }
      
      if (options.limit) {
        params.append('limit', options.limit);
      }

      const response = await apiClient.get(`${this.baseURL}/search?${params}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Search failed');
    }
  }

  /**
   * Get detailed entity information with relationships
   * @param {string} table - Entity table name
   * @param {number} hash - Entity hash
   */
  async getEntityDetails(table, hash) {
    try {
      const response = await apiClient.get(`${this.baseURL}/entity/${table}/${hash}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to get entity details');
    }
  }

  /**
   * Find all connections to/from an entity
   * @param {string} table - Entity table name  
   * @param {number} hash - Entity hash
   * @param {number} limit - Maximum connections to return
   */
  async findConnections(table, hash, limit = 50) {
    try {
      const response = await apiClient.get(`${this.baseURL}/connections/${table}/${hash}?limit=${limit}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to find connections');
    }
  }

  /**
   * Build exploration path by following relationships
   * @param {Array} entities - Array of {table, hash} objects to explore
   */
  async buildExplorationPath(entities) {
    try {
      const explorationPath = [];
      
      for (const entity of entities) {
        const [details, connections] = await Promise.all([
          this.getEntityDetails(entity.table, entity.hash),
          this.findConnections(entity.table, entity.hash)
        ]);
        
        explorationPath.push({
          entity: details.entity,
          relationships: details.relationships,
          connections: connections.connections,
          raw_data: details.raw_data
        });
      }
      
      return {
        path: explorationPath,
        summary: {
          entities_explored: entities.length,
          total_relationships: explorationPath.reduce((sum, item) => sum + item.relationships.length, 0),
          total_connections: explorationPath.reduce((sum, item) => 
            sum + item.connections.references_to.length + item.connections.references_from.length, 0
          )
        }
      };
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to build exploration path');
    }
  }

  /**
   * Search for armor set bonuses specifically
   * @param {string} query - Search query (optional)
   */
  async searchArmorSets(query = '') {
    try {
      // Search for items with "set" in name or description
      const searchTerm = query ? `${query} set` : 'set';
      const results = await this.universalSearch(searchTerm, { 
        table: 'destiny_inventory_item_definition',
        limit: 100 
      });
      
      // Filter for armor items and look for set-related content
      const armorSets = [];
      
      if (results.results.destiny_inventory_item_definition) {
        for (const item of results.results.destiny_inventory_item_definition.results) {
          // Get detailed info to check for set relationships
          try {
            const details = await this.getEntityDetails(item.table, item.hash);
            
            // Look for setHash or set-related fields in raw data
            const hasSetData = details.relationships.some(rel => 
              rel.field.toLowerCase().includes('set') || 
              rel.path.toLowerCase().includes('set')
            );
            
            if (hasSetData) {
              armorSets.push({
                ...item,
                setRelationships: details.relationships.filter(rel => 
                  rel.field.toLowerCase().includes('set')
                )
              });
            }
          } catch (error) {
            // Skip items that can't be analyzed
            continue;
          }
        }
      }
      
      return {
        query: searchTerm,
        total_found: armorSets.length,
        armor_sets: armorSets
      };
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to search armor sets');
    }
  }

  /**
   * Analyze relationship patterns across the manifest
   */
  async analyzeRelationshipPatterns() {
    try {
      const structure = await this.getManifestStructure();
      
      // Sample entities from each table to understand relationship patterns
      const patterns = {
        common_hash_fields: [],
        table_connections: {},
        relationship_frequency: {}
      };
      
      // This would require sampling data from each table
      // For now, return the structure info with relationship hints
      return {
        patterns,
        structure: structure.relationship_info,
        tables: Object.keys(structure.tables).filter(table => 
          structure.tables[table].has_relationships
        )
      };
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to analyze relationship patterns');
    }
  }
}

export const explorationService = new ExplorationService();