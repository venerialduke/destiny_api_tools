# Destiny2 Gethistoricalstatsforaccount

## Overview
Gets aggregate historical stats organized around each character for a given account.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/`
- **Operation ID:** `Destiny2.GetHistoricalStatsForAccount`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| destinyMembershipId | integer (int64) | Yes | The Destiny membershipId of the user to retrieve. |
| membershipType | integer (int32) | Yes | A valid non-BungieNet membership type. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groups | array | No | Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult"
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
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/
```

### With Query Parameters
```http
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/?groups=value
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
- Gets aggregate historical stats organized around each character for a given account.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
