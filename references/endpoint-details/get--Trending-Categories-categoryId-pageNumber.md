# Trending Gettrendingcategory

## Overview
Returns paginated lists of trending items for a category.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Trending/Categories/{categoryId}/{pageNumber}/`
- **Operation ID:** `Trending.GetTrendingCategory`
- **Tags:** Trending
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| categoryId | string | Yes | The ID of the category for whom you want additional results. |
| pageNumber | integer (int32) | Yes | The page # of results to return. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/SearchResultOfTrendingEntry"
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
GET /Trending/Categories/{categoryId}/{pageNumber}/
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
- Returns paginated lists of trending items for a category.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
