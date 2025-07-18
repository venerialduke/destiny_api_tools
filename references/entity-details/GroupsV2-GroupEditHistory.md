# GroupsV2.GroupEditHistory

## Entity Information
- **Entity Name**: GroupsV2.GroupEditHistory
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupedithistory operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupId | integer (int64) |  | No |
| name | string |  | No |
| nameEditors | integer (int64) |  | No |
| about | string |  | No |
| aboutEditors | integer (int64) |  | No |
| motto | string |  | No |
| mottoEditors | integer (int64) |  | No |
| clanCallsign | string |  | No |
| clanCallsignEditors | integer (int64) |  | No |
| editDate | string (date-time) |  | No |
| groupEditors | Array[User.UserInfoCard] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupEditHistory object
const example = {
  groupId: 123,
  name: "example value",
  nameEditors: 123,
  about: "example value",
  aboutEditors: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupEditHistory object
example = {
    "groupId": 123,
    "name": "example value",
    "nameEditors": 123,
    "about": "example value",
    "aboutEditors": 123,
    # ... more properties
}
```

## Related Entities
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupEditHistory":   {
      "type": "object",
      "properties": {
          "groupId": {
              "format": "int64",
              "type": "integer"
          },
          "name": {
              "type": "string"
          },
          "nameEditors": {
              "format": "int64",
              "type": "integer"
          },
          "about": {
              "type": "string"
          },
          "aboutEditors": {
              "format": "int64",
              "type": "integer"
          },
          "motto": {
              "type": "string"
          },
          "mottoEditors": {
              "format": "int64",
              "type": "integer"
          },
          "clanCallsign": {
              "type": "string"
          },
          "clanCallsignEditors": {
              "format": "int64",
              "type": "integer"
          },
          "editDate": {
              "format": "date-time",
              "type": "string"
          },
          "groupEditors": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.UserInfoCard"
              }
          }
      }
  }
}
```
