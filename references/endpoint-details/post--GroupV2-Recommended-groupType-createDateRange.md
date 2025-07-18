# Groupv2 Getrecommendedgroups

## Overview
Gets groups recommended for you based on the groups to whom those you follow belong.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/GroupV2/Recommended/{groupType}/{createDateRange}/`
- **Operation ID:** `GroupV2.GetRecommendedGroups`
- **Tags:** GroupV2
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadGroups

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| createDateRange | integer (int32) | Yes | Requested range in which to pull recommended groups |
| groupType | integer (int32) | Yes | Type of groups requested |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/GroupsV2.GroupV2Card"
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
POST /GroupV2/Recommended/{groupType}/{createDateRange}/
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
- Gets groups recommended for you based on the groups to whom those you follow belong.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
