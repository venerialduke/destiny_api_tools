# Destiny.Definitions.DestinyVendorAcceptedItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorAcceptedItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If you ever wondered how the Vault works, here it is.
The Vault is merely a set of inventory buckets that exist on your Profile/Account level. When you transfer items in the Vault, the game is using the Vault Vendor's DestinyVendorAcceptedItemDefinitions to see where the appropriate destination bucket is for the source bucket from whence your item is moving. If it finds such an entry, it transfers the item to the other bucket.
The mechanics for Postmaster works similarly, which is also a vendor. All driven by Accepted Items.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| acceptedInventoryBucketHash | integer (uint32) | The "source" bucket for a transfer. When a user wants to transfer an item, the appropriate DestinyVendorDefinition's acceptedItems property is evaluated, looking for an entry where acceptedInventoryBucketHash matches the bucket that the item being transferred is currently located. If it exists, the item will be transferred into whatever bucket is defined by destinationInventoryBucketHash. | No |
| destinationInventoryBucketHash | integer (uint32) | This is the bucket where the item being transferred will be put, given that it was being transferred *from* the bucket defined in acceptedInventoryBucketHash. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorAcceptedItemDefinition object
const example = {
  acceptedInventoryBucketHash: 123,
  destinationInventoryBucketHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorAcceptedItemDefinition object
example = {
    "acceptedInventoryBucketHash": 123,
    "destinationInventoryBucketHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryBucketDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorAcceptedItemDefinition":   {
      "description": "If you ever wondered how the Vault works, here it is.\r\nThe Vault is merely a set of inventory buckets that exist on your Profile/Account level. When you transfer items in the Vault, the game is using the Vault Vendor's DestinyVendorAcceptedItemDefinitions to see where the appropriate destination bucket is for the source bucket from whence your item is moving. If it finds such an entry, it transfers the item to the other bucket.\r\nThe mechanics for Postmaster works similarly, which is also a vendor. All driven by Accepted Items.",
      "type": "object",
      "properties": {
          "acceptedInventoryBucketHash": {
              "format": "uint32",
              "description": "The \"source\" bucket for a transfer. When a user wants to transfer an item, the appropriate DestinyVendorDefinition's acceptedItems property is evaluated, looking for an entry where acceptedInventoryBucketHash matches the bucket that the item being transferred is currently located. If it exists, the item will be transferred into whatever bucket is defined by destinationInventoryBucketHash.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "destinationInventoryBucketHash": {
              "format": "uint32",
              "description": "This is the bucket where the item being transferred will be put, given that it was being transferred *from* the bucket defined in acceptedInventoryBucketHash.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          }
      }
  }
}
```
