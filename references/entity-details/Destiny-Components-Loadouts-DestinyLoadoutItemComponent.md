# Destiny.Components.Loadouts.DestinyLoadoutItemComponent

## Entity Information
- **Entity Name**: Destiny.Components.Loadouts.DestinyLoadoutItemComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutitemcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemInstanceId | integer (int64) |  | No |
| plugItemHashes | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Loadouts.DestinyLoadoutItemComponent object
const example = {
  itemInstanceId: 123,
  plugItemHashes: [],
};
```

### Python
```python
# Example Destiny.Components.Loadouts.DestinyLoadoutItemComponent object
example = {
    "itemInstanceId": 123,
    "plugItemHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Loadouts.DestinyLoadoutItemComponent":   {
      "type": "object",
      "properties": {
          "itemInstanceId": {
              "format": "int64",
              "type": "integer"
          },
          "plugItemHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
