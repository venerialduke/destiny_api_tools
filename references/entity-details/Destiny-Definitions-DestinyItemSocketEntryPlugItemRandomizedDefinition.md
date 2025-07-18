# Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemsocketentryplugitemrandomizeddefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| craftingRequirements | Destiny.Definitions.DestinyPlugItemCraftingRequirements |  | No |
| currentlyCanRoll | boolean | Indicates if the plug can be rolled on the current version of the item. For example, older versions of weapons may have plug rolls that are no longer possible on the current versions. | No |
| plugItemHash | integer (uint32) | The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition object
const example = {
  craftingRequirements: null,
  currentlyCanRoll: true,
  plugItemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition object
example = {
    "craftingRequirements": None,
    "currentlyCanRoll": True,
    "plugItemHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyPlugItemCraftingRequirements**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition":   {
      "type": "object",
      "properties": {
          "craftingRequirements": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyPlugItemCraftingRequirements"
          },
          "currentlyCanRoll": {
              "description": "Indicates if the plug can be rolled on the current version of the item. For example, older versions of weapons may have plug rolls that are no longer possible on the current versions.",
              "type": "boolean"
          },
          "plugItemHash": {
              "format": "uint32",
              "description": "The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
