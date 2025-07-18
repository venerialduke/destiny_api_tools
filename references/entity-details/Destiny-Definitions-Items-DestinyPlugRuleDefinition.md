# Destiny.Definitions.Items.DestinyPlugRuleDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyPlugRuleDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Dictates a rule around whether the plug is enabled or insertable.
In practice, the live Destiny data will refer to these entries by index. You can then look up that index in the appropriate property (enabledRules or insertionRules) to get the localized string for the failure message if it failed.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| failureMessage | string | The localized string to show if this rule fails. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyPlugRuleDefinition object
const example = {
  failureMessage: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyPlugRuleDefinition object
example = {
    "failureMessage": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyPlugRuleDefinition":   {
      "description": "Dictates a rule around whether the plug is enabled or insertable.\r\nIn practice, the live Destiny data will refer to these entries by index. You can then look up that index in the appropriate property (enabledRules or insertionRules) to get the localized string for the failure message if it failed.",
      "type": "object",
      "properties": {
          "failureMessage": {
              "description": "The localized string to show if this rule fails.",
              "type": "string"
          }
      }
  }
}
```
