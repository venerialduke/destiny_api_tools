# User Getmembershipfromhardlinkedcredential

## Overview
Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/User/GetMembershipFromHardLinkedCredential/{crType}/{credential}/`
- **Operation ID:** `User.GetMembershipFromHardLinkedCredential`
- **Tags:** User
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| credential | string | Yes | The credential to look up. Must be a valid SteamID64. |
| crType | integer (byte) | Yes | The credential type. 'SteamId' is the only valid value at present. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/User.HardLinkedUserMembership"
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
GET /User/GetMembershipFromHardLinkedCredential/{crType}/{credential}/
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
- Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
