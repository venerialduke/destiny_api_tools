# Groupv2 Getadminsandfounderofgroup

## Overview
Get the list of members in a given group who are of admin level or higher.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GroupV2/{groupId}/AdminsAndFounder/`
- **Operation ID:** `GroupV2.GetAdminsAndFounderOfGroup`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| currentpage | integer (int32) | Yes | Page number (starting with 1). Each page has a fixed size of 50 items per page. |
| groupId | integer (int64) | Yes | The ID of the group. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/SearchResultOfGroupMember"
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
GET /GroupV2/{groupId}/AdminsAndFounder/
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
- Get the list of members in a given group who are of admin level or higher.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
