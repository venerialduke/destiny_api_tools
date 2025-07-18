# Tokens Getpartnerofferskuhistory

## Overview
Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Tokens/Partner/History/{partnerApplicationId}/{targetBnetMembershipId}/`
- **Operation ID:** `Tokens.GetPartnerOfferSkuHistory`
- **Tags:** Tokens
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** PartnerOfferGrant

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| partnerApplicationId | integer (int32) | Yes | The partner application identifier. |
| targetBnetMembershipId | integer (int64) | Yes | The bungie.net user to apply missing offers to. If not self, elevated permissions are required. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Tokens.PartnerOfferSkuHistoryResponse"
      }
    },
    "ErrorCode": {
      "format": "int32",
      "type": "integer",
      "x-enum-reference": {
        "$ref": "#/components/schemas/Exceptions.PlatformErrorCodes"
      }
    },
    "ThrottleSeconds": {
      "format": "int32",
      "type": "integer"
    },
    "ErrorStatus": {
      "type": "string"
    },
    "Message": {
      "type": "string"
    },
    "MessageData": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "DetailedErrorTrace": {
      "type": "string"
    }
  }
}
```


## Example Usage

### Request
```http
GET /Tokens/Partner/History/{partnerApplicationId}/{targetBnetMembershipId}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Response
```json
{
  "Response": {
    // Response data will be here
  },
  "ErrorCode": 1,
  "ThrottleSeconds": 0,
  "ErrorStatus": "Success",
  "Message": "Ok",
  "MessageData": {},
  "DetailedErrorTrace": ""
}
```

## Notes
- Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
