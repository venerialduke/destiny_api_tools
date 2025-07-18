# Destiny.Sockets.DestinyItemPlugBase

## Entity Information
- **Entity Name**: Destiny.Sockets.DestinyItemPlugBase
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemplugbase data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugItemHash | integer (uint32) | The hash identifier of the DestinyInventoryItemDefinition that represents this plug. | No |
| canInsert | boolean | If true, this plug has met all of its insertion requirements. Big if true. | No |
| enabled | boolean | If true, this plug will provide its benefits while inserted. | No |
| insertFailIndexes | Array[integer] | If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted.
This list will be empty if the plug can be inserted. | No |
| enableFailIndexes | Array[integer] | If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.
This list will be empty if the plug is enabled. | No |
| stackSize | integer (int32) | If available, this is the stack size to display for the socket plug item. | No |
| maxStackSize | integer (int32) | If available, this is the maximum stack size to display for the socket plug item. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Sockets.DestinyItemPlugBase object
const example = {
  plugItemHash: 123,
  canInsert: true,
  enabled: true,
  insertFailIndexes: [],
  enableFailIndexes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Sockets.DestinyItemPlugBase object
example = {
    "plugItemHash": 123,
    "canInsert": True,
    "enabled": True,
    "insertFailIndexes": [],
    "enableFailIndexes": [],
    # ... more properties
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
  "Destiny.Sockets.DestinyItemPlugBase":   {
      "type": "object",
      "properties": {
          "plugItemHash": {
              "format": "uint32",
              "description": "The hash identifier of the DestinyInventoryItemDefinition that represents this plug.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "canInsert": {
              "description": "If true, this plug has met all of its insertion requirements. Big if true.",
              "type": "boolean"
          },
          "enabled": {
              "description": "If true, this plug will provide its benefits while inserted.",
              "type": "boolean"
          },
          "insertFailIndexes": {
              "description": "If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted.\r\nThis list will be empty if the plug can be inserted.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "enableFailIndexes": {
              "description": "If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.\r\nThis list will be empty if the plug is enabled.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "stackSize": {
              "format": "int32",
              "description": "If available, this is the stack size to display for the socket plug item.",
              "type": "integer"
          },
          "maxStackSize": {
              "format": "int32",
              "description": "If available, this is the maximum stack size to display for the socket plug item.",
              "type": "integer"
          }
      }
  }
}
```
