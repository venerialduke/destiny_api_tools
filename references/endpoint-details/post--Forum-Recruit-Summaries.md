# Forum Getrecruitmentthreadsummaries

## Overview
Allows the caller to get a list of to 25 recruitment thread summary information objects.

## Endpoint Details
- **HTTP Method:** POST
- **Path:** `/Forum/Recruit/Summaries/`
- **Operation ID:** `Forum.GetRecruitmentThreadSummaries`
- **Tags:** Forum
- **Deprecated:** false

## Authentication
- **Required:** No\n- **Permissions:** None

## Parameters

This endpoint does not require any parameters.

## Response Schema

### Success Response (200)
```json
{
  "type": "object",
  "properties": {
    "Response": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Forum.ForumRecruitmentDetail"
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
POST /Forum/Recruit/Summaries/
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
- Allows the caller to get a list of to 25 recruitment thread summary information objects.
- Response follows the standard Bungie API format with Response, ErrorCode, ThrottleSeconds, etc.
