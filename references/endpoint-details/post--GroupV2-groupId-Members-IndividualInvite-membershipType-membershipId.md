# Groupv2 Individualgroupinvite

## Overview
Invite a user to join this group.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/`
- **Operation ID:** `GroupV2.IndividualGroupInvite`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** AdminGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | ID of the group you would like to join. |
| membershipId | integer (int64) | Yes | Membership id of the account being invited. |
| membershipType | integer (int32) | Yes | MembershipType of the account being invited. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/GroupsV2.GroupApplicationResponse"
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
POST /GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/
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
- Invite a user to join this group.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
