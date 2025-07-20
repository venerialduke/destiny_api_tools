# Destiny API Tools - Manifest System Guide

## Overview

The Destiny API Tools Manifest System provides comprehensive access to all Destiny 2 game definition data through a high-performance, automatically-updating local database. This system downloads, processes, and serves over 35,000 game definitions including weapons, armor, activities, vendors, and cosmetic items.

## 🚀 Quick Start

### Starting the Enhanced Server

```bash
# Navigate to backend directory
cd backend

# Install dependencies (including new psutil requirement)
pip install -r requirements.txt

# Start the enhanced server with automatic updates
python app_with_updater.py
```

The server will automatically:
- Initialize the manifest database (downloads ~100MB on first run)
- Start background updates (checks every 6 hours)
- Enable all monitoring and health checks
- Provide comprehensive API access

### Key URLs
- **Server**: `https://localhost:5001`
- **Health Check**: `https://localhost:5001/health`
- **Manifest Status**: `https://localhost:5001/api/manifest/status`
- **Update Dashboard**: `https://localhost:5001/api/updater/dashboard`
- **System Health**: `https://localhost:5001/api/updater/system-health`

## 📚 Manifest API Endpoints

### Core Item Access

#### Get Item by Hash
```http
GET /api/manifest/items/{hash}
```
**Example**: `/api/manifest/items/4094900227`
```json
{
  "hash": 4094900227,
  "displayProperties": {
    "name": "Gjallarhorn",
    "description": "Forged from the armor of fallen Guardians...",
    "icon": "https://bungie.net/common/destiny2_content/icons/..."
  },
  "itemType": 3,
  "tierType": 6,
  "classType": 3,
  "damageType": 3,
  "categories": {
    "isWeapon": true,
    "isArmor": false,
    "isExotic": true
  },
  "powerCap": 1810,
  "ammoType": 3
}
```

#### Enhanced Search
```http
GET /api/manifest/items/search?q=gjallarhorn&tier=6&weapon=true
```
**Parameters**:
- `q` - Text search query
- `type` - Item type (1=Currency, 2=Armor, 3=Weapon, etc.)
- `tier` - Tier type (3=Common, 4=Rare, 5=Legendary, 6=Exotic)
- `class` - Class type (0=Titan, 1=Hunter, 2=Warlock, 3=Any)
- `damage` - Damage type (1=Kinetic, 2=Arc, 3=Solar, 4=Void, 6=Stasis, 7=Strand)
- `power_min`/`power_max` - Power cap range
- Boolean filters: `weapon`, `armor`, `consumable`, `mod`, `emblem`, `ghost`, `ship`, `sparrow`, `emote`, `shader`, `ornament`
- `limit` - Results per page (max 100, default 50)
- `offset` - Pagination offset

#### Fast Text Search (FTS5)
```http
GET /api/manifest/items/search/fts?q=exotic weapon
```
Ultra-fast full-text search using SQLite FTS5 for text-only queries.

#### Batch Item Lookup
```http
POST /api/manifest/items/batch
Content-Type: application/json

{
  "hashes": [4094900227, 2223009594, 1384536110],
  "raw": false
}
```

### Specialized Category Endpoints

#### Weapons
```http
GET /api/manifest/weapons?tier=6&damage=3&class=3
```
Weapon-specific search with damage type and class filtering.

#### Armor
```http
GET /api/manifest/armor?tier=5&class=1
```
Armor-specific search with class restrictions.

#### Cosmetics
```http
GET /api/manifest/cosmetics?category=ship&tier=6
```
**Categories**: `emblem`, `ship`, `sparrow`, `emote`, `shader`, `ghost`

#### Other Categories
- `/api/manifest/consumables` - Consumable items and materials
- `/api/manifest/mods` - Weapon and armor modifications

### Discovery & Utility

#### Random Items
```http
GET /api/manifest/random?count=5&category=weapon&tier=6
```
Get random items for discovery or testing.

#### Category Overview
```http
GET /api/manifest/categories
```
Lists all available categories with counts and endpoint mappings.

#### Manifest Statistics
```http
GET /api/manifest/stats
```
Comprehensive breakdown of items by category, tier, and class.

## 🔄 Update Management API

### Background Update Control

#### Start/Stop Background Updates
```http
POST /api/updater/start
POST /api/updater/stop
```

#### Force Immediate Update
```http
POST /api/updater/force-update
```

#### Updater Status
```http
GET /api/updater/status
```
```json
{
  "running": true,
  "status": "idle",
  "last_check": "2025-07-20T15:30:00Z",
  "last_update": "2025-07-19T08:15:00Z",
  "next_check": "2025-07-20T21:30:00Z",
  "check_interval_hours": 6,
  "uptime_hours": 24.5,
  "statistics": {
    "total_checks": 48,
    "total_updates": 2,
    "success_rate": 100.0,
    "consecutive_errors": 0
  },
  "health": {
    "status": "healthy",
    "consecutive_errors": 0
  }
}
```

### Configuration Management

#### Get/Update Configuration
```http
GET /api/updater/config
PUT /api/updater/config
Content-Type: application/json

{
  "check_interval_hours": 4.0
}
```
**Valid intervals**: 0.1 hours (6 minutes) to 168 hours (1 week)

### Health Monitoring

#### System Health Check
```http
GET /api/updater/system-health
```
```json
{
  "status": "healthy",
  "healthy": true,
  "uptime_hours": 24.5,
  "checks": {
    "database": {
      "healthy": true,
      "status": "ready",
      "message": "Database ready with 35,836 definitions"
    },
    "updater": {
      "healthy": true,
      "status": "healthy", 
      "message": "Updater healthy (running: true)"
    },
    "system_resources": {
      "healthy": true,
      "status": "good",
      "message": "Resources normal (CPU: 12.3%, Memory: 45.2%)"
    },
    "disk_space": {
      "healthy": true,
      "status": "good",
      "message": "Disk space sufficient: 78.5% free"
    },
    "api": {
      "healthy": true,
      "status": "operational",
      "message": "API operational with 35,836 items available"
    }
  },
  "summary": {
    "total_checks": 5,
    "healthy_checks": 5,
    "critical_issues": 0
  }
}
```

#### Performance Metrics
```http
GET /api/updater/performance
```
Real-time CPU, memory, and application performance data.

#### Complete Dashboard
```http
GET /api/updater/dashboard
```
Comprehensive monitoring data combining all system information.

#### Prometheus Metrics
```http
GET /api/updater/metrics
```
Metrics in Prometheus-compatible format for monitoring systems.

## 💾 Database Schema

### Item Categories
The system categorizes items using 11 boolean flags:
- `isWeapon` - Weapons (swords, guns, etc.)
- `isArmor` - Armor pieces (helmet, gauntlets, etc.) 
- `isConsumable` - Consumable items and materials
- `isMod` - Weapon and armor modifications
- `isEmblem` - Player emblems
- `isGhost` - Ghost shells
- `isShip` - Player ships
- `isSparrow` - Sparrow vehicles
- `isEmote` - Player emotes
- `isShader` - Armor shaders
- `isOrnament` - Weapon and armor ornaments

### Item Tiers
- `3` - Common (white)
- `4` - Rare (blue) 
- `5` - Legendary (purple)
- `6` - Exotic (yellow)

### Class Types
- `0` - Titan
- `1` - Hunter
- `2` - Warlock
- `3` - Any class

### Damage Types
- `0` - None/Kinetic
- `1` - Kinetic
- `2` - Arc
- `3` - Solar
- `4` - Void
- `6` - Stasis
- `7` - Strand

## 🔧 Advanced Usage

### Full-Text Search Tips
```http
# Simple text search (uses FTS5 automatically)
GET /api/manifest/items/search/fts?q=exotic hand cannon

# Complex boolean queries
GET /api/manifest/items/search/fts?q="gjallarhorn OR sleeper"

# Search with filters (uses regular SQL)
GET /api/manifest/items/search?q=exotic&tier=6&weapon=true&damage=3
```

### Power Cap Filtering
```http
# Find sunset weapons (power cap below current)
GET /api/manifest/weapons?power_max=1350

# Find current endgame items
GET /api/manifest/items/search?power_min=1750&tier=5
```

### Pagination
```http
# Get first page
GET /api/manifest/weapons?limit=25&offset=0

# Get second page  
GET /api/manifest/weapons?limit=25&offset=25
```

### Performance Optimization
- **Use FTS endpoints** for text-only searches (much faster)
- **Batch requests** for multiple items instead of individual calls
- **Limit results** appropriately (default 50, max 100)
- **Use category endpoints** instead of filtering search for better performance

## 🚨 Error Handling

### Common Error Responses
```json
// Item not found
{
  "error": "Item not found"
}

// Invalid parameters
{
  "error": "Query parameter 'q' is required"
}

// Rate limiting (if implemented)
{
  "error": "Rate limit exceeded"
}
```

### Health Status Codes
- **healthy** - All systems operational
- **degraded** - Some issues but functional
- **critical** - Major issues requiring attention

### Update Status Types
- **idle** - Waiting for next check
- **checking** - Checking for updates
- **downloading** - Downloading manifest
- **processing** - Processing downloaded data
- **complete** - Update completed successfully
- **error** - Update failed

## 🔍 Monitoring & Debugging

### System Health Monitoring
Monitor these key endpoints for production deployments:
- `/api/updater/health` - Quick health check
- `/api/updater/system-health` - Comprehensive health status
- `/api/updater/metrics` - Prometheus metrics

### Log Monitoring
The enhanced application provides structured logging:
```
INFO - Manifest updater started
INFO - Manifest check complete - no update needed  
INFO - Manifest update completed in 8.3s
ERROR - Manifest update error: Network timeout
```

### Performance Monitoring
Key metrics to track:
- **Update success rate** - Should be >95%
- **Check duration** - Should be <30 seconds
- **Update duration** - Should be <60 seconds  
- **System resources** - CPU <70%, Memory <70%
- **Disk space** - >10% free recommended

## 🚀 Production Deployment

### Environment Variables
```bash
export PORT=5001
export FLASK_DEBUG=false
export BUNGIE_API_KEY=your_api_key_here
```

### Health Check Configuration
Configure your load balancer to use:
- **Health check URL**: `/health`
- **Health check interval**: 30 seconds
- **Timeout**: 10 seconds
- **Healthy threshold**: 2 consecutive successes
- **Unhealthy threshold**: 3 consecutive failures

### Monitoring Integration
For Prometheus/Grafana monitoring:
```bash
# Scrape metrics endpoint
curl https://your-server/api/updater/metrics
```

### Backup Considerations
The manifest database is automatically updated, but consider:
- **Database backups** - `data/manifest.db` file
- **Configuration backups** - Environment variables and settings
- **Log retention** - Application logs for debugging

## 📈 Performance Characteristics

### Database Size
- **Manifest database**: ~200-250 MB
- **Total game definitions**: 35,000+
- **Weapons**: ~8,000 items
- **Armor**: ~12,000 items  
- **Cosmetics**: ~15,000 items

### Response Times
- **Item lookup by hash**: <5ms
- **Simple text search (FTS)**: <10ms
- **Complex filtered search**: <50ms
- **Batch requests (100 items)**: <100ms

### Update Performance
- **Manifest download**: 30-60 seconds
- **Database processing**: 5-15 seconds
- **Total update time**: 45-90 seconds
- **Update frequency**: Every 6 hours (configurable)

## 🎯 Use Cases

### Game Tool Development
```javascript
// Get all exotic weapons
const exoticWeapons = await fetch('/api/manifest/weapons?tier=6');

// Search for specific items
const searchResults = await fetch('/api/manifest/items/search/fts?q=fatebringer');

// Get random items for features
const randomItems = await fetch('/api/manifest/random?count=10&category=weapon');
```

### Data Analysis
```python
# Get comprehensive statistics
import requests
stats = requests.get('/api/manifest/stats').json()

# Monitor system health
health = requests.get('/api/updater/system-health').json()
```

### Loadout Tools
```javascript
// Get specific items by hash
const loadoutItems = await fetch('/api/manifest/items/batch', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    hashes: [4094900227, 2223009594, 1384536110]
  })
});
```

This manifest system provides enterprise-grade reliability and performance for any Destiny 2 application or tool! 🎮✨