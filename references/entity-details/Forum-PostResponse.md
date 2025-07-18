# Forum.PostResponse

## Entity Information
- **Entity Name**: Forum.PostResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for postresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lastReplyTimestamp | string (date-time) |  | No |
| IsPinned | boolean |  | No |
| urlMediaType | integer (int32) |  | No |
| thumbnail | string |  | No |
| popularity | integer (int32) |  | No |
| isActive | boolean |  | No |
| isAnnouncement | boolean |  | No |
| userRating | integer (int32) |  | No |
| userHasRated | boolean |  | No |
| userHasMutedPost | boolean |  | No |
| latestReplyPostId | integer (int64) |  | No |
| latestReplyAuthorId | integer (int64) |  | No |
| ignoreStatus | Ignores.IgnoreResponse |  | No |
| locale | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Forum.PostResponse object
const example = {
  lastReplyTimestamp: "example value",
  IsPinned: true,
  urlMediaType: 123,
  thumbnail: "example value",
  popularity: 123,
  // ... more properties
};
```

### Python
```python
# Example Forum.PostResponse object
example = {
    "lastReplyTimestamp": "example value",
    "IsPinned": True,
    "urlMediaType": 123,
    "thumbnail": "example value",
    "popularity": 123,
    # ... more properties
}
```

## Related Entities
- **Forum.ForumMediaType**: Referenced in this entity
- **Forum.ForumPostPopularity**: Referenced in this entity
- **Ignores.IgnoreResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Forum.PostResponse":   {
      "type": "object",
      "properties": {
          "lastReplyTimestamp": {
              "format": "date-time",
              "type": "string"
          },
          "IsPinned": {
              "type": "boolean"
          },
          "urlMediaType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Forum.ForumMediaType"
              }
          },
          "thumbnail": {
              "type": "string"
          },
          "popularity": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Forum.ForumPostPopularity"
              }
          },
          "isActive": {
              "type": "boolean"
          },
          "isAnnouncement": {
              "type": "boolean"
          },
          "userRating": {
              "format": "int32",
              "type": "integer"
          },
          "userHasRated": {
              "type": "boolean"
          },
          "userHasMutedPost": {
              "type": "boolean"
          },
          "latestReplyPostId": {
              "format": "int64",
              "type": "integer"
          },
          "latestReplyAuthorId": {
              "format": "int64",
              "type": "integer"
          },
          "ignoreStatus": {
              "$ref": "#/definitions/Ignores.IgnoreResponse"
          },
          "locale": {
              "type": "string"
          }
      }
  }
}
```
