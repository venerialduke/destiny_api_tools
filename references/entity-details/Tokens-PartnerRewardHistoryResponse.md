# Tokens.PartnerRewardHistoryResponse

## Entity Information
- **Entity Name**: Tokens.PartnerRewardHistoryResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for partnerrewardhistoryresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| PartnerOffers | Array[Tokens.PartnerOfferSkuHistoryResponse] |  | No |
| TwitchDrops | Array[Tokens.TwitchDropHistoryResponse] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.PartnerRewardHistoryResponse object
const example = {
  PartnerOffers: [],
  TwitchDrops: [],
};
```

### Python
```python
# Example Tokens.PartnerRewardHistoryResponse object
example = {
    "PartnerOffers": [],
    "TwitchDrops": [],
}
```

## Related Entities
- **Tokens.PartnerOfferSkuHistoryResponse**: Referenced in this entity
- **Tokens.TwitchDropHistoryResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.PartnerRewardHistoryResponse":   {
      "type": "object",
      "properties": {
          "PartnerOffers": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Tokens.PartnerOfferSkuHistoryResponse"
              }
          },
          "TwitchDrops": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Tokens.TwitchDropHistoryResponse"
              }
          }
      }
  }
}
```
