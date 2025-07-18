# Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypostgamecarnagereportextendeddata data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| weapons | Array[Destiny.HistoricalStats.DestinyHistoricalWeaponStats] | List of weapons and their perspective values. | No |
| values | object | Collection of stats for the player in this activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData object
const example = {
  weapons: [],
  values: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData object
example = {
    "weapons": [],
    "values": None,
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalWeaponStats**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData":   {
      "type": "object",
      "properties": {
          "weapons": {
              "description": "List of weapons and their perspective values.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalWeaponStats"
              }
          },
          "values": {
              "description": "Collection of stats for the player in this activity.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          }
      }
  }
}
```
