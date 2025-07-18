# Fireteam Searchpublicavailableclanfireteams

## Overview
Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/`
- **Operation ID:** `Fireteam.SearchPublicAvailableClanFireteams`
- **Tags:** Fireteam
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| activityType | integer (int32) | Yes | The activity type to filter by. |
| dateRange | integer (byte) | Yes | The date range to grab available fireteams. |
| page | integer (int32) | Yes | Zero based page |
| platform | integer (byte) | Yes | The platform filter. |
| slotFilter | integer (byte) | Yes | Filters based on available slots |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| excludeImmediate | boolean | No | If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum. |
| langFilter | string | No | An optional language filter. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/SearchResultOfFireteamSummary"
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
GET /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### With Query Parameters
```http
GET /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/?excludeImmediate=true&langFilter=example_value
Authorization: Bearer YOUR_ACCESS_TOKEN
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
- Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
