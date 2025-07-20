# Destiny Manifest Implementation Plan

## Overview

This plan outlines the implementation of a complete Destiny 2 manifest management system that downloads, stores, and provides fast access to all static game data. The system will use SQLite for local storage and provide REST API endpoints for efficient manifest lookups.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Destiny API Tools                       │
├─────────────────────────────────────────────────────────────┤
│  Frontend (React)                                          │
│  ├── Manifest Hook (useManifest)                          │
│  ├── Item Components (ItemCard, ItemTooltip)              │
│  └── Search Components (ItemSearch, FilterPanel)          │
├─────────────────────────────────────────────────────────────┤
│  Backend (Flask)                                           │
│  ├── Manifest API Endpoints                               │
│  ├── Manifest Service (Download/Update)                   │
│  ├── Database Service (SQLite Operations)                 │
│  └── Background Tasks (Scheduled Updates)                 │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                                │
│  ├── SQLite Database (manifest.db)                        │
│  ├── Version Tracking (metadata table)                    │
│  └── Cached JSON Files (backup/debugging)                 │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Phases

### Phase 1: Core Manifest Service
**Objective**: Download and parse manifest data
**Duration**: 2-3 hours

#### 1.1 Manifest Download Service
**File**: `backend/app/services/manifest_service.py`

**Key Components**:
- `ManifestDownloader` class
- Version checking and comparison
- Download progress tracking
- Error handling and retry logic

**Features**:
- Check current manifest version from Bungie API
- Download full manifest JSON (100MB+)
- Validate download integrity
- Handle network errors and timeouts

#### 1.2 Database Schema Design
**File**: `backend/app/models/manifest_models.py`

**Core Tables**:
```sql
-- Version tracking
CREATE TABLE manifest_metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Item definitions (weapons, armor, etc.)
CREATE TABLE destiny_inventory_item_definition (
    hash INTEGER PRIMARY KEY,
    display_name TEXT,
    description TEXT,
    icon TEXT,
    item_type INTEGER,
    item_sub_type INTEGER,
    tier_type INTEGER,
    class_type INTEGER,
    damage_type INTEGER,
    power_cap INTEGER,
    is_weapon BOOLEAN,
    is_armor BOOLEAN,
    raw_json TEXT,
    search_text TEXT -- For full-text search
);

-- Activity definitions
CREATE TABLE destiny_activity_definition (
    hash INTEGER PRIMARY KEY,
    display_name TEXT,
    description TEXT,
    activity_type_hash INTEGER,
    playlist_items TEXT, -- JSON array
    modifiers TEXT, -- JSON array
    raw_json TEXT
);

-- Vendor definitions
CREATE TABLE destiny_vendor_definition (
    hash INTEGER PRIMARY KEY,
    display_name TEXT,
    description TEXT,
    icon TEXT,
    vendor_banner TEXT,
    enabled BOOLEAN,
    raw_json TEXT
);

-- Additional core definition tables...
```

#### 1.3 Database Operations Service
**File**: `backend/app/services/database_service.py`

**Features**:
- SQLite connection management
- Bulk insert operations for performance
- Transaction handling
- Database schema migrations
- Query optimization

### Phase 2: Data Processing Pipeline
**Objective**: Transform manifest data into queryable format
**Duration**: 3-4 hours

#### 2.1 Data Parser and Transformer
**File**: `backend/app/services/manifest_parser.py`

**Processing Pipeline**:
1. **JSON Parsing**: Load manifest JSON files
2. **Data Extraction**: Extract relevant fields from complex nested structures
3. **Data Enrichment**: Add computed fields (search text, categorization)
4. **Relationship Mapping**: Link related definitions (perks to items, etc.)
5. **Database Population**: Bulk insert processed data

**Key Processing Logic**:
- Parse item definitions and extract displayProperties
- Categorize items (weapons, armor, consumables)
- Extract socket and perk information
- Build search-optimized text fields
- Handle localization data

#### 2.2 Database Population
**Features**:
- Atomic database updates (temp DB → swap)
- Progress tracking for large datasets
- Error recovery and rollback
- Performance optimization (batched inserts)

### Phase 3: REST API Endpoints
**Objective**: Provide fast manifest lookup APIs
**Duration**: 2-3 hours

#### 3.1 Manifest API Blueprint
**File**: `backend/app/api/manifest/__init__.py`

**Endpoints**:
```python
# Core lookup endpoints
GET /api/manifest/items/{hash}              # Single item lookup
GET /api/manifest/items/search              # Item search with filters
GET /api/manifest/activities/{hash}         # Activity lookup
GET /api/manifest/vendors/{hash}            # Vendor lookup

# Batch operations
POST /api/manifest/items/batch              # Multiple item lookup
POST /api/manifest/lookup                   # Multi-type lookup

# Search and filtering
GET /api/manifest/items/search              # Advanced item search
GET /api/manifest/weapons                   # Weapon-specific queries
GET /api/manifest/armor                     # Armor-specific queries

# Metadata
GET /api/manifest/status                    # Manifest version and status
GET /api/manifest/stats                     # Database statistics
```

#### 3.2 Search and Filter Implementation
**Features**:
- Full-text search across item names/descriptions
- Multi-criteria filtering (type, tier, class, damage)
- Fuzzy matching for typos
- Pagination for large result sets
- Caching for popular queries

#### 3.3 Response Optimization
**Features**:
- Minimal JSON responses (avoid raw_json unless requested)
- Response compression
- ETags for client-side caching
- Batch operations to reduce round trips

### Phase 4: Update Management System
**Objective**: Keep manifest data current automatically
**Duration**: 2-3 hours

#### 4.1 Version Checking Service
**File**: `backend/app/services/manifest_updater.py`

**Features**:
- Scheduled version checks (daily)
- Compare local vs remote manifest versions
- Trigger updates when new versions available
- Notification system for update status

#### 4.2 Background Update Tasks
**Implementation Options**:
- **Option A**: APScheduler for in-process scheduling
- **Option B**: Celery for distributed task processing
- **Option C**: Simple cron-style background thread

**Update Process**:
1. Check Bungie API for new manifest version
2. Download new manifest if version changed
3. Process data in temporary database
4. Validate data integrity
5. Atomically swap to new database
6. Clean up old files
7. Log update status and metrics

#### 4.3 Error Handling and Recovery
**Features**:
- Retry logic for failed downloads
- Fallback to previous version on corruption
- Health monitoring and alerts
- Graceful degradation during updates

## Database Design Details

### Core Tables Schema

#### manifest_metadata
```sql
CREATE TABLE manifest_metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example data:
-- ('version', '123.45.67.890')
-- ('last_updated', '2025-07-20T10:30:00Z')
-- ('download_url', 'https://bungie.net/...')
```

#### destiny_inventory_item_definition
```sql
CREATE TABLE destiny_inventory_item_definition (
    hash INTEGER PRIMARY KEY,
    display_name TEXT NOT NULL,
    description TEXT,
    icon TEXT,
    
    -- Item categorization
    item_type INTEGER,           -- DestinyItemType enum
    item_sub_type INTEGER,       -- DestinyItemSubType enum
    tier_type INTEGER,           -- TierType (common, rare, legendary, exotic)
    class_type INTEGER,          -- DestinyClass (titan, hunter, warlock, any)
    
    -- Weapon-specific
    damage_type INTEGER,         -- DamageType (kinetic, arc, solar, void, stasis)
    ammo_type INTEGER,          -- DestinyAmmunitionType
    
    -- Categorization flags
    is_weapon BOOLEAN DEFAULT FALSE,
    is_armor BOOLEAN DEFAULT FALSE,
    is_consumable BOOLEAN DEFAULT FALSE,
    is_mod BOOLEAN DEFAULT FALSE,
    
    -- Power and progression
    power_cap INTEGER,
    default_damage_type INTEGER,
    
    -- Search optimization
    search_text TEXT,           -- Concatenated searchable text
    
    -- Raw data for complete access
    raw_json TEXT,
    
    -- Indexes for common queries
    INDEX idx_item_type (item_type),
    INDEX idx_tier_type (tier_type),
    INDEX idx_class_type (class_type),
    INDEX idx_is_weapon (is_weapon),
    INDEX idx_is_armor (is_armor),
    INDEX idx_search_text (search_text)
);
```

### Performance Considerations

#### Indexing Strategy
```sql
-- Primary hash lookups (fastest)
CREATE INDEX idx_hash ON destiny_inventory_item_definition(hash);

-- Search and filtering
CREATE INDEX idx_search_composite ON destiny_inventory_item_definition(
    item_type, tier_type, class_type, is_weapon
);

-- Full-text search
CREATE VIRTUAL TABLE item_search_fts USING fts5(
    hash, display_name, description, search_text,
    content='destiny_inventory_item_definition'
);
```

#### Query Optimization
- Use prepared statements for common queries
- Implement connection pooling
- Cache frequent lookups in memory
- Use EXPLAIN QUERY PLAN for optimization

## API Design Examples

### Item Lookup API
```python
@manifest_bp.route('/items/<int:item_hash>', methods=['GET'])
def get_item(item_hash):
    """Get item definition by hash."""
    include_raw = request.args.get('raw', 'false').lower() == 'true'
    
    item = manifest_service.get_item(item_hash, include_raw=include_raw)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    return jsonify({
        'hash': item.hash,
        'displayProperties': {
            'name': item.display_name,
            'description': item.description,
            'icon': f"https://bungie.net{item.icon}"
        },
        'itemType': item.item_type,
        'tierType': item.tier_type,
        'classType': item.class_type,
        'isWeapon': item.is_weapon,
        'isArmor': item.is_armor,
        **({'rawJson': json.loads(item.raw_json)} if include_raw else {})
    })
```

### Search API
```python
@manifest_bp.route('/items/search', methods=['GET'])
def search_items():
    """Search items with filters."""
    query = request.args.get('q', '')
    item_type = request.args.get('type', type=int)
    tier_type = request.args.get('tier', type=int)
    class_type = request.args.get('class', type=int)
    is_weapon = request.args.get('weapon', 'false').lower() == 'true'
    limit = min(request.args.get('limit', 50, type=int), 100)
    offset = request.args.get('offset', 0, type=int)
    
    results = manifest_service.search_items(
        query=query,
        item_type=item_type,
        tier_type=tier_type,
        class_type=class_type,
        is_weapon=is_weapon,
        limit=limit,
        offset=offset
    )
    
    return jsonify({
        'items': [format_item_summary(item) for item in results.items],
        'total': results.total,
        'hasMore': results.has_more,
        'pagination': {
            'limit': limit,
            'offset': offset,
            'nextOffset': offset + limit if results.has_more else None
        }
    })
```

## Frontend Integration

### React Hook for Manifest Data
```javascript
// hooks/useManifest.js
export const useManifest = () => {
  const [manifestStatus, setManifestStatus] = useState(null);
  
  const getItem = useCallback(async (hash) => {
    const response = await apiClient.get(`/manifest/items/${hash}`);
    return response.data;
  }, []);
  
  const searchItems = useCallback(async (filters) => {
    const params = new URLSearchParams(filters);
    const response = await apiClient.get(`/manifest/items/search?${params}`);
    return response.data;
  }, []);
  
  return { getItem, searchItems, manifestStatus };
};
```

### Item Display Components
```javascript
// components/ItemCard.js
const ItemCard = ({ itemHash }) => {
  const { getItem } = useManifest();
  const [item, setItem] = useState(null);
  
  useEffect(() => {
    getItem(itemHash).then(setItem);
  }, [itemHash, getItem]);
  
  if (!item) return <div>Loading...</div>;
  
  return (
    <div className="item-card">
      <img src={item.displayProperties.icon} alt={item.displayProperties.name} />
      <h3>{item.displayProperties.name}</h3>
      <p>{item.displayProperties.description}</p>
    </div>
  );
};
```

## Implementation Timeline

### Week 1: Core Infrastructure
- **Day 1-2**: Manifest download service and database schema
- **Day 3-4**: Data processing pipeline and database population
- **Day 5**: Testing and optimization

### Week 2: API and Frontend
- **Day 1-2**: REST API endpoints and search functionality
- **Day 3-4**: Frontend hooks and components
- **Day 5**: Integration testing

### Week 3: Updates and Polish
- **Day 1-2**: Background update system
- **Day 3-4**: Performance optimization and caching
- **Day 5**: Documentation and deployment

## Success Metrics

### Performance Targets
- **Item lookup**: < 10ms average response time
- **Search queries**: < 100ms for typical searches
- **Database size**: < 200MB total storage
- **Update frequency**: Daily version checks, automatic updates

### Functionality Goals
- Support for all major definition types (items, activities, vendors)
- Full-text search across item names and descriptions
- Advanced filtering by type, tier, class, damage type
- Batch operations for efficient data loading
- Real-time manifest status monitoring

## Security and Reliability

### Data Integrity
- Checksums for downloaded files
- Database transaction rollbacks on corruption
- Backup and recovery procedures
- Health monitoring and alerting

### Performance Monitoring
- Query performance tracking
- Database size monitoring
- Update success/failure rates
- API response time metrics

## Future Enhancements

### Phase 2 Features
- Multi-language support (localization)
- Advanced relationship mapping (perks to items)
- Semantic search capabilities
- Real-time manifest streaming updates
- GraphQL API for complex queries

### Optimization Opportunities
- In-memory caching layer (Redis)
- Database sharding for massive scale
- CDN integration for icon assets
- Compressed response formats

---

This implementation plan provides a robust, scalable foundation for manifest management that will enable rich item browsing, advanced search capabilities, and fast user experiences across all Destiny API Tools features.