# Forum.ForumRecruitmentDetail

## Entity Information
- **Entity Name**: Forum.ForumRecruitmentDetail
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for forumrecruitmentdetail operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| topicId | integer (int64) |  | No |
| microphoneRequired | boolean |  | No |
| intensity | integer (byte) |  | No |
| tone | integer (byte) |  | No |
| approved | boolean |  | No |
| conversationId | integer (int64) |  | No |
| playerSlotsTotal | integer (int32) |  | No |
| playerSlotsRemaining | integer (int32) |  | No |
| Fireteam | Array[User.GeneralUser] |  | No |
| kickedPlayerIds | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Forum.ForumRecruitmentDetail object
const example = {
  topicId: 123,
  microphoneRequired: true,
  intensity: 123,
  tone: 123,
  approved: true,
  // ... more properties
};
```

### Python
```python
# Example Forum.ForumRecruitmentDetail object
example = {
    "topicId": 123,
    "microphoneRequired": True,
    "intensity": 123,
    "tone": 123,
    "approved": True,
    # ... more properties
}
```

## Related Entities
- **Forum.ForumRecruitmentIntensityLabel**: Referenced in this entity
- **Forum.ForumRecruitmentToneLabel**: Referenced in this entity
- **User.GeneralUser**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Forum.ForumRecruitmentDetail":   {
      "type": "object",
      "properties": {
          "topicId": {
              "format": "int64",
              "type": "integer"
          },
          "microphoneRequired": {
              "type": "boolean"
          },
          "intensity": {
              "format": "byte",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Forum.ForumRecruitmentIntensityLabel"
              }
          },
          "tone": {
              "format": "byte",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Forum.ForumRecruitmentToneLabel"
              }
          },
          "approved": {
              "type": "boolean"
          },
          "conversationId": {
              "format": "int64",
              "type": "integer"
          },
          "playerSlotsTotal": {
              "format": "int32",
              "type": "integer"
          },
          "playerSlotsRemaining": {
              "format": "int32",
              "type": "integer"
          },
          "Fireteam": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.GeneralUser"
              }
          },
          "kickedPlayerIds": {
              "type": "array",
              "items": {
                  "format": "int64",
                  "type": "integer"
              }
          }
      }
  }
}
```
