# Destiny.Components.Inventory.DestinyPlatformSilverComponent

## Entity Information
- **Entity Name**: Destiny.Components.Inventory.DestinyPlatformSilverComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyplatformsilvercomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| platformSilver | object | If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Inventory.DestinyPlatformSilverComponent object
const example = {
  platformSilver: null,
};
```

### Python
```python
# Example Destiny.Components.Inventory.DestinyPlatformSilverComponent object
example = {
    "platformSilver": None,
}
```

## Related Entities
- **Destiny.Entities.Items.DestinyItemComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Inventory.DestinyPlatformSilverComponent":   {
      "type": "object",
      "properties": {
          "platformSilver": {
              "description": "If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemComponent"
              }
          }
      },
      "x-destiny-component-type-dependency": "PlatformSilver"
  }
}
```
