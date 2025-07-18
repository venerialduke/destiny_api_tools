# App Getapplicationapiusage

## Overview
Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/App/ApiUsage/{applicationId}/`
- **Operation ID:** `App.GetApplicationApiUsage`
- **Tags:** App
- **Deprecated:** false

## Authentication
- **Required:** Yes\n- **Type:** OAuth2\n- **Permissions:** ReadUserData

## Parameters

### Path Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| applicationId | integer (int32) | Yes | ID of the application to get usage statistics. |

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| end | string (date-time) | No | End time for query. Goes to now if not specified. |
| start | string (date-time) | No | Start time for query. Goes to 24 hours ago if not specified. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "$ref": "#/definitions/Applications.ApiUsage"
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
GET /App/ApiUsage/{applicationId}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### With Query Parameters
```http
GET /App/ApiUsage/{applicationId}/?end=example_value&start=example_value
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
- Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
