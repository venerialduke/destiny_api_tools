# Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A subclass of DestinyItemQuantity, that provides not just the item and its quantity but also information that BNet can - at some point - use internally to provide more robust runtime information about the item's qualities.
If you want it, please ask! We're just out of time to wire it up right now. Or a clever person just may do it with our existing endpoints.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | The quest reward item *may* be associated with a vendor. If so, this is that vendor. Use this hash to look up the DestinyVendorDefinition. | No |
| vendorItemIndex | integer (int32) | The quest reward item *may* be associated with a vendor. If so, this is the index of the item being sold, which we can use at runtime to find instanced item information for the reward item. | No |
| itemHash | integer (uint32) | The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition. | No |
| itemInstanceId | integer (int64) | If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null. | No |
| quantity | integer (int32) | The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used. | No |
| hasConditionalVisibility | boolean | Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem object
const example = {
  vendorHash: 123,
  vendorItemIndex: 123,
  itemHash: 123,
  itemInstanceId: 123,
  quantity: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem object
example = {
    "vendorHash": 123,
    "vendorItemIndex": 123,
    "itemHash": 123,
    "itemInstanceId": 123,
    "quantity": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem":   {
      "description": "A subclass of DestinyItemQuantity, that provides not just the item and its quantity but also information that BNet can - at some point - use internally to provide more robust runtime information about the item's qualities.\r\nIf you want it, please ask! We're just out of time to wire it up right now. Or a clever person just may do it with our existing endpoints.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "The quest reward item *may* be associated with a vendor. If so, this is that vendor. Use this hash to look up the DestinyVendorDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "vendorItemIndex": {
              "format": "int32",
              "description": "The quest reward item *may* be associated with a vendor. If so, this is the index of the item being sold, which we can use at runtime to find instanced item information for the reward item.",
              "type": "integer"
          },
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "itemInstanceId": {
              "format": "int64",
              "description": "If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.",
              "type": "integer"
          },
          "quantity": {
              "format": "int32",
              "description": "The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.",
              "type": "integer"
          },
          "hasConditionalVisibility": {
              "description": "Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.",
              "type": "boolean"
          }
      }
  }
}
```
