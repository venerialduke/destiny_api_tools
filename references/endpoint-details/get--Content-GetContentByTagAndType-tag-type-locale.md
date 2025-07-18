# Content Getcontentbytagandtype

## Overview
Returns the newest item that matches a given tag and Content Type.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Content/GetContentByTagAndType/{tag}/{type}/{locale}/`
- **Operation ID:** `Content.GetContentByTagAndType`
- **Tags:** Content
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| locale | string | Yes |  |
| tag | string | Yes |  |
| type | string | Yes |  |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| head | boolean | No | Not used. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Content.ContentItemPublicContract"
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
GET /Content/GetContentByTagAndType/{tag}/{type}/{locale}/
```

### With Query Parameters
```http
GET /Content/GetContentByTagAndType/{tag}/{type}/{locale}/?head=true
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
- Returns the newest item that matches a given tag and Content Type.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
