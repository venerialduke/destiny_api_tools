# Destiny.Definitions.Items.DestinyDerivedItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyDerivedItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is a reference to, and summary data for, a specific item that you can get as a result of Using or Acquiring some other Item (For example, this could be summary information for an Emote that you can get by opening an an Eververse Box) See DestinyDerivedItemCategoryDefinition for more information.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The hash for the DestinyInventoryItemDefinition of this derived item, if there is one. Sometimes we are given this information as a manual override, in which case there won't be an actual DestinyInventoryItemDefinition for what we display, but you can still show the strings from this object itself. | No |
| itemName | string | The name of the derived item. | No |
| itemDetail | string | Additional details about the derived item, in addition to the description. | No |
| itemDescription | string | A brief description of the item. | No |
| iconPath | string | An icon for the item. | No |
| vendorItemIndex | integer (int32) | If the item was derived from a "Preview Vendor", this will be an index into the DestinyVendorDefinition's itemList property. Otherwise, -1. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyDerivedItemDefinition object
const example = {
  itemHash: 123,
  itemName: "example value",
  itemDetail: "example value",
  itemDescription: "example value",
  iconPath: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyDerivedItemDefinition object
example = {
    "itemHash": 123,
    "itemName": "example value",
    "itemDetail": "example value",
    "itemDescription": "example value",
    "iconPath": "example value",
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyDerivedItemDefinition":   {
      "description": "This is a reference to, and summary data for, a specific item that you can get as a result of Using or Acquiring some other Item (For example, this could be summary information for an Emote that you can get by opening an an Eververse Box) See DestinyDerivedItemCategoryDefinition for more information.",
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The hash for the DestinyInventoryItemDefinition of this derived item, if there is one. Sometimes we are given this information as a manual override, in which case there won't be an actual DestinyInventoryItemDefinition for what we display, but you can still show the strings from this object itself.",
              "type": "integer"
          },
          "itemName": {
              "description": "The name of the derived item.",
              "type": "string"
          },
          "itemDetail": {
              "description": "Additional details about the derived item, in addition to the description.",
              "type": "string"
          },
          "itemDescription": {
              "description": "A brief description of the item.",
              "type": "string"
          },
          "iconPath": {
              "description": "An icon for the item.",
              "type": "string"
          },
          "vendorItemIndex": {
              "format": "int32",
              "description": "If the item was derived from a \"Preview Vendor\", this will be an index into the DestinyVendorDefinition's itemList property. Otherwise, -1.",
              "type": "integer"
          }
      }
  }
}
```
