# Tokens Claimpartneroffer

## Overview
Claim a partner offer as the authenticated user.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Tokens/Partner/ClaimOffer/`
- **Operation ID:** `Tokens.ClaimPartnerOffer`
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
POST /Tokens/Partner/ClaimOffer/
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
- Claim a partner offer as the authenticated user.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
