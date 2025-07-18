# Destiny.Advanced.AwaPermissionRequested

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaPermissionRequested
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing awapermissionrequested data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| type | integer (int32) | Type of advanced write action. | No |
| affectedItemId | integer (int64) | Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available. | No |
| membershipType | integer (int32) | Destiny membership type of the account to modify. | No |
| characterId | integer (int64) | Destiny character ID, if applicable, that will be affected by the action. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Advanced.AwaPermissionRequested object
const example = {
  type: 123,
  affectedItemId: 123,
  membershipType: 123,
  characterId: 123,
};
```

### Python
```python
# Example Destiny.Advanced.AwaPermissionRequested object
example = {
    "type": 123,
    "affectedItemId": 123,
    "membershipType": 123,
    "characterId": 123,
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Advanced.AwaType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaPermissionRequested":   {
      "type": "object",
      "properties": {
          "type": {
              "format": "int32",
              "description": "Type of advanced write action.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Advanced.AwaType"
              }
          },
          "affectedItemId": {
              "format": "int64",
              "description": "Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available.",
              "type": "integer"
          },
          "membershipType": {
              "format": "int32",
              "description": "Destiny membership type of the account to modify.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "characterId": {
              "format": "int64",
              "description": "Destiny character ID, if applicable, that will be affected by the action.",
              "type": "integer"
          }
      }
  }
}
```
