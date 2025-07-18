# Tokens.UserRewardAvailabilityModel

## Entity Information
- **Entity Name**: Tokens.UserRewardAvailabilityModel
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for userrewardavailabilitymodel operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| AvailabilityModel | Tokens.RewardAvailabilityModel |  | No |
| IsAvailableForUser | boolean |  | No |
| IsUnlockedForUser | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.UserRewardAvailabilityModel object
const example = {
  AvailabilityModel: null,
  IsAvailableForUser: true,
  IsUnlockedForUser: true,
};
```

### Python
```python
# Example Tokens.UserRewardAvailabilityModel object
example = {
    "AvailabilityModel": None,
    "IsAvailableForUser": True,
    "IsUnlockedForUser": True,
}
```

## Related Entities
- **Tokens.RewardAvailabilityModel**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.UserRewardAvailabilityModel":   {
      "type": "object",
      "properties": {
          "AvailabilityModel": {
              "$ref": "#/definitions/Tokens.RewardAvailabilityModel"
          },
          "IsAvailableForUser": {
              "type": "boolean"
          },
          "IsUnlockedForUser": {
              "type": "boolean"
          }
      }
  }
}
```
