# Content Rssnewsarticles

## Overview
Returns a JSON string response that is the RSS feed for news articles.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Content/Rss/NewsArticles/{pageToken}/`
- **Operation ID:** `Content.RssNewsArticles`
- **Tags:** Content
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageToken | string | Yes | Zero-based pagination token for paging through result sets. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| categoryfilter | string | No | Optionally filter response to only include news items in a certain category. |
| includebody | boolean | No | Optionally include full content body for each news item. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Content.NewsArticleRssResponse"
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
GET /Content/Rss/NewsArticles/{pageToken}/
```

### With Query Parameters
```http
GET /Content/Rss/NewsArticles/{pageToken}/?categoryfilter=example_value&includebody=true
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
- Returns a JSON string response that is the RSS feed for news articles.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
