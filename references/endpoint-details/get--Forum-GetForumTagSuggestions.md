# Forum Getforumtagsuggestions

## Overview
Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

## Endpoint Details
- **HTTP Method:** GET
- **Path:** `/Forum/GetForumTagSuggestions/`
- **Operation ID:** `Forum.GetForumTagSuggestions`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| partialtag | string | No | The partial tag input to generate suggestions from. |


## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Tags.Models.Contracts.TagResponse"
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
GET /Forum/GetForumTagSuggestions/
```

### With Query Parameters
```http
GET /Forum/GetForumTagSuggestions/?partialtag=example_value
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
- Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
