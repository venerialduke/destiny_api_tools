# Content Getcontentbyid

## Overview
Returns a content item referenced by id

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Content/GetContentById/{id}/{locale}/`
- **Operation ID:** `Content.GetContentById`
- **Tags:** Content
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer (int64) | Yes |  |
| locale | string | Yes |  |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| head | boolean | No | false |


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
GET /Content/GetContentById/{id}/{locale}/
```

### With Query Parameters
```http
GET /Content/GetContentById/{id}/{locale}/?head=true
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
- Returns a content item referenced by id
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
