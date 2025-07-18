# Destiny.Components.Items.DestinyItemPlugComponent

## Entity Information
- **Entity Name**: Destiny.Components.Items.DestinyItemPlugComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Plugs are non-instanced items that can provide Stat and Perk benefits when socketed into an instanced item. Items have Sockets, and Plugs are inserted into Sockets.
This component finds all items that are considered "Plugs" in your inventory, and return information about the plug aside from any specific Socket into which it could be inserted.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugObjectives | Array[Destiny.Quests.DestinyObjectiveProgress] | Sometimes, Plugs may have objectives: these are often used for flavor and display purposes, but they can be used for any arbitrary purpose (both fortunately and unfortunately). Recently (with Season 2) they were expanded in use to be used as the "gating" for whether the plug can be inserted at all. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data. | No |
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
// Example Destiny.Components.Items.DestinyItemPlugComponent object
const example = {
  plugObjectives: [],
  plugItemHash: 123,
  canInsert: true,
  enabled: true,
  insertFailIndexes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Components.Items.DestinyItemPlugComponent object
example = {
    "plugObjectives": [],
    "plugItemHash": 123,
    "canInsert": True,
    "enabled": True,
    "insertFailIndexes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Items.DestinyItemPlugComponent":   {
      "description": "Plugs are non-instanced items that can provide Stat and Perk benefits when socketed into an instanced item. Items have Sockets, and Plugs are inserted into Sockets.\r\nThis component finds all items that are considered \"Plugs\" in your inventory, and return information about the plug aside from any specific Socket into which it could be inserted.",
      "type": "object",
      "properties": {
          "plugObjectives": {
              "description": "Sometimes, Plugs may have objectives: these are often used for flavor and display purposes, but they can be used for any arbitrary purpose (both fortunately and unfortunately). Recently (with Season 2) they were expanded in use to be used as the \"gating\" for whether the plug can be inserted at all. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
              }
          },
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
      },
      "x-destiny-component-type-dependency": "ItemPlugStates"
  }
}
```
