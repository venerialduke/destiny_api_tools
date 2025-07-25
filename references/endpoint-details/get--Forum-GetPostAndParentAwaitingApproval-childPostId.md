# Forum Getpostandparentawaitingapproval

## Overview
Returns the post specified and its immediate parent of posts that are awaiting approval.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Forum/GetPostAndParentAwaitingApproval/{childPostId}/`
- **Operation ID:** `Forum.GetPostAndParentAwaitingApproval`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| childPostId | integer (int64) | Yes |  |

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
GET /Forum/GetPostAndParentAwaitingApproval/{childPostId}/
```

### With Query Parameters
```http
GET /Forum/GetPostAndParentAwaitingApproval/{childPostId}/?showbanned=example_value
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
- Returns the post specified and its immediate parent of posts that are awaiting approval.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
