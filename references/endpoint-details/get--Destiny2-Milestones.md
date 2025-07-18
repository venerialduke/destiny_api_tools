# Destiny2 Getpublicmilestones

## Overview
Gets public information about currently available Milestones.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/Milestones/`
- **Operation ID:** `Destiny2.GetPublicMilestones`
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
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestone"
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
GET /Destiny2/Milestones/
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
- Gets public information about currently available Milestones.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
