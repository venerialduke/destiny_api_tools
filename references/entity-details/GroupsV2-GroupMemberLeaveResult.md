# GroupsV2.GroupMemberLeaveResult

## Entity Information
- **Entity Name**: GroupsV2.GroupMemberLeaveResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupmemberleaveresult operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| group | GroupsV2.GroupV2 |  | No |
| groupDeleted | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupMemberLeaveResult object
const example = {
  group: null,
  groupDeleted: true,
};
```

### Python
```python
# Example GroupsV2.GroupMemberLeaveResult object
example = {
    "group": None,
    "groupDeleted": True,
}
```

## Related Entities
- **GroupsV2.GroupV2**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupMemberLeaveResult":   {
      "type": "object",
      "properties": {
          "group": {
              "$ref": "#/definitions/GroupsV2.GroupV2"
          },
          "groupDeleted": {
              "type": "boolean"
          }
      }
  }
}
```
