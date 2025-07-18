# Destiny.Definitions.DestinyActivityUnlockStringDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityUnlockStringDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a status string that could be conditionally displayed about an activity. Note that externally, you can only see the strings themselves. Internally we combine this information with server state to determine which strings should be shown.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayString | string | The string to be displayed if the conditions are met. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityUnlockStringDefinition object
const example = {
  displayString: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityUnlockStringDefinition object
example = {
    "displayString": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityUnlockStringDefinition":   {
      "description": "Represents a status string that could be conditionally displayed about an activity. Note that externally, you can only see the strings themselves. Internally we combine this information with server state to determine which strings should be shown.",
      "type": "object",
      "properties": {
          "displayString": {
              "description": "The string to be displayed if the conditions are met.",
              "type": "string"
          }
      }
  }
}
```
