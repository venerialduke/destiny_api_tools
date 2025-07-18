# Groupv2 Getinvitedindividuals

## Overview
Get the list of users who have been invited into the group.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GroupV2/{groupId}/Members/InvitedIndividuals/`
- **Operation ID:** `GroupV2.GetInvitedIndividuals`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** AdminGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| currentpage | integer (int32) | Yes | Page number (starting with 1). Each page has a fixed size of 50 items per page. |
| groupId | integer (int64) | Yes | ID of the group. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/SearchResultOfGroupMemberApplication"
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
GET /GroupV2/{groupId}/Members/InvitedIndividuals/
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
- Get the list of users who have been invited into the group.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
