# User.EmailSettings

## Entity Information
- **Entity Name**: User.EmailSettings
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The set of all email subscription/opt-in settings and definitions.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| optInDefinitions | object | Keyed by the name identifier of the opt-in definition. | No |
| subscriptionDefinitions | object | Keyed by the name identifier of the Subscription definition. | No |
| views | object | Keyed by the name identifier of the View definition. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EmailSettings object
const example = {
  optInDefinitions: null,
  subscriptionDefinitions: null,
  views: null,
};
```

### Python
```python
# Example User.EmailSettings object
example = {
    "optInDefinitions": None,
    "subscriptionDefinitions": None,
    "views": None,
}
```

## Related Entities
- **User.EmailOptInDefinition**: Referenced in this entity
- **User.EmailSubscriptionDefinition**: Referenced in this entity
- **User.EmailViewDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EmailSettings":   {
      "description": "The set of all email subscription/opt-in settings and definitions.",
      "type": "object",
      "properties": {
          "optInDefinitions": {
              "description": "Keyed by the name identifier of the opt-in definition.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/User.EmailOptInDefinition"
              }
          },
          "subscriptionDefinitions": {
              "description": "Keyed by the name identifier of the Subscription definition.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/User.EmailSubscriptionDefinition"
              }
          },
          "views": {
              "description": "Keyed by the name identifier of the View definition.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/User.EmailViewDefinition"
              }
          }
      }
  }
}
```
