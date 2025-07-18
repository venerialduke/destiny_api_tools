# Destiny2 Gethistoricalstats

## Overview
Gets historical stats for indicated character.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/`
- **Operation ID:** `Destiny2.GetHistoricalStats`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| characterId | integer (int64) | Yes | The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters. |
| destinyMembershipId | integer (int64) | Yes | The Destiny membershipId of the user to retrieve. |
| membershipType | integer (int32) | Yes | A valid non-BungieNet membership type. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| dayend | string (date-time) | No | Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. |
| daystart | string (date-time) | No | First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. |
| groups | array | No | Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals |
| modes | array | No | Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. |
| periodType | integer (int32) | No | Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod"
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
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/
```

### With Query Parameters
```http
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/?dayend=example_value&daystart=example_value
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
- Gets historical stats for indicated character.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
