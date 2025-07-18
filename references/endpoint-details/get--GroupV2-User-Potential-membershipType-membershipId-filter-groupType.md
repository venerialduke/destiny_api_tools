# Groupv2 Getpotentialgroupsformember

## Overview
Get information about the groups that a given member has applied to or been invited to.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/`
- **Operation ID:** `GroupV2.GetPotentialGroupsForMember`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filter | integer (int32) | Yes | Filter apply to list of potential joined groups. |
| groupType | integer (int32) | Yes | Type of group the supplied member applied. |
| membershipId | integer (int64) | Yes | Membership ID to for which to find applied groups. |
| membershipType | integer (int32) | Yes | Membership type of the supplied membership ID. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/GroupsV2.GroupPotentialMembershipSearchResponse"
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
GET /GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/
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
- Get information about the groups that a given member has applied to or been invited to.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
