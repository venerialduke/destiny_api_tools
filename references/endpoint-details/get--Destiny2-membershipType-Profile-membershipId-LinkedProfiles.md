# Destiny2 Getlinkedprofiles

## Overview
Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/`
- **Operation ID:** `Destiny2.GetLinkedProfiles`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| membershipId | integer (int64) | Yes | The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work! |
| membershipType | integer (int32) | Yes | The type for the membership whose linked Destiny accounts you want returned. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| getAllMemberships | boolean | No | (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Destiny.Responses.DestinyLinkedProfilesResponse"
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
GET /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/
```

### With Query Parameters
```http
GET /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/?getAllMemberships=true
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
- Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
