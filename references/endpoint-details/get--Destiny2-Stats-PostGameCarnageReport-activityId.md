# Destiny2 Getpostgamecarnagereport

## Overview
Gets the available post game carnage report for the activity ID.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/Stats/PostGameCarnageReport/{activityId}/`
- **Operation ID:** `Destiny2.GetPostGameCarnageReport`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| activityId | integer (int64) | Yes | The ID of the activity whose PGCR is requested. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyPostGameCarnageReportData"
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
GET /Destiny2/Stats/PostGameCarnageReport/{activityId}/
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
- Gets the available post game carnage report for the activity ID.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
