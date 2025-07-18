# Destiny2 Setitemlockstate

## Overview
Set the Lock State for an instanced item. You must have a valid Destiny Account.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Destiny2/Actions/Items/SetLockState/`
- **Operation ID:** `Destiny2.SetItemLockState`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** MoveEquipDestinyItems

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
POST /Destiny2/Actions/Items/SetLockState/
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
- Set the Lock State for an instanced item. You must have a valid Destiny Account.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
