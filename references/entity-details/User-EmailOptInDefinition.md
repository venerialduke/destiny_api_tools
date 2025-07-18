# User.EmailOptInDefinition

## Entity Information
- **Entity Name**: User.EmailOptInDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines a single opt-in category: a wide-scoped permission to send emails for the subject related to the opt-in.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string | The unique identifier for this opt-in category. | No |
| value | integer (int64) | The flag value for this opt-in category. For historical reasons, this is defined as a flags enum. | No |
| setByDefault | boolean | If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they're opting into. | No |
| dependentSubscriptions | Array[User.EmailSubscriptionDefinition] | Information about the dependent subscriptions for this opt-in. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EmailOptInDefinition object
const example = {
  name: "example value",
  value: 123,
  setByDefault: true,
  dependentSubscriptions: [],
};
```

### Python
```python
# Example User.EmailOptInDefinition object
example = {
    "name": "example value",
    "value": 123,
    "setByDefault": True,
    "dependentSubscriptions": [],
}
```

## Related Entities
- **User.EmailSubscriptionDefinition**: Referenced in this entity
- **User.OptInFlags**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EmailOptInDefinition":   {
      "description": "Defines a single opt-in category: a wide-scoped permission to send emails for the subject related to the opt-in.",
      "type": "object",
      "properties": {
          "name": {
              "description": "The unique identifier for this opt-in category.",
              "type": "string"
          },
          "value": {
              "format": "int64",
              "description": "The flag value for this opt-in category. For historical reasons, this is defined as a flags enum.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/User.OptInFlags"
              }
          },
          "setByDefault": {
              "description": "If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they're opting into.",
              "type": "boolean"
          },
          "dependentSubscriptions": {
              "description": "Information about the dependent subscriptions for this opt-in.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.EmailSubscriptionDefinition"
              }
          }
      }
  }
}
```
