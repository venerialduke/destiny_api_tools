# User.EMailSettingSubscriptionLocalization

## Entity Information
- **Entity Name**: User.EMailSettingSubscriptionLocalization
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Localized text relevant to a given EMail setting in a given localization. Extra settings specifically for subscriptions.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| unknownUserDescription | string |  | No |
| registeredUserDescription | string |  | No |
| unregisteredUserDescription | string |  | No |
| unknownUserActionText | string |  | No |
| knownUserActionText | string |  | No |
| title | string |  | No |
| description | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EMailSettingSubscriptionLocalization object
const example = {
  unknownUserDescription: "example value",
  registeredUserDescription: "example value",
  unregisteredUserDescription: "example value",
  unknownUserActionText: "example value",
  knownUserActionText: "example value",
  // ... more properties
};
```

### Python
```python
# Example User.EMailSettingSubscriptionLocalization object
example = {
    "unknownUserDescription": "example value",
    "registeredUserDescription": "example value",
    "unregisteredUserDescription": "example value",
    "unknownUserActionText": "example value",
    "knownUserActionText": "example value",
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EMailSettingSubscriptionLocalization":   {
      "description": "Localized text relevant to a given EMail setting in a given localization. Extra settings specifically for subscriptions.",
      "type": "object",
      "properties": {
          "unknownUserDescription": {
              "type": "string"
          },
          "registeredUserDescription": {
              "type": "string"
          },
          "unregisteredUserDescription": {
              "type": "string"
          },
          "unknownUserActionText": {
              "type": "string"
          },
          "knownUserActionText": {
              "type": "string"
          },
          "title": {
              "type": "string"
          },
          "description": {
              "type": "string"
          }
      }
  }
}
```
