# Content Searchcontentwithtext

## Overview
Gets content based on querystring information passed in. Provides basic search and text search capabilities.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Content/Search/{locale}/`
- **Operation ID:** `Content.SearchContentWithText`
- **Tags:** Content
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| locale | string | Yes |  |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ctype | string | No | Content type tag: Help, News, etc. Supply multiple ctypes separated by space. |
| currentpage | integer (int32) | No | Page number for the search results, starting with page 1. |
| head | boolean | No | Not used. |
| searchtext | string | No | Word or phrase for the search. |
| source | string | No | For analytics, hint at the part of the app that triggered the search. Optional. |
| tag | string | No | Tag used on the content to be searched. |


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
GET /Content/Search/{locale}/
```

### With Query Parameters
```http
GET /Content/Search/{locale}/?ctype=example_value&currentpage=123
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
- Gets content based on querystring information passed in. Provides basic search and text search capabilities.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
