# Tokens.PartnerOfferHistoryResponse

## Entity Information
- **Entity Name**: Tokens.PartnerOfferHistoryResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for partnerofferhistoryresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| PartnerOfferKey | string |  | No |
| MembershipId | integer (int64) |  | No |
| MembershipType | integer (int32) |  | No |
| LocalizedName | string |  | No |
| LocalizedDescription | string |  | No |
| IsConsumable | boolean |  | No |
| QuantityApplied | integer (int32) |  | No |
| ApplyDate | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.PartnerOfferHistoryResponse object
const example = {
  PartnerOfferKey: "example value",
  MembershipId: 123,
  MembershipType: 123,
  LocalizedName: "example value",
  LocalizedDescription: "example value",
  // ... more properties
};
```

### Python
```python
# Example Tokens.PartnerOfferHistoryResponse object
example = {
    "PartnerOfferKey": "example value",
    "MembershipId": 123,
    "MembershipType": 123,
    "LocalizedName": "example value",
    "LocalizedDescription": "example value",
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.PartnerOfferHistoryResponse":   {
      "type": "object",
      "properties": {
          "PartnerOfferKey": {
              "type": "string"
          },
          "MembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "MembershipType": {
              "format": "int32",
              "enum": [
                  "0",
                  "1",
                  "2",
                  "3",
                  "4",
                  "5",
                  "6",
                  "10",
                  "20",
                  "254",
                  "-1"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "TigerXbox"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "TigerPsn"
                  },
                  {
                      "numericValue": "3",
                      "identifier": "TigerSteam"
                  },
                  {
                      "numericValue": "4",
                      "identifier": "TigerBlizzard"
                  },
                  {
                      "numericValue": "5",
                      "identifier": "TigerStadia"
                  },
                  {
                      "numericValue": "6",
                      "identifier": "TigerEgs"
                  },
                  {
                      "numericValue": "10",
                      "identifier": "TigerDemon"
                  },
                  {
                      "numericValue": "20",
                      "identifier": "GoliathGame"
                  },
                  {
                      "numericValue": "254",
                      "identifier": "BungieNext"
                  },
                  {
                      "numericValue": "-1",
                      "identifier": "All",
                      "description": "\"All\" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for any query where you pass a known membershipId."
                  }
              ]
          },
          "LocalizedName": {
              "type": "string"
          },
          "LocalizedDescription": {
              "type": "string"
          },
          "IsConsumable": {
              "type": "boolean"
          },
          "QuantityApplied": {
              "format": "int32",
              "type": "integer"
          },
          "ApplyDate": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
