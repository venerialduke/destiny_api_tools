# Tokens.BungieRewardDisplay

## Entity Information
- **Entity Name**: Tokens.BungieRewardDisplay
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for bungierewarddisplay operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| UserRewardAvailabilityModel | Tokens.UserRewardAvailabilityModel |  | No |
| ObjectiveDisplayProperties | Tokens.RewardDisplayProperties |  | No |
| RewardDisplayProperties | Tokens.RewardDisplayProperties |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.BungieRewardDisplay object
const example = {
  UserRewardAvailabilityModel: null,
  ObjectiveDisplayProperties: null,
  RewardDisplayProperties: null,
};
```

### Python
```python
# Example Tokens.BungieRewardDisplay object
example = {
    "UserRewardAvailabilityModel": None,
    "ObjectiveDisplayProperties": None,
    "RewardDisplayProperties": None,
}
```

## Related Entities
- **Tokens.RewardDisplayProperties**: Referenced in this entity
- **Tokens.UserRewardAvailabilityModel**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.BungieRewardDisplay":   {
      "type": "object",
      "properties": {
          "UserRewardAvailabilityModel": {
              "$ref": "#/definitions/Tokens.UserRewardAvailabilityModel"
          },
          "ObjectiveDisplayProperties": {
              "$ref": "#/definitions/Tokens.RewardDisplayProperties"
          },
          "RewardDisplayProperties": {
              "$ref": "#/definitions/Tokens.RewardDisplayProperties"
          }
      }
  }
}
```
