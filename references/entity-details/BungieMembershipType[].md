# BungieMembershipType[]

## Entity Information
- **Entity Name**: BungieMembershipType[]
- **Entity Type**: Schema (array)
- **Base Type**: array

## Description
API entity for bungiemembershiptype[] operations.

## Usage Examples

### JavaScript
```javascript
```

### Python
```python
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- No additional notes for this entity.

## JSON Schema
```json
{
  "BungieMembershipType[]":   {
      "type": "array",
      "items": {
          "format": "int32",
          "description": "The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.",
          "type": "integer",
          "x-enum-reference": {
              "$ref": "#/components/schemas/BungieMembershipType"
          }
      }
  }
}
```
