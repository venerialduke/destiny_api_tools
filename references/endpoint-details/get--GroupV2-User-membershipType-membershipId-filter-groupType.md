# Groupv2 Getgroupsformember

## Overview
Get information about the groups that a given member has joined.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/`
- **Operation ID:** `GroupV2.GetGroupsForMember`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filter | integer (int32) | Yes | Filter apply to list of joined groups. |
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
      "$ref": "#/definitions/GroupsV2.GetGroupsForMemberResponse"
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
GET /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/
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
- Get information about the groups that a given member has joined.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
