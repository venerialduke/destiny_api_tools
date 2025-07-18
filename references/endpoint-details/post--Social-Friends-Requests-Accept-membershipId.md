# Social Acceptfriendrequest

## Overview
Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Social/Friends/Requests/Accept/{membershipId}/`
- **Operation ID:** `Social.AcceptFriendRequest`
- **Tags:** Social
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** BnetWrite

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| membershipId | string | Yes | The membership id of the user you wish to accept. |


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
POST /Social/Friends/Requests/Accept/{membershipId}/
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
- Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
