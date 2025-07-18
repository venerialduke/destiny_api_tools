# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoptionsettingscontrol data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| type | integer (int32) |  | No |
| minSelectedItems | integer (int32) |  | No |
| maxSelectedItems | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl object
const example = {
  type: 123,
  minSelectedItems: 123,
  maxSelectedItems: 123,
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl object
example = {
    "type": 123,
    "minSelectedItems": 123,
    "maxSelectedItems": 123,
}
```

## Related Entities
- **Destiny.FireteamFinderOptionControlType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl":   {
      "type": "object",
      "properties": {
          "type": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionControlType"
              }
          },
          "minSelectedItems": {
              "format": "int32",
              "type": "integer"
          },
          "maxSelectedItems": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
