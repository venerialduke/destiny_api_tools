# Destiny.Definitions.DestinyItemTooltipNotification

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemTooltipNotification
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemtooltipnotification data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayString | string |  | No |
| displayStyle | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemTooltipNotification object
const example = {
  displayString: "example value",
  displayStyle: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemTooltipNotification object
example = {
    "displayString": "example value",
    "displayStyle": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemTooltipNotification":   {
      "type": "object",
      "properties": {
          "displayString": {
              "type": "string"
          },
          "displayStyle": {
              "type": "string"
          }
      }
  }
}
```
