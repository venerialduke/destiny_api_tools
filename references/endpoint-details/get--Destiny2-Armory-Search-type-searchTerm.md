# Destiny2 Searchdestinyentities

## Overview
Gets a page list of Destiny items.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Destiny2/Armory/Search/{type}/{searchTerm}/`
- **Operation ID:** `Destiny2.SearchDestinyEntities`
- **Tags:** Destiny2
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| searchTerm | string | Yes | The string to use when searching for Destiny entities. |
| type | string | Yes | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer (int32) | No | Page number to return, starting with 0. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Destiny.Definitions.DestinyEntitySearchResult"
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
GET /Destiny2/Armory/Search/{type}/{searchTerm}/
```

### With Query Parameters
```http
GET /Destiny2/Armory/Search/{type}/{searchTerm}/?page=123
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
- Gets a page list of Destiny items.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
