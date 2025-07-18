# Tokens.PartnerOfferSkuHistoryResponse

## Entity Information
- **Entity Name**: Tokens.PartnerOfferSkuHistoryResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for partnerofferskuhistoryresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| SkuIdentifier | string |  | No |
| LocalizedName | string |  | No |
| LocalizedDescription | string |  | No |
| ClaimDate | string (date-time) |  | No |
| AllOffersApplied | boolean |  | No |
| TransactionId | string |  | No |
| SkuOffers | Array[Tokens.PartnerOfferHistoryResponse] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.PartnerOfferSkuHistoryResponse object
const example = {
  SkuIdentifier: "example value",
  LocalizedName: "example value",
  LocalizedDescription: "example value",
  ClaimDate: "example value",
  AllOffersApplied: true,
  // ... more properties
};
```

### Python
```python
# Example Tokens.PartnerOfferSkuHistoryResponse object
example = {
    "SkuIdentifier": "example value",
    "LocalizedName": "example value",
    "LocalizedDescription": "example value",
    "ClaimDate": "example value",
    "AllOffersApplied": True,
    # ... more properties
}
```

## Related Entities
- **Tokens.PartnerOfferHistoryResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.PartnerOfferSkuHistoryResponse":   {
      "type": "object",
      "properties": {
          "SkuIdentifier": {
              "type": "string"
          },
          "LocalizedName": {
              "type": "string"
          },
          "LocalizedDescription": {
              "type": "string"
          },
          "ClaimDate": {
              "format": "date-time",
              "type": "string"
          },
          "AllOffersApplied": {
              "type": "boolean"
          },
          "TransactionId": {
              "type": "string"
          },
          "SkuOffers": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Tokens.PartnerOfferHistoryResponse"
              }
          }
      }
  }
}
```
