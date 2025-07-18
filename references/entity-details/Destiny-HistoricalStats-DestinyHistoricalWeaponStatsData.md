# Destiny.HistoricalStats.DestinyHistoricalWeaponStatsData

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalWeaponStatsData
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalweaponstatsdata data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| weapons | Array[Destiny.HistoricalStats.DestinyHistoricalWeaponStats] | List of weapons and their perspective values. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalWeaponStatsData object
const example = {
  weapons: [],
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalWeaponStatsData object
example = {
    "weapons": [],
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalWeaponStats**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalWeaponStatsData":   {
      "type": "object",
      "properties": {
          "weapons": {
              "description": "List of weapons and their perspective values.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalWeaponStats"
              }
          }
      }
  }
}
```
