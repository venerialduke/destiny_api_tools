# Fireteamfinder Getplayerlobbies

## Overview
Retrieves the information for a Fireteam lobby.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/FireteamFinder/PlayerLobbies/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/`
- **Operation ID:** `FireteamFinder.GetPlayerLobbies`
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
| nextPageToken | string | No | An optional token from a previous response to fetch the next page of results. |
| pageSize | integer (int32) | No | The maximum number of results to be returned with this page. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderGetPlayerLobbiesResponse"
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
GET /FireteamFinder/PlayerLobbies/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
```

### With Query Parameters
```http
GET /FireteamFinder/PlayerLobbies/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/?nextPageToken=example_value&pageSize=123
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
- Retrieves the information for a Fireteam lobby.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
