# Forum.PollResult

## Entity Information
- **Entity Name**: Forum.PollResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for pollresult operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| answerText | string |  | No |
| answerSlot | integer (int32) |  | No |
| lastVoteDate | string (date-time) |  | No |
| votes | integer (int32) |  | No |
| requestingUserVoted | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Forum.PollResult object
const example = {
  answerText: "example value",
  answerSlot: 123,
  lastVoteDate: "example value",
  votes: 123,
  requestingUserVoted: true,
};
```

### Python
```python
# Example Forum.PollResult object
example = {
    "answerText": "example value",
    "answerSlot": 123,
    "lastVoteDate": "example value",
    "votes": 123,
    "requestingUserVoted": True,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Forum.PollResult":   {
      "type": "object",
      "properties": {
          "answerText": {
              "type": "string"
          },
          "answerSlot": {
              "format": "int32",
              "type": "integer"
          },
          "lastVoteDate": {
              "format": "date-time",
              "type": "string"
          },
          "votes": {
              "format": "int32",
              "type": "integer"
          },
          "requestingUserVoted": {
              "type": "boolean"
          }
      }
  }
}
```
