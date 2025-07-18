# User Getmembershipdataforcurrentuser

## Overview
Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/User/GetMembershipsForCurrentUser/`
- **Operation ID:** `User.GetMembershipDataForCurrentUser`
- **Tags:** User
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadBasicUserProfile

## Parameters

This endpoint does not require any parameters.

## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/User.UserMembershipData"
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
GET /User/GetMembershipsForCurrentUser/
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
- Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
