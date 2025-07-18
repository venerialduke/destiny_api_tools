# Forum Getcoretopicspaged

## Overview
Gets a listing of all topics marked as part of the core group.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/`
- **Operation ID:** `Forum.GetCoreTopicsPaged`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| categoryFilter | integer (int32) | Yes | The category filter. |
| page | integer (int32) | Yes | Zero base page |
| quickDate | integer (int32) | Yes | The date filter. |
| sort | integer (byte) | Yes | The sort mode. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| locales | string | No | Comma seperated list of locales posts must match to return in the result list. Default 'en' |


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
GET /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/
```

### With Query Parameters
```http
GET /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/?locales=example_value
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
- Gets a listing of all topics marked as part of the core group.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
