# User Searchbyglobalnameprefix

## Overview
[OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/User/Search/Prefix/{displayNamePrefix}/{page}/`
- **Operation ID:** `User.SearchByGlobalNamePrefix`
- **Tags:** User
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| displayNamePrefix | string | Yes | The display name prefix you're looking for. |
| page | integer (int32) | Yes | The zero-based page of results you desire. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/User.UserSearchResponse"
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
GET /User/Search/Prefix/{displayNamePrefix}/{page}/
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
- [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
