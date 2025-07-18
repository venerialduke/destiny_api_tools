# Tokens Getpartnerrewardhistory

## Overview
Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Tokens/Partner/History/{targetBnetMembershipId}/Application/{partnerApplicationId}/`
- **Operation ID:** `Tokens.GetPartnerRewardHistory`
- **Tags:** Tokens
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** PartnerOfferGrant

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| partnerApplicationId | integer (int32) | Yes | The partner application identifier. |
| targetBnetMembershipId | integer (int64) | Yes | The bungie.net user to return reward history for. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Tokens.PartnerRewardHistoryResponse"
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
GET /Tokens/Partner/History/{targetBnetMembershipId}/Application/{partnerApplicationId}/
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
- Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
