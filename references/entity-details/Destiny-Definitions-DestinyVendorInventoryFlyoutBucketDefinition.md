# Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Information about a single inventory bucket in a vendor flyout UI and how it is shown.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| collapsible | boolean | If true, the inventory bucket should be able to be collapsed visually. | No |
| inventoryBucketHash | integer (uint32) | The inventory bucket whose contents should be shown. | No |
| sortItemsBy | integer (int32) | The methodology to use for sorting items from the flyout. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition object
const example = {
  collapsible: true,
  inventoryBucketHash: 123,
  sortItemsBy: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition object
example = {
    "collapsible": True,
    "inventoryBucketHash": 123,
    "sortItemsBy": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryBucketDefinition**: Referenced in this entity
- **Destiny.DestinyItemSortType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition":   {
      "description": "Information about a single inventory bucket in a vendor flyout UI and how it is shown.",
      "type": "object",
      "properties": {
          "collapsible": {
              "description": "If true, the inventory bucket should be able to be collapsed visually.",
              "type": "boolean"
          },
          "inventoryBucketHash": {
              "format": "uint32",
              "description": "The inventory bucket whose contents should be shown.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "sortItemsBy": {
              "format": "int32",
              "description": "The methodology to use for sorting items from the flyout.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyItemSortType"
              }
          }
      }
  }
}
```
