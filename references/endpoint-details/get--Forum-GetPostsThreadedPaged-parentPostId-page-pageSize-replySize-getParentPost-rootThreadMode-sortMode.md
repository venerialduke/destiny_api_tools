# Forum Getpoststhreadedpaged

## Overview
Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/`
- **Operation ID:** `Forum.GetPostsThreadedPaged`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| getParentPost | boolean | Yes |  |
| page | integer (int32) | Yes |  |
| pageSize | integer (int32) | Yes |  |
| parentPostId | integer (int64) | Yes |  |
| replySize | integer (int32) | Yes |  |
| rootThreadMode | boolean | Yes |  |
| sortMode | integer (int32) | Yes |  |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| showbanned | string | No | If this value is not null or empty, banned posts are requested to be returned |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Forum.PostSearchResponse"
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
GET /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/
```

### With Query Parameters
```http
GET /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/?showbanned=example_value
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
- Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
