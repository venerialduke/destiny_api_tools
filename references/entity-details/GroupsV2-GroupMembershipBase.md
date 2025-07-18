# GroupsV2.GroupMembershipBase

## Entity Information
- **Entity Name**: GroupsV2.GroupMembershipBase
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupmembershipbase operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| group | GroupsV2.GroupV2 |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupMembershipBase object
const example = {
  group: null,
};
```

### Python
```python
# Example GroupsV2.GroupMembershipBase object
example = {
    "group": None,
}
```

## Related Entities
- **GroupsV2.GroupV2**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupMembershipBase":   {
      "type": "object",
      "properties": {
          "group": {
              "$ref": "#/definitions/GroupsV2.GroupV2"
          }
      }
  }
}
```
