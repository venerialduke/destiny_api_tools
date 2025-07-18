# Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemtiertypeinfusionblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| baseQualityTransferRatio | number (float) | The default portion of quality that will transfer from the infuser to the infusee item. (InfuserQuality - InfuseeQuality) * baseQualityTransferRatio = base quality transferred. | No |
| minimumQualityIncrement | integer (int32) | As long as InfuserQuality > InfuseeQuality, the amount of quality bestowed is guaranteed to be at least this value, even if the transferRatio would dictate that it should be less. The total amount of quality that ends up in the Infusee cannot exceed the Infuser's quality however (for instance, if you infuse a 300 item with a 301 item and the minimum quality increment is 10, the infused item will not end up with 310 quality) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock object
const example = {
  baseQualityTransferRatio: 123.45,
  minimumQualityIncrement: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock object
example = {
    "baseQualityTransferRatio": 123.45,
    "minimumQualityIncrement": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock":   {
      "type": "object",
      "properties": {
          "baseQualityTransferRatio": {
              "format": "float",
              "description": "The default portion of quality that will transfer from the infuser to the infusee item. (InfuserQuality - InfuseeQuality) * baseQualityTransferRatio = base quality transferred.",
              "type": "number"
          },
          "minimumQualityIncrement": {
              "format": "int32",
              "description": "As long as InfuserQuality > InfuseeQuality, the amount of quality bestowed is guaranteed to be at least this value, even if the transferRatio would dictate that it should be less. The total amount of quality that ends up in the Infusee cannot exceed the Infuser's quality however (for instance, if you infuse a 300 item with a 301 item and the minimum quality increment is 10, the infused item will not end up with 310 quality)",
              "type": "integer"
          }
      }
  }
}
```
