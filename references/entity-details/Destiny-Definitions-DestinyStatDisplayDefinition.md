# Destiny.Definitions.DestinyStatDisplayDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyStatDisplayDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Describes the way that an Item Stat (see DestinyStatDefinition) is transformed using the DestinyStatGroupDefinition related to that item. See both of the aforementioned definitions for more information about the stages of stat transformation.
This represents the transformation of a stat into a "Display" stat (the closest value that BNet can get to the in-game display value of the stat)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statHash | integer (uint32) | The hash identifier for the stat being transformed into a Display stat.
Use it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition's stats property. | No |
| maximumValue | integer (int32) | Regardless of the output of interpolation, this is the maximum possible value that the stat can be. It should also be used as the upper bound for displaying the stat as a progress bar (the minimum always being 0) | No |
| displayAsNumeric | boolean | If this is true, the stat should be displayed as a number. Otherwise, display it as a progress bar. Or, you know, do whatever you want. There's no displayAsNumeric police. | No |
| displayInterpolation | Array[Interpolation.InterpolationPoint] | The interpolation table representing how the Investment Stat is transformed into a Display Stat. 
See DestinyStatDefinition for a description of the stages of stat transformation. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyStatDisplayDefinition object
const example = {
  statHash: 123,
  maximumValue: 123,
  displayAsNumeric: true,
  displayInterpolation: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyStatDisplayDefinition object
example = {
    "statHash": 123,
    "maximumValue": 123,
    "displayAsNumeric": True,
    "displayInterpolation": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity
- **Interpolation.InterpolationPoint**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyStatDisplayDefinition":   {
      "description": "Describes the way that an Item Stat (see DestinyStatDefinition) is transformed using the DestinyStatGroupDefinition related to that item. See both of the aforementioned definitions for more information about the stages of stat transformation.\r\nThis represents the transformation of a stat into a \"Display\" stat (the closest value that BNet can get to the in-game display value of the stat)",
      "type": "object",
      "properties": {
          "statHash": {
              "format": "uint32",
              "description": "The hash identifier for the stat being transformed into a Display stat.\r\nUse it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition's stats property.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "maximumValue": {
              "format": "int32",
              "description": "Regardless of the output of interpolation, this is the maximum possible value that the stat can be. It should also be used as the upper bound for displaying the stat as a progress bar (the minimum always being 0)",
              "type": "integer"
          },
          "displayAsNumeric": {
              "description": "If this is true, the stat should be displayed as a number. Otherwise, display it as a progress bar. Or, you know, do whatever you want. There's no displayAsNumeric police.",
              "type": "boolean"
          },
          "displayInterpolation": {
              "description": "The interpolation table representing how the Investment Stat is transformed into a Display Stat. \r\nSee DestinyStatDefinition for a description of the stages of stat transformation.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Interpolation.InterpolationPoint"
              }
          }
      }
  }
}
```
