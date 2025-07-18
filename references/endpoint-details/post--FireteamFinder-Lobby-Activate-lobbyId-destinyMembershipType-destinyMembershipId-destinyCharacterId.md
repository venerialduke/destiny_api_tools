# Fireteamfinder Activatelobby

## Overview
Activates a lobby and initializes it as an active Fireteam.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/FireteamFinder/Lobby/Activate/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/`
- **Operation ID:** `FireteamFinder.ActivateLobby`
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
| lobbyId | integer (int64) | Yes | The ID of the lobby to activate. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| forceActivation | boolean | No | Optional boolean to forcibly activate the lobby, kicking pending applicants. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "boolean"
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
POST /FireteamFinder/Lobby/Activate/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
```

### With Query Parameters
```http
POST /FireteamFinder/Lobby/Activate/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/?forceActivation=true
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
- Activates a lobby and initializes it as an active Fireteam.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
