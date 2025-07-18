# Forum Gettopicspaged

## Overview
Get topics from any forum.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/`
- **Operation ID:** `Forum.GetTopicsPaged`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| categoryFilter | integer (int32) | Yes | A category filter |
| group | integer (int64) | Yes | The group, if any. |
| page | integer (int32) | Yes | Zero paged page number |
| pageSize | integer (int32) | Yes | Unused |
| quickDate | integer (int32) | Yes | A date filter. |
| sort | integer (byte) | Yes | The sort mode. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| locales | string | No | Comma seperated list of locales posts must match to return in the result list. Default 'en' |
| tagstring | string | No | The tags to search, if any. |


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
GET /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/
```

### With Query Parameters
```http
GET /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/?locales=example_value&tagstring=example_value
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
- Get topics from any forum.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
