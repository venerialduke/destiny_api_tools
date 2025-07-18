# Groupv2 Getuserclaninvitesetting

## Overview
Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GroupV2/GetUserClanInviteSetting/{mType}/`
- **Operation ID:** `GroupV2.GetUserClanInviteSetting`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadUserData

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| mType | integer (int32) | Yes | The Destiny membership type of the account we wish to access settings. |


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
GET /GroupV2/GetUserClanInviteSetting/{mType}/
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
- Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
