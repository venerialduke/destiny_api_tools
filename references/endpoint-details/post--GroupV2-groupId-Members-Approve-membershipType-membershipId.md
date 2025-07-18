# Groupv2 Approvepending

## Overview
Approve the given membershipId to join the group/clan as long as they have applied.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/`
- **Operation ID:** `GroupV2.ApprovePending`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** AdminGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | ID of the group. |
| membershipId | integer (int64) | Yes | The membership id being approved. |
| membershipType | integer (int32) | Yes | Membership type of the supplied membership ID. |


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
POST /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/
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
- Approve the given membershipId to join the group/clan as long as they have applied.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
