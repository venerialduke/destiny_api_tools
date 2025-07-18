#  Getglobalalerts

## Overview
Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/GlobalAlerts/`
- **Operation ID:** `.GetGlobalAlerts`
- **Tags:** 
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includestreaming | boolean | No | Determines whether Streaming Alerts are included in results |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/GlobalAlert"
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
GET /GlobalAlerts/
```

### With Query Parameters
```http
GET /GlobalAlerts/?includestreaming=true
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
- Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
