# Destiny.DestinyProgressionRewardItemSocketOverrideState

## Entity Information
- **Entity Name**: Destiny.DestinyProgressionRewardItemSocketOverrideState
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents the stats and item state if applicable for progression reward items with socket overrides

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rewardItemStats | object | Information about the computed stats from socket and plug overrides for this progression, if there is any data for it. | No |
| itemState | integer (int32) | Information about the item state, specifically deepsight if there is any data for it | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyProgressionRewardItemSocketOverrideState object
const example = {
  rewardItemStats: null,
  itemState: 123,
};
```

### Python
```python
# Example Destiny.DestinyProgressionRewardItemSocketOverrideState object
example = {
    "rewardItemStats": None,
    "itemState": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity
- **Destiny.DestinyStat**: Referenced in this entity
- **Destiny.ItemState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgressionRewardItemSocketOverrideState":   {
      "description": "Represents the stats and item state if applicable for progression reward items with socket overrides",
      "type": "object",
      "properties": {
          "rewardItemStats": {
              "description": "Information about the computed stats from socket and plug overrides for this progression, if there is any data for it.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.DestinyStat"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "itemState": {
              "format": "int32",
              "description": "Information about the item state, specifically deepsight if there is any data for it",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ItemState"
              }
          }
      }
  }
}
```
