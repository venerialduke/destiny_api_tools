# Tokens Forcedropsrepair

## Overview
Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Tokens/Partner/ForceDropsRepair/`
- **Operation ID:** `Tokens.ForceDropsRepair`
- **Tags:** Tokens
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** PartnerOfferGrant

## Parameters

This endpoint does not require any parameters.

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
POST /Tokens/Partner/ForceDropsRepair/
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
- Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
