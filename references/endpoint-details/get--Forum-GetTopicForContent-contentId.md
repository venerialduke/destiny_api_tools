# Forum Gettopicforcontent

## Overview
Gets the post Id for the given content item's comments, if it exists.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Forum/GetTopicForContent/{contentId}/`
- **Operation ID:** `Forum.GetTopicForContent`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| contentId | integer (int64) | Yes |  |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "format": "int64",
      "type": "integer"
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
GET /Forum/GetTopicForContent/{contentId}/
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
- Gets the post Id for the given content item's comments, if it exists.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
