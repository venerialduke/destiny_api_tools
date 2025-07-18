# Tokens Applymissingpartnerofferswithoutclaim

## Overview
Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/`
- **Operation ID:** `Tokens.ApplyMissingPartnerOffersWithoutClaim`
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
      "type": "boolean"
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
POST /Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/
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
- Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
