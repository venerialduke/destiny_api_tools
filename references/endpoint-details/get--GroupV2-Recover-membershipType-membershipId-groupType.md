# Groupv2 Recovergroupforfounder

## Overview
Allows a founder to manually recover a group they can see in game but not on bungie.net

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/`
- **Operation ID:** `GroupV2.RecoverGroupForFounder`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupType | integer (int32) | Yes | Type of group the supplied member founded. |
| membershipId | integer (int64) | Yes | Membership ID to for which to find founded groups. |
| membershipType | integer (int32) | Yes | Membership type of the supplied membership ID. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/GroupsV2.GroupMembershipSearchResponse"
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
GET /GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/
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
- Allows a founder to manually recover a group they can see in game but not on bungie.net
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
