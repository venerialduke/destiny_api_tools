# Destiny.HistoricalStats.Definitions.DestinyActivityModeType[]

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.DestinyActivityModeType[]
- **Entity Type**: Schema (array)
- **Base Type**: array

## Description
Destiny API entity representing destinyactivitymodetype[] data.

## Usage Examples

### JavaScript
```javascript
```

### Python
```python
```

## Related Entities
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity

## Notes
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.DestinyActivityModeType[]":   {
      "type": "array",
      "items": {
          "format": "int32",
          "description": "For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!",
          "type": "integer",
          "x-enum-reference": {
              "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
          }
      }
  }
}
```
