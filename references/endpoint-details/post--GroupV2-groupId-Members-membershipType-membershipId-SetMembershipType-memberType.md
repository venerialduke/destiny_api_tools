# Groupv2 Editgroupmembership

## Overview
Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/`
- **Operation ID:** `GroupV2.EditGroupMembership`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** AdminGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | ID of the group to which the member belongs. |
| membershipId | integer (int64) | Yes | Membership ID to modify. |
| membershipType | integer (int32) | Yes | Membership type of the provide membership ID. |
| memberType | integer (int32) | Yes | New membertype for the specified member. |


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
POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/
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
- Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
