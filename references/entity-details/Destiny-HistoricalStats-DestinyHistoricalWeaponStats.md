# Destiny.HistoricalStats.DestinyHistoricalWeaponStats

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalWeaponStats
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalweaponstats data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| referenceId | integer (uint32) | The hash ID of the item definition that describes the weapon. | No |
| values | object | Collection of stats for the period. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalWeaponStats object
const example = {
  referenceId: 123,
  values: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalWeaponStats object
example = {
    "referenceId": 123,
    "values": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalWeaponStats":   {
      "type": "object",
      "properties": {
          "referenceId": {
              "format": "uint32",
              "description": "The hash ID of the item definition that describes the weapon.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "values": {
              "description": "Collection of stats for the period.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          }
      }
  }
}
```
