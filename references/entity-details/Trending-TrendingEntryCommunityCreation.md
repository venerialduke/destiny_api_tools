# Trending.TrendingEntryCommunityCreation

## Entity Information
- **Entity Name**: Trending.TrendingEntryCommunityCreation
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for trendingentrycommunitycreation operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| media | string |  | No |
| title | string |  | No |
| author | string |  | No |
| authorMembershipId | integer (int64) |  | No |
| postId | integer (int64) |  | No |
| body | string |  | No |
| upvotes | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntryCommunityCreation object
const example = {
  media: "example value",
  title: "example value",
  author: "example value",
  authorMembershipId: 123,
  postId: 123,
  // ... more properties
};
```

### Python
```python
# Example Trending.TrendingEntryCommunityCreation object
example = {
    "media": "example value",
    "title": "example value",
    "author": "example value",
    "authorMembershipId": 123,
    "postId": 123,
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Trending.TrendingEntryCommunityCreation":   {
      "type": "object",
      "properties": {
          "media": {
              "type": "string"
          },
          "title": {
              "type": "string"
          },
          "author": {
              "type": "string"
          },
          "authorMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "postId": {
              "format": "int64",
              "type": "integer"
          },
          "body": {
              "type": "string"
          },
          "upvotes": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
