# Tokens.PartnerOfferClaimRequest

## Entity Information
- **Entity Name**: Tokens.PartnerOfferClaimRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for partnerofferclaimrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| PartnerOfferId | string |  | No |
| BungieNetMembershipId | integer (int64) |  | No |
| TransactionId | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.PartnerOfferClaimRequest object
const example = {
  PartnerOfferId: "example value",
  BungieNetMembershipId: 123,
  TransactionId: "example value",
};
```

### Python
```python
# Example Tokens.PartnerOfferClaimRequest object
example = {
    "PartnerOfferId": "example value",
    "BungieNetMembershipId": 123,
    "TransactionId": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.PartnerOfferClaimRequest":   {
      "type": "object",
      "properties": {
          "PartnerOfferId": {
              "type": "string"
          },
          "BungieNetMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "TransactionId": {
              "type": "string"
          }
      }
  }
}
```
