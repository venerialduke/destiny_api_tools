# Fireteam Getclanfireteam

## Overview
Gets a specific fireteam.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Fireteam/Clan/{groupId}/Summary/{fireteamId}/`
- **Operation ID:** `Fireteam.GetClanFireteam`
- **Tags:** Fireteam
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| fireteamId | integer (int64) | Yes | The unique id of the fireteam. |
| groupId | integer (int64) | Yes | The group id of the clan. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Fireteam.FireteamResponse"
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
GET /Fireteam/Clan/{groupId}/Summary/{fireteamId}/
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
- Gets a specific fireteam.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
