# Enhanced Manifest System

## Overview

The Enhanced Manifest System downloads and processes **ALL** Destiny 2 definition tables from Bungie's manifest, not just the 6 tables we previously had. It creates two databases:

1. **Complete Database** - All definition tables in normalized format
2. **Flattened Database** - Single table with all JSON flattened using `json_row_structure.py` functions

## What This Solves

### Previous System Limitations:
- Only had 6 out of 20+ definition tables
- Missing triumphs (`DestinyRecordDefinition`)
- Missing stats (`DestinyStatDefinition`) 
- Missing sockets (`DestinySocketCategoryDefinition`)
- Limited search to display text only

### Enhanced System Benefits:
- Downloads **ALL** available definition tables
- Stores complete raw JSON files
- Creates searchable flattened database
- Enables search across ALL manifest relationships
- Supports triumph exploration, stat analysis, socket compatibility

## File Structure

```
data/
├── manifest_complete.db      # All tables in normalized format
├── manifest_flattened.db     # Single flattened table for universal search
└── manifest_raw/            # Raw JSON files from Bungie
    ├── DestinyRecordDefinition.json         # Triumphs!
    ├── DestinyStatDefinition.json           # Stats!
    ├── DestinySocketCategoryDefinition.json # Socket compatibility!
    ├── DestinyInventoryItemDefinition.json  # Items
    └── ... (20+ more definition files)
```

## Database Schemas

### Complete Database Tables
Each definition type gets its own table:
```sql
CREATE TABLE DestinyRecordDefinition (
    hash INTEGER PRIMARY KEY,
    display_name TEXT,
    description TEXT,
    raw_json TEXT
);
-- Plus 20+ other definition tables
```

### Flattened Database
Single table for universal search:
```sql
CREATE TABLE manifest_flattened (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_table TEXT NOT NULL,           -- Which definition table
    entity_hash INTEGER NOT NULL,         -- Entity identifier
    entity_name TEXT,                     -- Display name if available
    key_path TEXT NOT NULL,               -- JSON path (e.g., "displayProperties.name")
    data_type TEXT NOT NULL,              -- String, Numeric, Boolean, dict, array
    boolean_value INTEGER,                -- Boolean values
    numeric_value REAL,                   -- Numeric values (including hashes)
    string_value TEXT,                    -- String values
    key_link TEXT,                        -- Full key path for relationships
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## API Endpoints

### Enhanced Manifest Management
- `POST /api/manifest/enhanced/update` - Download and process all tables
- `GET /api/manifest/enhanced/status` - System status and stats
- `GET /api/manifest/enhanced/tables` - List all available tables

### Enhanced Search
- `GET /api/manifest/enhanced/search/universal?q=<query>` - Search ALL manifest data
- `GET /api/manifest/enhanced/search/entity/<table>/<hash>` - Get flattened entity details
- `GET /api/manifest/enhanced/search/triumphs?q=<query>` - Search specifically for triumphs

### Search Parameters
- `q` - Search query (searches key paths and string values)
- `table` - Filter to specific definition table
- `type` - Filter by data type (String, Numeric, Boolean)
- `limit` - Maximum results (default 100, max 500)

## Usage Examples

### 1. Update Enhanced Manifest
```bash
curl -X POST https://localhost:5001/api/manifest/enhanced/update
```

### 2. Search for Triumphs
```bash
curl "https://localhost:5001/api/manifest/enhanced/search/triumphs?q=raid"
```

### 3. Universal Search for Armor Sets
```bash
curl "https://localhost:5001/api/manifest/enhanced/search/universal?q=set&table=DestinyInventoryItemDefinition"
```

### 4. Find All Socket-Related Data
```bash
curl "https://localhost:5001/api/manifest/enhanced/search/universal?q=socket"
```

### 5. Search for Specific Stats
```bash
curl "https://localhost:5001/api/manifest/enhanced/search/universal?q=mobility&table=DestinyStatDefinition"
```

## Implementation Details

### Download Process
1. Calls `/Destiny2/Manifest/` to get all available definition URLs
2. Downloads each JSON file (English only)
3. Stores raw JSON files in `manifest_raw/` directory

### Complete Database Creation
1. Creates normalized table for each definition type
2. Extracts `displayProperties.name` and `displayProperties.description`
3. Stores complete raw JSON for each entity

### Flattened Database Creation
1. Uses `json_row_structure.py` functions to flatten each JSON object
2. Creates key-value pairs with type inference
3. Enables search across ALL JSON fields and relationships
4. Maintains source table tracking for context

### Performance Optimizations
- Indexes on source_table, entity_hash, key_path, data_type
- Separate indexes for string_value and numeric_value
- Batched database operations during creation

## Testing

Run the test script to verify the system:
```bash
python test_enhanced_manifest.py
```

This will:
- Download all definition tables
- Create both databases
- Show statistics about what was found
- Verify triumph and system tables are available

## Benefits for Manifest Exploration

### Now Possible:
✅ **Triumph Search** - Find and explore all triumph records  
✅ **Stat Analysis** - Search mobility, resilience, intellect definitions  
✅ **Socket Compatibility** - Discover mod/socket relationships  
✅ **Perk Exploration** - Find weapon/armor perk definitions  
✅ **Quest Chain Mapping** - Trace quest progressions  
✅ **Lore Discovery** - Search lore entries  
✅ **Location Data** - Explore destination/place definitions  
✅ **Universal Relationships** - Follow ANY hash reference between entities  

### Enhanced Search Capabilities:
- Search across 20+ definition types simultaneously
- Find entities by ANY JSON field, not just name/description
- Discover relationships through hash references
- Filter by data type (find all numeric hashes, all boolean flags, etc.)
- Trace connections between different definition types

This transforms the manifest from a limited "item catalog" into a comprehensive, searchable database of ALL Destiny 2 game definitions and their relationships.