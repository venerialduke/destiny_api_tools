# Destiny.Requests.DestinyItemTransferRequest

## Entity Information
- **Entity Name**: Destiny.Requests.DestinyItemTransferRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemtransferrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemReferenceHash | integer (uint32) |  | No |
| stackSize | integer (int32) |  | No |
| transferToVault | boolean |  | No |
| itemId | integer (int64) | The instance ID of the item for this action request. | No |
| characterId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.DestinyItemTransferRequest object
const example = {
  itemReferenceHash: 123,
  stackSize: 123,
  transferToVault: true,
  itemId: 123,
  characterId: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Requests.DestinyItemTransferRequest object
example = {
    "itemReferenceHash": 123,
    "stackSize": 123,
    "transferToVault": True,
    "itemId": 123,
    "characterId": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Requests.DestinyItemTransferRequest":   {
      "type": "object",
      "properties": {
          "itemReferenceHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "stackSize": {
              "format": "int32",
              "type": "integer"
          },
          "transferToVault": {
              "type": "boolean"
          },
          "itemId": {
              "format": "int64",
              "description": "The instance ID of the item for this action request.",
              "type": "integer"
          },
          "characterId": {
              "format": "int64",
              "type": "integer"
          },
          "membershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          }
      }
  }
}
```
