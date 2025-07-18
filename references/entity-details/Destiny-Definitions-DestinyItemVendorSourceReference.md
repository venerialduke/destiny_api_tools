# Destiny.Definitions.DestinyItemVendorSourceReference

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemVendorSourceReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents that a vendor could sell this item, and provides a quick link to that vendor and sale item.
 Note that we do not and cannot make a guarantee that the vendor will ever *actually* sell this item, only that the Vendor has a definition that indicates it *could* be sold.
 Note also that a vendor may sell the same item in multiple "ways", which means there may be multiple vendorItemIndexes for a single Vendor hash.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | The identifier for the vendor that may sell this item. | No |
| vendorItemIndexes | Array[integer] | The Vendor sale item indexes that represent the sale information for this item. The same vendor may sell an item in multiple "ways", hence why this is a list. (for instance, a weapon may be "sold" as a reward in a quest, for Glimmer, and for Masterwork Cores: each of those ways would be represented by a different vendor sale item with a different index) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemVendorSourceReference object
const example = {
  vendorHash: 123,
  vendorItemIndexes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemVendorSourceReference object
example = {
    "vendorHash": 123,
    "vendorItemIndexes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemVendorSourceReference":   {
      "description": "Represents that a vendor could sell this item, and provides a quick link to that vendor and sale item.\r\n Note that we do not and cannot make a guarantee that the vendor will ever *actually* sell this item, only that the Vendor has a definition that indicates it *could* be sold.\r\n Note also that a vendor may sell the same item in multiple \"ways\", which means there may be multiple vendorItemIndexes for a single Vendor hash.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "The identifier for the vendor that may sell this item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "vendorItemIndexes": {
              "description": "The Vendor sale item indexes that represent the sale information for this item. The same vendor may sell an item in multiple \"ways\", hence why this is a list. (for instance, a weapon may be \"sold\" as a reward in a quest, for Glimmer, and for Masterwork Cores: each of those ways would be represented by a different vendor sale item with a different index)",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
