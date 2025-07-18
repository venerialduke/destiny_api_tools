# Fireteam Getmyclanfireteams

## Overview
Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/`
- **Operation ID:** `Fireteam.GetMyClanFireteams`
- **Tags:** Fireteam
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupId | integer (int64) | Yes | The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true). |
| includeClosed | boolean | Yes | If true, return fireteams that have been closed. |
| page | integer (int32) | Yes | Deprecated parameter, ignored. |
| platform | integer (byte) | Yes | The platform filter. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| groupFilter | boolean | No | If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams. |
| langFilter | string | No | An optional language filter. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/SearchResultOfFireteamResponse"
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
GET /Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### With Query Parameters
```http
GET /Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/?groupFilter=true&langFilter=example_value
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
- Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
