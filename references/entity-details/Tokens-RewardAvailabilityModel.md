# Tokens.RewardAvailabilityModel

## Entity Information
- **Entity Name**: Tokens.RewardAvailabilityModel
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for rewardavailabilitymodel operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| HasExistingCode | boolean |  | No |
| RecordDefinitions | Array[Destiny.Definitions.Records.DestinyRecordDefinition] |  | No |
| CollectibleDefinitions | Array[Tokens.CollectibleDefinitions] |  | No |
| IsOffer | boolean |  | No |
| HasOffer | boolean |  | No |
| OfferApplied | boolean |  | No |
| DecryptedToken | string |  | No |
| IsLoyaltyReward | boolean |  | No |
| ShopifyEndDate | string (date-time) |  | No |
| GameEarnByDate | string (date-time) |  | No |
| RedemptionEndDate | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.RewardAvailabilityModel object
const example = {
  HasExistingCode: true,
  RecordDefinitions: [],
  CollectibleDefinitions: [],
  IsOffer: true,
  HasOffer: true,
  // ... more properties
};
```

### Python
```python
# Example Tokens.RewardAvailabilityModel object
example = {
    "HasExistingCode": True,
    "RecordDefinitions": [],
    "CollectibleDefinitions": [],
    "IsOffer": True,
    "HasOffer": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Records.DestinyRecordDefinition**: Referenced in this entity
- **Tokens.CollectibleDefinitions**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.RewardAvailabilityModel":   {
      "type": "object",
      "properties": {
          "HasExistingCode": {
              "type": "boolean"
          },
          "RecordDefinitions": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordDefinition"
              }
          },
          "CollectibleDefinitions": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Tokens.CollectibleDefinitions"
              }
          },
          "IsOffer": {
              "type": "boolean"
          },
          "HasOffer": {
              "type": "boolean"
          },
          "OfferApplied": {
              "type": "boolean"
          },
          "DecryptedToken": {
              "type": "string"
          },
          "IsLoyaltyReward": {
              "type": "boolean"
          },
          "ShopifyEndDate": {
              "format": "date-time",
              "type": "string"
          },
          "GameEarnByDate": {
              "format": "date-time",
              "type": "string"
          },
          "RedemptionEndDate": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
