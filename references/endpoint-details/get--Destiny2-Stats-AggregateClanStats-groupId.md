# Destiny2 Getclanaggregatestats

## Overview
Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/Stats/AggregateClanStats/{groupId}/`
- **Operation ID:** `Destiny2.GetClanAggregateStats`
- **Tags:** Destiny2, Preview
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | Group ID of the clan whose leaderboards you wish to fetch. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| modes | string | No | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Destiny.HistoricalStats.DestinyClanAggregateStat"
      }
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
GET /Destiny2/Stats/AggregateClanStats/{groupId}/
```

### With Query Parameters
```http
GET /Destiny2/Stats/AggregateClanStats/{groupId}/?modes=example_value
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
- Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
