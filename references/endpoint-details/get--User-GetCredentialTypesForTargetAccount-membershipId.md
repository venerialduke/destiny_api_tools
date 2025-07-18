# User Getcredentialtypesfortargetaccount

## Overview
Returns a list of credential types attached to the requested account

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/User/GetCredentialTypesForTargetAccount/{membershipId}/`
- **Operation ID:** `User.GetCredentialTypesForTargetAccount`
- **Tags:** User
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| membershipId | integer (int64) | Yes | The user's membership id |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/User.Models.GetCredentialTypesForAccountResponse"
      }
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
GET /User/GetCredentialTypesForTargetAccount/{membershipId}/
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
- Returns a list of credential types attached to the requested account
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
