# Groupv2 Kickmember

## Overview
Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/`
- **Operation ID:** `GroupV2.KickMember`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** AdminGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | Group ID to kick the user from. |
| membershipId | integer (int64) | Yes | Membership ID to kick. |
| membershipType | integer (int32) | Yes | Membership type of the provided membership ID. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/GroupsV2.GroupMemberLeaveResult"
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
POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/
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
- Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
