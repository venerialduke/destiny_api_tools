# Destiny2 Awaprovideauthorizationresult

## Overview
Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Destiny2/Awa/AwaProvideAuthorizationResult/`
- **Operation ID:** `Destiny2.AwaProvideAuthorizationResult`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

This endpoint does not require any parameters.

## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "format": "int32",
      "type": "integer"
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
POST /Destiny2/Awa/AwaProvideAuthorizationResult/
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
- Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
