# GroupsV2.GroupMembership

## Entity Information
- **Entity Name**: GroupsV2.GroupMembership
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupmembership operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| member | GroupsV2.GroupMember |  | No |
| group | GroupsV2.GroupV2 |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupMembership object
const example = {
  member: null,
  group: null,
};
```

### Python
```python
# Example GroupsV2.GroupMembership object
example = {
    "member": None,
    "group": None,
}
```

## Related Entities
- **GroupsV2.GroupMember**: Referenced in this entity
- **GroupsV2.GroupV2**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupMembership":   {
      "type": "object",
      "properties": {
          "member": {
              "$ref": "#/definitions/GroupsV2.GroupMember"
          },
          "group": {
              "$ref": "#/definitions/GroupsV2.GroupV2"
          }
      }
  }
}
```
