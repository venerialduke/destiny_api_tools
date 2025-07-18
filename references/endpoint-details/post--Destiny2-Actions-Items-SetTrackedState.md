# Destiny2 Setquesttrackedstate

## Overview
Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Destiny2/Actions/Items/SetTrackedState/`
- **Operation ID:** `Destiny2.SetQuestTrackedState`
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
POST /Destiny2/Actions/Items/SetTrackedState/
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
- Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
