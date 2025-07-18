# GroupsV2.GroupNameSearchRequest

## Entity Information
- **Entity Name**: GroupsV2.GroupNameSearchRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupnamesearchrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupName | string |  | No |
| groupType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupNameSearchRequest object
const example = {
  groupName: "example value",
  groupType: 123,
};
```

### Python
```python
# Example GroupsV2.GroupNameSearchRequest object
example = {
    "groupName": "example value",
    "groupType": 123,
}
```

## Related Entities
- **GroupsV2.GroupType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupNameSearchRequest":   {
      "type": "object",
      "properties": {
          "groupName": {
              "type": "string"
          },
          "groupType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupType"
              }
          }
      }
  }
}
```
