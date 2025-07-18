# Destiny2 Getclanweeklyrewardstate

## Overview
Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/Clan/{groupId}/WeeklyRewardState/`
- **Operation ID:** `Destiny2.GetClanWeeklyRewardState`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | A valid group id of clan. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Destiny.Milestones.DestinyMilestone"
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
GET /Destiny2/Clan/{groupId}/WeeklyRewardState/
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
- Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
