# Destiny.Entities.Items.DestinyItemComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The base item component, filled with properties that are generally useful to know in any item request or that don't feel worthwhile to put in their own component.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The identifier for the item's definition, which is where most of the useful static information for the item can be found. | No |
| itemInstanceId | integer (int64) | If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size. | No |
| quantity | integer (int32) | The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it) | No |
| bindStatus | integer (int32) | If the item is bound to a location, it will be specified in this enum. | No |
| location | integer (int32) | An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items. | No |
| bucketHash | integer (uint32) | The hash identifier for the specific inventory bucket in which the item is located. | No |
| transferStatus | integer (int32) | If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer). | No |
| lockable | boolean | If the item can be locked, this will indicate that state. | No |
| state | integer (int32) | A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it's tracked or locked for example, or whether it has a masterwork plug inserted. | No |
| overrideStyleItemHash | integer (uint32) | If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.
If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate. | No |
| expirationDate | string (date-time) | If the item can expire, this is the date at which it will/did expire. | No |
| isWrapper | boolean | If this is true, the object is actually a "wrapper" of the object it's representing. This means that it's not the actual item itself, but rather an item that must be "opened" in game before you have and can use the item.
 Wrappers are an evolution of "bundles", which give an easy way to let you preview the contents of what you purchased while still letting you get a refund before you "open" it. | No |
| tooltipNotificationIndexes | Array[integer] | If this is populated, it is a list of indexes into DestinyInventoryItemDefinition.tooltipNotifications for any special tooltip messages that need to be shown for this item. | No |
| metricHash | integer (uint32) | The identifier for the currently-selected metric definition, to be displayed on the emblem nameplate. | No |
| metricObjective | object | The objective progress for the currently-selected metric definition, to be displayed on the emblem nameplate. | No |
| versionNumber | integer (int32) | The version of this item, used to index into the versions list in the item definition quality block. | No |
| itemValueVisibility | Array[boolean] | If available, a list that describes which item values (rewards) should be shown (true) or hidden (false). | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemComponent object
const example = {
  itemHash: 123,
  itemInstanceId: 123,
  quantity: 123,
  bindStatus: 123,
  location: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemComponent object
example = {
    "itemHash": 123,
    "itemInstanceId": 123,
    "quantity": 123,
    "bindStatus": 123,
    "location": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryBucketDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Metrics.DestinyMetricDefinition**: Referenced in this entity
- **Destiny.ItemBindStatus**: Referenced in this entity
- **Destiny.ItemLocation**: Referenced in this entity
- **Destiny.ItemState**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity
- **Destiny.TransferStatuses**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemComponent":   {
      "description": "The base item component, filled with properties that are generally useful to know in any item request or that don't feel worthwhile to put in their own component.",
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The identifier for the item's definition, which is where most of the useful static information for the item can be found.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "itemInstanceId": {
              "format": "int64",
              "description": "If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size.",
              "type": "integer"
          },
          "quantity": {
              "format": "int32",
              "description": "The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it)",
              "type": "integer"
          },
          "bindStatus": {
              "format": "int32",
              "description": "If the item is bound to a location, it will be specified in this enum.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ItemBindStatus"
              }
          },
          "location": {
              "format": "int32",
              "description": "An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ItemLocation"
              }
          },
          "bucketHash": {
              "format": "uint32",
              "description": "The hash identifier for the specific inventory bucket in which the item is located.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "transferStatus": {
              "format": "int32",
              "description": "If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer).",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.TransferStatuses"
              }
          },
          "lockable": {
              "description": "If the item can be locked, this will indicate that state.",
              "type": "boolean"
          },
          "state": {
              "format": "int32",
              "description": "A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it's tracked or locked for example, or whether it has a masterwork plug inserted.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ItemState"
              }
          },
          "overrideStyleItemHash": {
              "format": "uint32",
              "description": "If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.\r\nIf you don't do this, certain items whose styles are being overridden by socketed items - such as the \"Recycle Shader\" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "expirationDate": {
              "format": "date-time",
              "description": "If the item can expire, this is the date at which it will/did expire.",
              "type": "string"
          },
          "isWrapper": {
              "description": "If this is true, the object is actually a \"wrapper\" of the object it's representing. This means that it's not the actual item itself, but rather an item that must be \"opened\" in game before you have and can use the item.\r\n Wrappers are an evolution of \"bundles\", which give an easy way to let you preview the contents of what you purchased while still letting you get a refund before you \"open\" it.",
              "type": "boolean"
          },
          "tooltipNotificationIndexes": {
              "description": "If this is populated, it is a list of indexes into DestinyInventoryItemDefinition.tooltipNotifications for any special tooltip messages that need to be shown for this item.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "metricHash": {
              "format": "uint32",
              "description": "The identifier for the currently-selected metric definition, to be displayed on the emblem nameplate.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Metrics.DestinyMetricDefinition"
              }
          },
          "metricObjective": {
              "description": "The objective progress for the currently-selected metric definition, to be displayed on the emblem nameplate.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              ]
          },
          "versionNumber": {
              "format": "int32",
              "description": "The version of this item, used to index into the versions list in the item definition quality block.",
              "type": "integer"
          },
          "itemValueVisibility": {
              "description": "If available, a list that describes which item values (rewards) should be shown (true) or hidden (false).",
              "type": "array",
              "items": {
                  "type": "boolean"
              }
          }
      }
  }
}
```
