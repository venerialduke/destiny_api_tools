# Destiny2 Getleaderboards

## Overview
Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/`
- **Operation ID:** `Destiny2.GetLeaderboards`
- **Tags:** Destiny2, Preview
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
| maxtop | integer (int32) | No | Maximum number of top players to return. Use a large number to get entire leaderboard. |
| modes | string | No | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. |
| statid | string | No | ID of stat to return rather than returning all Leaderboard stats. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "additionalProperties": {
          "$ref": "#/definitions/Destiny.HistoricalStats.DestinyLeaderboard"
        }
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
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/
```

### With Query Parameters
```http
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/?maxtop=123&modes=example_value
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
- Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
