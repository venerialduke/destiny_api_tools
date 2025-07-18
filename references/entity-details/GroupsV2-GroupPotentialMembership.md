# GroupsV2.GroupPotentialMembership

## Entity Information
- **Entity Name**: GroupsV2.GroupPotentialMembership
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for grouppotentialmembership operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| member | GroupsV2.GroupPotentialMember |  | No |
| group | GroupsV2.GroupV2 |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupPotentialMembership object
const example = {
  member: null,
  group: null,
};
```

### Python
```python
# Example GroupsV2.GroupPotentialMembership object
example = {
    "member": None,
    "group": None,
}
```

## Related Entities
- **GroupsV2.GroupPotentialMember**: Referenced in this entity
- **GroupsV2.GroupV2**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupPotentialMembership":   {
      "type": "object",
      "properties": {
          "member": {
              "$ref": "#/definitions/GroupsV2.GroupPotentialMember"
          },
          "group": {
              "$ref": "#/definitions/GroupsV2.GroupV2"
          }
      }
  }
}
```
