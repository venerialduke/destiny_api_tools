# Fireteamfinder Searchlistingsbyfilters

## Overview
Returns search results for available Fireteams provided search filters.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/FireteamFinder/Search/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/`
- **Operation ID:** `FireteamFinder.SearchListingsByFilters`
- **Tags:** FireteamFinder
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| destinyCharacterId | integer (int64) | Yes | A valid Destiny character ID. |
| destinyMembershipId | integer (int64) | Yes | A valid Destiny membership ID. |
| destinyMembershipType | integer (int32) | Yes | A valid Destiny membership type. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| overrideOfflineFilter | boolean | No | Optional boolean to bypass the offline-only check, so the client can pull fireteam from the game. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersResponse"
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
POST /FireteamFinder/Search/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
```

### With Query Parameters
```http
POST /FireteamFinder/Search/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/?overrideOfflineFilter=true
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
- Returns search results for available Fireteams provided search filters.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
