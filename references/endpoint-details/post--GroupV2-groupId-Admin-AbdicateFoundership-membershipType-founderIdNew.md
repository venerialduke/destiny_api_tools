# Groupv2 Abdicatefoundership

## Overview
An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/`
- **Operation ID:** `GroupV2.AbdicateFoundership`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| founderIdNew | integer (int64) | Yes | The new founder for this group. Must already be a group admin. |
| groupId | integer (int64) | Yes | The target group id. |
| membershipType | integer (int32) | Yes | Membership type of the provided founderIdNew. |


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
POST /GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/
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
- An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
