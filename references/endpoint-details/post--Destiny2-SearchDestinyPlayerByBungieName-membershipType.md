# Destiny2 Searchdestinyplayerbybungiename

## Overview
Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/`
- **Operation ID:** `Destiny2.SearchDestinyPlayerByBungieName`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| membershipType | integer (int32) | Yes | A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/User.UserInfoCard"
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
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/
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
- Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
