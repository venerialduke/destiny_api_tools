# Social Getplatformfriendlist

## Overview
Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Social/PlatformFriends/{friendPlatform}/{page}/`
- **Operation ID:** `Social.GetPlatformFriendList`
- **Tags:** Social
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| friendPlatform | integer (int32) | Yes | The platform friend type. |
| page | string | Yes | The zero based page to return. Page size is 100. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Social.Friends.PlatformFriendResponse"
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
GET /Social/PlatformFriends/{friendPlatform}/{page}/
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
- Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
