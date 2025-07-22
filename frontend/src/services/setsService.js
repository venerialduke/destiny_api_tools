/**
 * Service for interacting with Destiny 2 Equipable Sets API
 */

import { apiClient } from './apiClient';

class SetsService {
    /**
     * Get summary statistics about equipable sets
     */
    async getSummary() {
        try {
            const response = await apiClient.get('/sets/summary');
            return response;
        } catch (error) {
            console.error('Error fetching sets summary:', error);
            throw error;
        }
    }

    /**
     * Get all equipable sets with optional filtering
     * @param {Object} options - Query options
     * @param {number} options.classFilter - Filter by class type (0=Titan, 1=Hunter, 2=Warlock)
     * @param {boolean} options.includeItems - Include detailed armor pieces
     * @param {boolean} options.includePerks - Include detailed set perks
     */
    async getAllSets(options = {}) {
        try {
            const params = new URLSearchParams();
            
            if (options.classFilter !== undefined) {
                params.append('class', options.classFilter);
            }
            if (options.includeItems) {
                params.append('include_items', 'true');
            }
            if (options.includePerks) {
                params.append('include_perks', 'true');
            }

            const url = `/sets/${params.toString() ? '?' + params.toString() : ''}`;
            const response = await apiClient.get(url);
            return response;
        } catch (error) {
            console.error('Error fetching all sets:', error);
            throw error;
        }
    }

    /**
     * Get equipable sets for a specific class
     * @param {number} classType - Class type (0=Titan, 1=Hunter, 2=Warlock)
     * @param {Object} options - Query options
     * @param {boolean} options.includeItems - Include detailed armor pieces
     * @param {boolean} options.includePerks - Include detailed set perks
     */
    async getSetsByClass(classType, options = {}) {
        try {
            const params = new URLSearchParams();
            
            if (options.includeItems) {
                params.append('include_items', 'true');
            }
            if (options.includePerks) {
                params.append('include_perks', 'true');
            }

            const url = `/sets/by-class/${classType}${params.toString() ? '?' + params.toString() : ''}`;
            const response = await apiClient.get(url);
            return response;
        } catch (error) {
            console.error(`Error fetching sets for class ${classType}:`, error);
            throw error;
        }
    }

    /**
     * Get detailed information for a specific equipable set
     * @param {number} setHash - The hash of the set to retrieve
     */
    async getSetDetails(setHash) {
        try {
            const response = await apiClient.get(`/sets/${setHash}`);
            return response;
        } catch (error) {
            console.error(`Error fetching set details for ${setHash}:`, error);
            throw error;
        }
    }

    /**
     * Helper method to get class name from class type
     * @param {number} classType - Class type number
     * @returns {string} Class name
     */
    getClassName(classType) {
        const classNames = {
            0: 'Titan',
            1: 'Hunter', 
            2: 'Warlock',
            3: 'Unknown'
        };
        return classNames[classType] || 'Unknown';
    }

    /**
     * Helper method to get class color from class type
     * @param {number} classType - Class type number
     * @returns {string} CSS color value
     */
    getClassColor(classType) {
        const classColors = {
            0: '#f24c3d', // Titan - Red
            1: '#4a90e2', // Hunter - Blue
            2: '#f39c12', // Warlock - Orange
            3: '#95a5a6'  // Unknown - Gray
        };
        return classColors[classType] || '#95a5a6';
    }

    /**
     * Format armor sub-type for display
     * @param {string} subType - Armor sub-type
     * @returns {string} Formatted sub-type
     */
    formatArmorType(subType) {
        const typeMap = {
            'Helmet': 'Helm',
            'Gauntlets': 'Arms',
            'Chest Armor': 'Chest',
            'Leg Armor': 'Legs',
            'Class Armor': 'Class'
        };
        return typeMap[subType] || subType;
    }
}

export const setsService = new SetsService();