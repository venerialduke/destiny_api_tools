# Destiny.Requests.Actions.DestinyActionRequest

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyActionRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactionrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyActionRequest object
const example = {
  membershipType: 123,
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyActionRequest object
example = {
    "membershipType": 123,
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Requests.Actions.DestinyActionRequest":   {
      "type": "object",
      "properties": {
          "membershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          }
      }
  }
}
```
