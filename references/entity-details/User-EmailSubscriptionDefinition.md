# User.EmailSubscriptionDefinition

## Entity Information
- **Entity Name**: User.EmailSubscriptionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines a single subscription: permission to send emails for a specific, focused subject (generally timeboxed, such as for a specific release of a product or feature).

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string | The unique identifier for this subscription. | No |
| localization | object | A dictionary of localized text for the EMail Opt-in setting, keyed by the locale. | No |
| value | integer (int64) | The bitflag value for this subscription. Should be a unique power of two value. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EmailSubscriptionDefinition object
const example = {
  name: "example value",
  localization: null,
  value: 123,
};
```

### Python
```python
# Example User.EmailSubscriptionDefinition object
example = {
    "name": "example value",
    "localization": None,
    "value": 123,
}
```

## Related Entities
- **User.EMailSettingSubscriptionLocalization**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EmailSubscriptionDefinition":   {
      "description": "Defines a single subscription: permission to send emails for a specific, focused subject (generally timeboxed, such as for a specific release of a product or feature).",
      "type": "object",
      "properties": {
          "name": {
              "description": "The unique identifier for this subscription.",
              "type": "string"
          },
          "localization": {
              "description": "A dictionary of localized text for the EMail Opt-in setting, keyed by the locale.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/User.EMailSettingSubscriptionLocalization"
              }
          },
          "value": {
              "format": "int64",
              "description": "The bitflag value for this subscription. Should be a unique power of two value.",
              "type": "integer"
          }
      }
  }
}
```
