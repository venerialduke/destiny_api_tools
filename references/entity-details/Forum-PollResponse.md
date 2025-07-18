# Forum.PollResponse

## Entity Information
- **Entity Name**: Forum.PollResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for pollresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| topicId | integer (int64) |  | No |
| results | Array[Forum.PollResult] |  | No |
| totalVotes | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Forum.PollResponse object
const example = {
  topicId: 123,
  results: [],
  totalVotes: 123,
};
```

### Python
```python
# Example Forum.PollResponse object
example = {
    "topicId": 123,
    "results": [],
    "totalVotes": 123,
}
```

## Related Entities
- **Forum.PollResult**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Forum.PollResponse":   {
      "type": "object",
      "properties": {
          "topicId": {
              "format": "int64",
              "type": "integer"
          },
          "results": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Forum.PollResult"
              }
          },
          "totalVotes": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
