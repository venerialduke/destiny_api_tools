# Fireteam Getactiveprivateclanfireteamcount

## Overview
Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Fireteam/Clan/{groupId}/ActiveCount/`
- **Operation ID:** `Fireteam.GetActivePrivateClanFireteamCount`
- **Tags:** Fireteam
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | The group id of the clan. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "format": "int32",
      "type": "integer"
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
GET /Fireteam/Clan/{groupId}/ActiveCount/
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
- Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
