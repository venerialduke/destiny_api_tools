# Destiny2 Getvendor

## Overview
Get the details of a specific Vendor.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/`
- **Operation ID:** `Destiny2.GetVendor`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| characterId | integer (int64) | Yes | The Destiny Character ID of the character for whom we're getting vendor info. |
| destinyMembershipId | integer (int64) | Yes | Destiny membership ID of another user. You may be denied. |
| membershipType | integer (int32) | Yes | A valid non-BungieNet membership type. |
| vendorHash | integer (uint32) | Yes | The Hash identifier of the Vendor to be returned. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| components | array | No | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Destiny.Responses.DestinyVendorResponse"
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
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/
```

### With Query Parameters
```http
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/?components=value
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
- Get the details of a specific Vendor.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
