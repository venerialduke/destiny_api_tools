# Content Searchcontentbytagandtype

## Overview
Searches for Content Items that match the given Tag and Content Type.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Content/SearchContentByTagAndType/{tag}/{type}/{locale}/`
- **Operation ID:** `Content.SearchContentByTagAndType`
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
| currentpage | integer (int32) | No | Page number for the search results starting with page 1. |
| head | boolean | No | Not used. |
| itemsperpage | integer (int32) | No | Not used. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/SearchResultOfContentItemPublicContract"
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
GET /Content/SearchContentByTagAndType/{tag}/{type}/{locale}/
```

### With Query Parameters
```http
GET /Content/SearchContentByTagAndType/{tag}/{type}/{locale}/?currentpage=123&head=true
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
- Searches for Content Items that match the given Tag and Content Type.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
