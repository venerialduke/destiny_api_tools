# Destiny.Definitions.DestinyItemSetBlockEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSetBlockEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines a particular entry in an ItemSet (AKA a particular Quest Step in a Quest)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| trackingValue | integer (int32) | Used for tracking which step a user reached. These values will be populated in the user's internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash. | No |
| itemHash | integer (uint32) | This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSetBlockEntryDefinition object
const example = {
  trackingValue: 123,
  itemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSetBlockEntryDefinition object
example = {
    "trackingValue": 123,
    "itemHash": 123,
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
  "Destiny.Definitions.DestinyItemSetBlockEntryDefinition":   {
      "description": "Defines a particular entry in an ItemSet (AKA a particular Quest Step in a Quest)",
      "type": "object",
      "properties": {
          "trackingValue": {
              "format": "int32",
              "description": "Used for tracking which step a user reached. These values will be populated in the user's internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash.",
              "type": "integer"
          },
          "itemHash": {
              "format": "uint32",
              "description": "This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
