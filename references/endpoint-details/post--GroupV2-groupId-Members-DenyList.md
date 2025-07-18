# Groupv2 Denypendingforlist

## Overview
Deny all of the pending users for the given group that match the passed-in .

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/{groupId}/Members/DenyList/`
- **Operation ID:** `GroupV2.DenyPendingForList`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** AdminGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | ID of the group. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Entities.EntityActionResult"
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
POST /GroupV2/{groupId}/Members/DenyList/
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
- Deny all of the pending users for the given group that match the passed-in .
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
