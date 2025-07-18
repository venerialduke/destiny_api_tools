# Tokens Getbungierewardsforuser

## Overview
Returns the bungie rewards for the targeted user.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Tokens/Rewards/GetRewardsForUser/{membershipId}/`
- **Operation ID:** `Tokens.GetBungieRewardsForUser`
- **Tags:** Tokens
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadAndApplyTokens

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| membershipId | integer (int64) | Yes | bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/Tokens.BungieRewardDisplay"
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
GET /Tokens/Rewards/GetRewardsForUser/{membershipId}/
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
- Returns the bungie rewards for the targeted user.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
