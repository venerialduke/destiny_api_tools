# Destiny API Tools - Project Architecture & Development Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Core Components](#core-components)
4. [Architecture Patterns](#architecture-patterns)
5. [Development Workflow](#development-workflow)
6. [Creating a New Tool](#creating-a-new-tool)
7. [API Reference](#api-reference)
8. [Deployment Guide](#deployment-guide)

## Project Overview

Destiny API Tools is a comprehensive web application for interacting with Bungie's Destiny 2 API. The application provides various tools for managing characters, searching items, analyzing data, and more. It follows a modern full-stack architecture with enterprise-grade patterns for scalability, maintainability, and performance.

### Technology Stack

**Backend:**
- **Framework**: Flask (Python)
- **API**: RESTful APIs with standardized responses
- **Database**: SQLite (manifest data), in-memory caching
- **Real-time**: WebSocket support for live updates
- **Background Jobs**: Scheduled task processing
- **Monitoring**: Health checks, performance metrics

**Frontend:**
- **Framework**: React 18+ with modern hooks
- **State Management**: React Context + Local State
- **Styling**: Tailwind CSS with component-based design
- **Build Tool**: Create React App / Vite
- **HTTP Client**: Axios with interceptors

**Infrastructure:**
- **Caching**: Multi-tier caching (memory, Redis-ready)
- **Search**: Full-text search with indexing
- **Logging**: Structured JSON logging
- **Testing**: Pytest (backend), Jest (frontend)

## Project Structure

```
destiny_api_tools/
├── backend/                     # Flask backend application
│   ├── app/                     # Main application package
│   │   ├── __init__.py         # App factory and initialization
│   │   ├── api/                # API endpoints and blueprints
│   │   │   ├── auth/           # Authentication endpoints
│   │   │   └── core/           # Core API functionality
│   │   │       ├── health.py   # Health check endpoints
│   │   │       ├── search.py   # Search API endpoints
│   │   │       ├── user.py     # User management
│   │   │       └── performance.py # Performance monitoring
│   │   ├── services/           # Business logic services
│   │   │   ├── bungie_api.py   # Bungie API integration
│   │   │   ├── auth_service.py # OAuth authentication
│   │   │   ├── user_service.py # User data management
│   │   │   ├── search_service.py # Advanced search functionality
│   │   │   ├── cache_service.py # Caching layer
│   │   │   ├── websocket_manager.py # Real-time updates
│   │   │   ├── data_pipeline.py # Background processing
│   │   │   ├── job_scheduler.py # Scheduled tasks
│   │   │   ├── health_monitor.py # Application monitoring
│   │   │   └── performance_monitor.py # Performance tracking
│   │   ├── utils/              # Utility modules
│   │   │   ├── response.py     # Standardized API responses
│   │   │   ├── validation.py   # Request validation
│   │   │   └── logging_config.py # Logging configuration
│   │   └── config.py           # Application configuration
│   ├── tests/                  # Test suite
│   │   ├── test_health_monitoring.py
│   │   └── test_search_service.py
│   └── requirements.txt        # Python dependencies
├── frontend/                   # React frontend application
│   ├── public/                 # Static assets
│   ├── src/                    # Source code
│   │   ├── components/         # Reusable components
│   │   │   ├── shared/         # Common UI components
│   │   │   │   ├── AdvancedSearch.js # Search interface
│   │   │   │   ├── CharacterCard.js  # Character display
│   │   │   │   └── CharacterList.js  # Character grid
│   │   │   ├── layout/         # Layout components
│   │   │   └── demo/           # Demo/example components
│   │   ├── pages/              # Page components
│   │   │   ├── auth/           # Authentication pages
│   │   │   ├── demo/           # Demo pages
│   │   │   └── HomePage.js     # Main landing page
│   │   ├── services/           # API integration
│   │   │   ├── base/           # Base service classes
│   │   │   │   ├── BaseService.js # Common service patterns
│   │   │   │   └── index.js    # Service exports
│   │   │   ├── apiClient.js    # HTTP client configuration
│   │   │   ├── authService.js  # Authentication service
│   │   │   └── userService.js  # User data service
│   │   ├── utils/              # Utility functions
│   │   │   └── performanceMonitor.js # Client-side monitoring
│   │   ├── contexts/           # React contexts
│   │   │   └── AuthContext.js  # Authentication state
│   │   ├── config/             # Configuration
│   │   │   └── appConfig.js    # Application settings
│   │   └── App.js              # Main application component
│   └── package.json            # Node.js dependencies
├── references/                 # API documentation and references
│   ├── api-summary/            # Bungie API guides
│   ├── endpoint-details/       # Detailed endpoint docs
│   └── entity-details/         # Data structure documentation
├── CLAUDE.md                   # Development instructions
├── PROJECT_ARCHITECTURE.md    # This documentation
└── README.md                   # Project overview
```

## Core Components

### Backend Services

#### 1. **API Layer** (`app/api/`)
- **Purpose**: Handles HTTP requests and responses
- **Structure**: Blueprint-based organization
- **Responsibilities**:
  - Request validation and parsing
  - Response formatting (using `utils/response.py`)
  - Authentication and authorization
  - Error handling and logging

#### 2. **Service Layer** (`app/services/`)
- **Purpose**: Contains business logic and external integrations
- **Key Services**:
  - `bungie_api.py`: Interface to Bungie's Destiny 2 API
  - `auth_service.py`: OAuth flow and token management
  - `search_service.py`: Advanced search and indexing
  - `cache_service.py`: Multi-tier caching system
  - `websocket_manager.py`: Real-time data synchronization
  - `data_pipeline.py`: Background job processing

#### 3. **Utilities** (`app/utils/`)
- **Purpose**: Common functionality used across the application
- **Components**:
  - `response.py`: Standardized API response formats
  - `validation.py`: Request validation helpers
  - `logging_config.py`: Structured logging setup

### Frontend Architecture

#### 1. **Component Hierarchy**
```
App.js
├── Layout Components (Header, Footer, Navigation)
├── Page Components (Routes)
│   ├── HomePage
│   ├── Auth Pages (Login, Callback)
│   └── Tool Pages (Character Manager, Search, etc.)
└── Shared Components (Reusable UI elements)
```

#### 2. **Service Layer** (`src/services/`)
- **BaseService**: Common patterns for API communication
- **Specialized Services**: Domain-specific API interactions
- **HTTP Client**: Configured Axios instance with interceptors

#### 3. **State Management**
- **React Context**: Global state (authentication, user data)
- **Local State**: Component-specific state with hooks
- **Performance Monitoring**: Client-side metrics collection

## Architecture Patterns

### 1. **Service-Oriented Architecture (SOA)**
- **Backend**: Services are independent and focused on specific domains
- **Frontend**: Service layer abstracts API communication
- **Benefits**: Modularity, testability, maintainability

### 2. **Standardized Response Format**
All API responses follow a consistent structure:
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully",
  "meta": {
    "timestamp": "2025-01-20T10:30:00Z",
    "request_id": "abc123"
  }
}
```

### 3. **Error Handling Strategy**
- **Centralized Error Processing**: All errors go through standardized handlers
- **Error Classification**: Different error types (validation, authentication, server)
- **Client-Friendly Messages**: User-readable error descriptions

### 4. **Caching Strategy**
- **Multi-Tier Caching**: Memory → Redis → Database
- **TTL-Based Expiration**: Automatic cache invalidation
- **Tag-Based Invalidation**: Group-based cache clearing

### 5. **Real-Time Updates**
- **WebSocket Manager**: Handles connections and subscriptions
- **Data Synchronization**: Automatic updates for character/inventory changes
- **Event-Driven Architecture**: Publish/subscribe pattern

## Development Workflow

### Setting Up Development Environment

1. **Backend Setup**:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. **Frontend Setup**:
```bash
cd frontend
npm install
npm start
```

3. **Environment Configuration**:
```bash
# Backend (.env)
BUNGIE_API_KEY=your_api_key
BUNGIE_CLIENT_ID=your_client_id
BUNGIE_CLIENT_SECRET=your_client_secret
FLASK_ENV=development

# Frontend (.env)
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_BUNGIE_CLIENT_ID=your_client_id
```

### Development Standards

#### 1. **Code Organization**
- **Single Responsibility**: Each module has one clear purpose
- **Dependency Injection**: Services receive dependencies rather than creating them
- **Interface Segregation**: Clean APIs between layers

#### 2. **Error Handling**
- **Always use try/catch blocks** in service methods
- **Log errors appropriately** with context information
- **Return meaningful error messages** to clients

#### 3. **Testing Requirements**
- **Unit Tests**: All service methods must have tests
- **Integration Tests**: API endpoints must be tested
- **Frontend Tests**: Components and services need test coverage

#### 4. **Documentation**
- **Docstrings**: All functions and classes must be documented
- **API Documentation**: Endpoints documented with examples
- **README Updates**: Keep documentation current

## Creating a New Tool

Follow these steps to add a new tool to the Destiny API Tools application:

### Step 1: Plan Your Tool

**Define Requirements**:
- What data does it need from the Bungie API?
- What user interactions are required?
- Does it need real-time updates?
- What caching strategy is appropriate?

**Example**: Creating a "Loadout Manager" tool
- **Data Needed**: Character equipment, inventory items
- **User Interactions**: Drag/drop items, save loadouts
- **Real-time**: Yes (equipment changes)
- **Caching**: Character data, item definitions

### Step 2: Backend Implementation

#### 2.1 Create the Service Layer

**File**: `backend/app/services/loadout_service.py`
```python
"""
Loadout management service for saving and managing character equipment sets.
"""

import logging
from typing import Dict, List, Any, Optional
from .bungie_api import BungieAPIService
from .cache_service import get_cache
from .user_service import UserService
from ..utils.response import APIResponse

logger = logging.getLogger(__name__)

class LoadoutService:
    """Service for managing character loadouts."""
    
    def __init__(self, access_token: str):
        self.bungie_api = BungieAPIService(access_token)
        self.cache = get_cache()
        self.user_service = UserService(access_token)
    
    def get_character_equipment(self, membership_type: int, 
                              character_id: str) -> Dict[str, Any]:
        """Get current equipment for a character."""
        try:
            # Check cache first
            cache_key = f"equipment:{membership_type}:{character_id}"
            cached_equipment = self.cache.get(cache_key)
            if cached_equipment:
                return cached_equipment
            
            # Fetch from Bungie API
            equipment = self.bungie_api.get_character_equipment(
                membership_type, character_id
            )
            
            # Cache for 5 minutes
            self.cache.set(cache_key, equipment, ttl=300)
            
            return equipment
            
        except Exception as e:
            logger.error(f"Failed to get character equipment: {e}")
            raise
    
    def save_loadout(self, loadout_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a character loadout."""
        try:
            # Validate loadout data
            required_fields = ['name', 'character_id', 'equipment']
            for field in required_fields:
                if field not in loadout_data:
                    raise ValueError(f"Missing required field: {field}")
            
            # Process and save loadout
            # Implementation would store in database/cache
            
            return {
                'loadout_id': 'generated_id',
                'status': 'saved',
                'message': 'Loadout saved successfully'
            }
            
        except Exception as e:
            logger.error(f"Failed to save loadout: {e}")
            raise
```

#### 2.2 Create API Endpoints

**File**: `backend/app/api/core/loadouts.py`
```python
"""
Loadout management API endpoints.
"""

from flask import Blueprint, request
from ...services.loadout_service import LoadoutService
from ...utils.response import APIResponse
from ...utils.validation import validate_request

loadouts_bp = Blueprint('loadouts', __name__)

@loadouts_bp.route('/loadouts/<membership_type>/<character_id>/equipment', methods=['GET'])
def get_character_equipment(membership_type: int, character_id: str):
    """Get current equipment for a character."""
    try:
        # Get access token from request headers
        access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not access_token:
            return APIResponse.error(
                message="Authentication required",
                code="MISSING_TOKEN"
            ), 401
        
        loadout_service = LoadoutService(access_token)
        equipment = loadout_service.get_character_equipment(
            int(membership_type), character_id
        )
        
        return APIResponse.success(
            data=equipment,
            message="Equipment retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve equipment",
            code="EQUIPMENT_ERROR",
            details={"error": str(e)}
        ), 500

@loadouts_bp.route('/loadouts', methods=['POST'])
def save_loadout():
    """Save a character loadout."""
    try:
        # Validate request
        data = request.get_json() or {}
        validation_rules = {
            'name': {'type': str, 'required': True, 'min_length': 1},
            'character_id': {'type': str, 'required': True},
            'equipment': {'type': dict, 'required': True}
        }
        
        validated_data = validate_request(data, validation_rules)
        
        # Get access token
        access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not access_token:
            return APIResponse.error(
                message="Authentication required",
                code="MISSING_TOKEN"
            ), 401
        
        loadout_service = LoadoutService(access_token)
        result = loadout_service.save_loadout(validated_data)
        
        return APIResponse.success(
            data=result,
            message="Loadout saved successfully"
        )
        
    except ValueError as e:
        return APIResponse.error(
            message=f"Invalid loadout data: {str(e)}",
            code="INVALID_LOADOUT_DATA"
        ), 400
    except Exception as e:
        return APIResponse.error(
            message="Failed to save loadout",
            code="SAVE_LOADOUT_ERROR",
            details={"error": str(e)}
        ), 500
```

#### 2.3 Register the Blueprint

**File**: `backend/app/api/core/__init__.py`
```python
# Add import
from .loadouts import loadouts_bp

# Register blueprint
core_bp.register_blueprint(loadouts_bp, url_prefix='/loadouts')
```

### Step 3: Frontend Implementation

#### 3.1 Create the Service

**File**: `frontend/src/services/loadoutService.js`
```javascript
/**
 * Loadout management service for the frontend.
 */

import BaseService from './base/BaseService';
import apiClient from './apiClient';

class LoadoutService extends BaseService {
  constructor() {
    super(apiClient);
  }

  /**
   * Get character equipment.
   */
  async getCharacterEquipment(membershipType, characterId) {
    const operation = () => 
      this.apiClient.get(`/core/loadouts/${membershipType}/${characterId}/equipment`);
    
    return this.withErrorHandling(operation, {
      cacheKey: `equipment:${membershipType}:${characterId}`,
      cacheTTL: 5 * 60 * 1000, // 5 minutes
    });
  }

  /**
   * Save a character loadout.
   */
  async saveLoadout(loadoutData) {
    const operation = () => 
      this.apiClient.post('/core/loadouts', loadoutData);
    
    return this.withErrorHandling(operation, {
      retry: 1, // Limited retries for POST operations
    });
  }

  /**
   * Get saved loadouts for a character.
   */
  async getCharacterLoadouts(characterId) {
    const operation = () => 
      this.apiClient.get(`/core/loadouts/character/${characterId}`);
    
    return this.withErrorHandling(operation, {
      cacheKey: `loadouts:${characterId}`,
      cacheTTL: 10 * 60 * 1000, // 10 minutes
    });
  }
}

export default new LoadoutService();
```

#### 3.2 Create the Component

**File**: `frontend/src/components/tools/LoadoutManager.js`
```javascript
/**
 * Loadout Manager Component
 * Allows users to manage character equipment loadouts.
 */

import React, { useState, useEffect } from 'react';
import { Save, Download, Trash2, Edit } from 'lucide-react';
import loadoutService from '../../services/loadoutService';
import performanceMonitor from '../../utils/performanceMonitor';

const LoadoutManager = ({ character }) => {
  const [equipment, setEquipment] = useState(null);
  const [loadouts, setLoadouts] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [editingLoadout, setEditingLoadout] = useState(null);

  // Load character equipment and saved loadouts
  useEffect(() => {
    if (character) {
      loadCharacterData();
    }
  }, [character]);

  const loadCharacterData = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const [equipmentData, loadoutsData] = await Promise.all([
        loadoutService.getCharacterEquipment(
          character.membershipType, 
          character.characterId
        ),
        loadoutService.getCharacterLoadouts(character.characterId)
      ]);

      setEquipment(equipmentData.data);
      setLoadouts(loadoutsData.data || []);

    } catch (err) {
      setError(err.message);
      performanceMonitor.recordError(err, { 
        context: 'LoadoutManager',
        characterId: character.characterId 
      });

    } finally {
      setIsLoading(false);
    }
  };

  const handleSaveLoadout = async (loadoutName) => {
    if (!equipment || !loadoutName.trim()) return;

    try {
      setIsLoading(true);

      const loadoutData = {
        name: loadoutName,
        character_id: character.characterId,
        equipment: equipment,
        created_at: new Date().toISOString()
      };

      const result = await loadoutService.saveLoadout(loadoutData);
      
      // Refresh loadouts list
      await loadCharacterData();

      // Show success message
      console.log('Loadout saved successfully:', result.data);

    } catch (err) {
      setError(err.message);
      performanceMonitor.recordError(err, { 
        context: 'LoadoutManager.saveLoadout' 
      });

    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center p-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
        <span className="ml-2 text-gray-400">Loading loadouts...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-900 border border-red-700 rounded-lg p-4">
        <div className="flex items-center">
          <Trash2 className="h-5 w-5 text-red-400 mr-2" />
          <span className="text-red-200">Error: {error}</span>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Current Equipment */}
      <div className="bg-gray-800 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-white mb-4">
          Current Equipment
        </h3>
        
        {equipment && (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {Object.entries(equipment).map(([slot, item]) => (
              <EquipmentSlot 
                key={slot} 
                slot={slot} 
                item={item} 
              />
            ))}
          </div>
        )}

        <div className="mt-4">
          <SaveLoadoutForm onSave={handleSaveLoadout} />
        </div>
      </div>

      {/* Saved Loadouts */}
      <div className="bg-gray-800 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-white mb-4">
          Saved Loadouts ({loadouts.length})
        </h3>

        {loadouts.length === 0 ? (
          <p className="text-gray-400">No saved loadouts yet.</p>
        ) : (
          <div className="grid gap-3">
            {loadouts.map((loadout) => (
              <LoadoutCard 
                key={loadout.id} 
                loadout={loadout}
                onEdit={setEditingLoadout}
                onDelete={() => {/* Implementation */}}
                onApply={() => {/* Implementation */}}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

// Sub-components
const EquipmentSlot = ({ slot, item }) => {
  return (
    <div className="bg-gray-700 rounded-lg p-3 text-center">
      <div className="text-xs text-gray-400 mb-1 capitalize">
        {slot.replace(/([A-Z])/g, ' $1').trim()}
      </div>
      {item && item.displayProperties ? (
        <>
          <img 
            src={`https://bungie.net${item.displayProperties.icon}`}
            alt={item.displayProperties.name}
            className="w-12 h-12 mx-auto mb-2"
          />
          <div className="text-sm text-white truncate">
            {item.displayProperties.name}
          </div>
        </>
      ) : (
        <div className="w-12 h-12 mx-auto mb-2 bg-gray-600 rounded"></div>
      )}
    </div>
  );
};

const SaveLoadoutForm = ({ onSave }) => {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name.trim()) {
      onSave(name.trim());
      setName('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Loadout name..."
        className="flex-1 px-3 py-2 bg-gray-700 border border-gray-600 rounded text-white placeholder-gray-400"
      />
      <button
        type="submit"
        disabled={!name.trim()}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50 flex items-center"
      >
        <Save className="h-4 w-4 mr-1" />
        Save
      </button>
    </form>
  );
};

const LoadoutCard = ({ loadout, onEdit, onDelete, onApply }) => {
  return (
    <div className="bg-gray-700 rounded-lg p-4 flex items-center justify-between">
      <div>
        <h4 className="text-white font-medium">{loadout.name}</h4>
        <p className="text-gray-400 text-sm">
          Created {new Date(loadout.created_at).toLocaleDateString()}
        </p>
      </div>
      
      <div className="flex gap-2">
        <button
          onClick={() => onApply(loadout)}
          className="p-2 text-green-400 hover:bg-gray-600 rounded"
          title="Apply Loadout"
        >
          <Download className="h-4 w-4" />
        </button>
        <button
          onClick={() => onEdit(loadout)}
          className="p-2 text-blue-400 hover:bg-gray-600 rounded"
          title="Edit Loadout"
        >
          <Edit className="h-4 w-4" />
        </button>
        <button
          onClick={() => onDelete(loadout.id)}
          className="p-2 text-red-400 hover:bg-gray-600 rounded"
          title="Delete Loadout"
        >
          <Trash2 className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
};

export default LoadoutManager;
```

#### 3.3 Create the Page Component

**File**: `frontend/src/pages/tools/LoadoutManagerPage.js`
```javascript
/**
 * Loadout Manager Page
 */

import React, { useState, useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import LoadoutManager from '../../components/tools/LoadoutManager';
import CharacterSelector from '../../components/shared/CharacterSelector';

const LoadoutManagerPage = () => {
  const { user, isAuthenticated } = useAuth();
  const [selectedCharacter, setSelectedCharacter] = useState(null);

  useEffect(() => {
    if (user?.characters?.length > 0 && !selectedCharacter) {
      setSelectedCharacter(user.characters[0]);
    }
  }, [user, selectedCharacter]);

  if (!isAuthenticated) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-white mb-4">
            Loadout Manager
          </h1>
          <p className="text-gray-400">
            Please log in to manage your character loadouts.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-white mb-2">
          Loadout Manager
        </h1>
        <p className="text-gray-400">
          Save and manage your character equipment configurations.
        </p>
      </div>

      {user?.characters && (
        <div className="mb-6">
          <CharacterSelector
            characters={user.characters}
            selectedCharacter={selectedCharacter}
            onCharacterSelect={setSelectedCharacter}
          />
        </div>
      )}

      {selectedCharacter && (
        <LoadoutManager character={selectedCharacter} />
      )}
    </div>
  );
};

export default LoadoutManagerPage;
```

#### 3.4 Add Route

**File**: `frontend/src/App.js`
```javascript
// Add import
import LoadoutManagerPage from './pages/tools/LoadoutManagerPage';

// Add route
<Route path="/tools/loadouts" element={<LoadoutManagerPage />} />
```

### Step 4: Testing

#### 4.1 Backend Tests

**File**: `backend/tests/test_loadout_service.py`
```python
"""
Test suite for loadout management functionality.
"""

import pytest
from unittest.mock import Mock, patch
from app.services.loadout_service import LoadoutService


class TestLoadoutService:
    """Test loadout service functionality."""
    
    def setup_method(self):
        """Setup test environment."""
        self.access_token = "test_token"
        self.loadout_service = LoadoutService(self.access_token)
    
    @patch('app.services.loadout_service.BungieAPIService')
    @patch('app.services.loadout_service.get_cache')
    def test_get_character_equipment(self, mock_get_cache, mock_bungie_api):
        """Test getting character equipment."""
        # Mock cache miss
        mock_cache = Mock()
        mock_cache.get.return_value = None
        mock_get_cache.return_value = mock_cache
        
        # Mock Bungie API response
        mock_api = Mock()
        mock_equipment = {"helmet": {"name": "Test Helmet"}}
        mock_api.get_character_equipment.return_value = mock_equipment
        mock_bungie_api.return_value = mock_api
        
        result = self.loadout_service.get_character_equipment(1, "char123")
        
        assert result == mock_equipment
        mock_cache.set.assert_called_once()
    
    def test_save_loadout_validation(self):
        """Test loadout validation."""
        # Missing required fields
        invalid_loadout = {"name": "Test"}
        
        with pytest.raises(ValueError):
            self.loadout_service.save_loadout(invalid_loadout)
    
    def test_save_loadout_success(self):
        """Test successful loadout save."""
        valid_loadout = {
            "name": "Test Loadout",
            "character_id": "char123",
            "equipment": {"helmet": {"name": "Test Helmet"}}
        }
        
        result = self.loadout_service.save_loadout(valid_loadout)
        
        assert result["status"] == "saved"
        assert "loadout_id" in result
```

#### 4.2 Frontend Tests

**File**: `frontend/src/components/tools/__tests__/LoadoutManager.test.js`
```javascript
/**
 * Tests for LoadoutManager component.
 */

import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import LoadoutManager from '../LoadoutManager';
import loadoutService from '../../../services/loadoutService';

// Mock the loadout service
jest.mock('../../../services/loadoutService');

describe('LoadoutManager', () => {
  const mockCharacter = {
    characterId: 'char123',
    membershipType: 1,
    displayProperties: { name: 'Hunter' }
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders loading state initially', () => {
    render(<LoadoutManager character={mockCharacter} />);
    
    expect(screen.getByText('Loading loadouts...')).toBeInTheDocument();
  });

  test('displays character equipment when loaded', async () => {
    const mockEquipment = {
      helmet: { displayProperties: { name: 'Test Helmet', icon: '/icon.jpg' } }
    };
    
    loadoutService.getCharacterEquipment.mockResolvedValue({
      data: mockEquipment
    });
    loadoutService.getCharacterLoadouts.mockResolvedValue({
      data: []
    });

    render(<LoadoutManager character={mockCharacter} />);

    await waitFor(() => {
      expect(screen.getByText('Test Helmet')).toBeInTheDocument();
    });
  });

  test('handles save loadout', async () => {
    const user = userEvent.setup();
    
    loadoutService.getCharacterEquipment.mockResolvedValue({
      data: { helmet: { name: 'Test Helmet' } }
    });
    loadoutService.getCharacterLoadouts.mockResolvedValue({
      data: []
    });
    loadoutService.saveLoadout.mockResolvedValue({
      data: { loadout_id: 'loadout123' }
    });

    render(<LoadoutManager character={mockCharacter} />);

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Loadout name...')).toBeInTheDocument();
    });

    const nameInput = screen.getByPlaceholderText('Loadout name...');
    const saveButton = screen.getByText('Save');

    await user.type(nameInput, 'My Test Loadout');
    await user.click(saveButton);

    await waitFor(() => {
      expect(loadoutService.saveLoadout).toHaveBeenCalledWith(
        expect.objectContaining({
          name: 'My Test Loadout',
          character_id: 'char123'
        })
      );
    });
  });
});
```

### Step 5: Documentation and Integration

#### 5.1 Update Navigation

**File**: `frontend/src/components/layout/Header.js`
```javascript
// Add navigation link
<Link to="/tools/loadouts" className="nav-link">
  Loadout Manager
</Link>
```

#### 5.2 Add to Homepage

**File**: `frontend/src/pages/HomePage.js`
```javascript
// Add tool card
<ToolCard
  title="Loadout Manager"
  description="Save and manage character equipment configurations"
  icon="⚔️"
  link="/tools/loadouts"
  features={[
    "Save current equipment as loadouts",
    "Quick-switch between configurations",
    "Organize builds by activity type"
  ]}
/>
```

#### 5.3 Update Documentation

**File**: `README.md`
```markdown
## Tools Available

### Loadout Manager
- Save character equipment configurations
- Quick-switch between different builds
- Organize loadouts by activity type
- Real-time equipment synchronization
```

## API Reference

### Authentication
All API endpoints require authentication via Bearer token in the Authorization header:
```
Authorization: Bearer <access_token>
```

### Response Format
All API responses follow this structure:
```json
{
  "success": boolean,
  "data": object | array | null,
  "message": string,
  "meta": {
    "timestamp": "ISO 8601 timestamp",
    "request_id": "unique identifier"
  }
}
```

### Core Endpoints

#### Health & Monitoring
- `GET /api/core/health/health` - Basic health check
- `GET /api/core/health/detailed` - Detailed health status
- `GET /api/core/health/performance` - Performance metrics

#### Search
- `POST /api/core/search/search` - Advanced search
- `GET /api/core/search/suggest` - Search suggestions
- `GET /api/core/search/quick-search` - Quick text search

#### User Management
- `GET /api/core/user/profile` - User profile and characters
- `POST /api/auth/callback` - OAuth callback handling

### Error Codes
- `MISSING_TOKEN` - Authentication token required
- `INVALID_TOKEN` - Token is invalid or expired
- `VALIDATION_ERROR` - Request validation failed
- `NOT_FOUND` - Requested resource not found
- `SERVER_ERROR` - Internal server error

## Deployment Guide

### Production Checklist

1. **Environment Variables**:
   - Set `FLASK_ENV=production`
   - Configure database connections
   - Set secure secret keys

2. **Security**:
   - Enable HTTPS
   - Configure CORS properly
   - Set secure cookie flags

3. **Performance**:
   - Enable caching layers
   - Configure CDN for static assets
   - Set up database connection pooling

4. **Monitoring**:
   - Configure logging levels
   - Set up health check endpoints
   - Enable performance monitoring

5. **Scaling**:
   - Configure load balancing
   - Set up background job workers
   - Enable horizontal scaling

### Docker Deployment

**File**: `docker-compose.yml`
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://...
    ports:
      - "5000:5000"
  
  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - backend
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

This comprehensive documentation provides everything needed to understand the project structure and create new tools following established patterns and best practices.