# Communitycontent Getcommunitycontent

## Overview
Returns community content.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/CommunityContent/Get/{sort}/{mediaFilter}/{page}/`
- **Operation ID:** `CommunityContent.GetCommunityContent`
- **Tags:** CommunityContent
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| mediaFilter | integer (int32) | Yes | The type of media to get |
| page | integer (int32) | Yes | Zero based page |
| sort | integer (byte) | Yes | The sort mode. |


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
GET /CommunityContent/Get/{sort}/{mediaFilter}/{page}/
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
- Returns community content.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
