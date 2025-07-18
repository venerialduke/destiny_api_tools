# Content.CommentSummary

## Entity Information
- **Entity Name**: Content.CommentSummary
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for commentsummary operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| topicId | integer (int64) |  | No |
| commentCount | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.CommentSummary object
const example = {
  topicId: 123,
  commentCount: 123,
};
```

### Python
```python
# Example Content.CommentSummary object
example = {
    "topicId": 123,
    "commentCount": 123,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.CommentSummary":   {
      "type": "object",
      "properties": {
          "topicId": {
              "format": "int64",
              "type": "integer"
          },
          "commentCount": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
