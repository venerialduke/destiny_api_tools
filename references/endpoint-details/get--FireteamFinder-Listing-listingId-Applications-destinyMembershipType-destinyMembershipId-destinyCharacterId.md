# Fireteamfinder Getlistingapplications

## Overview
Retrieves all applications to a Fireteam Finder listing.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/FireteamFinder/Listing/{listingId}/Applications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/`
- **Operation ID:** `FireteamFinder.GetListingApplications`
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
| listingId | integer (int64) | Yes | The ID of the listing whose applications to retrieve. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| flags | integer (int64) | No | Optional flag representing a filter on the state of the application. |
| nextPageToken | string | No | An optional token from a previous response to fetch the next page of results. |
| pageSize | integer (int32) | No | The maximum number of results to be returned with this page. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderGetListingApplicationsResponse"
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
GET /FireteamFinder/Listing/{listingId}/Applications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
```

### With Query Parameters
```http
GET /FireteamFinder/Listing/{listingId}/Applications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/?flags=123&nextPageToken=example_value
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
- Retrieves all applications to a Fireteam Finder listing.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
