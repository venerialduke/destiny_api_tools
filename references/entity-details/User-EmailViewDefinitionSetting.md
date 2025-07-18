# User.EmailViewDefinitionSetting

## Entity Information
- **Entity Name**: User.EmailViewDefinitionSetting
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for emailviewdefinitionsetting operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string | The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired. | No |
| localization | object | A dictionary of localized text for the EMail setting, keyed by the locale. | No |
| setByDefault | boolean | If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet. | No |
| optInAggregateValue | integer (int64) | The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting. | No |
| subscriptions | Array[User.EmailSubscriptionDefinition] | The subscriptions to show as children of this setting, if any. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EmailViewDefinitionSetting object
const example = {
  name: "example value",
  localization: null,
  setByDefault: true,
  optInAggregateValue: 123,
  subscriptions: [],
};
```

### Python
```python
# Example User.EmailViewDefinitionSetting object
example = {
    "name": "example value",
    "localization": None,
    "setByDefault": True,
    "optInAggregateValue": 123,
    "subscriptions": [],
}
```

## Related Entities
- **User.EMailSettingLocalization**: Referenced in this entity
- **User.EmailSubscriptionDefinition**: Referenced in this entity
- **User.OptInFlags**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EmailViewDefinitionSetting":   {
      "type": "object",
      "properties": {
          "name": {
              "description": "The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired.",
              "type": "string"
          },
          "localization": {
              "description": "A dictionary of localized text for the EMail setting, keyed by the locale.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/User.EMailSettingLocalization"
              }
          },
          "setByDefault": {
              "description": "If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.",
              "type": "boolean"
          },
          "optInAggregateValue": {
              "format": "int64",
              "description": "The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/User.OptInFlags"
              }
          },
          "subscriptions": {
              "description": "The subscriptions to show as children of this setting, if any.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.EmailSubscriptionDefinition"
              }
          }
      }
  }
}
```
