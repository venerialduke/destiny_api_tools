# Destiny.Definitions.DestinyProgressionStepDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyProgressionStepDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This defines a single Step in a progression (which roughly equates to a level. See DestinyProgressionDefinition for caveats).

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| stepName | string | Very rarely, Progressions will have localized text describing the Level of the progression. This will be that localized text, if it exists. Otherwise, the standard appears to be to simply show the level numerically. | No |
| displayEffectType | integer (int32) | This appears to be, when you "level up", whether a visual effect will display and on what entity. See DestinyProgressionStepDisplayEffect for slightly more info. | No |
| progressTotal | integer (int32) | The total amount of progression points/"experience" you will need to initially reach this step. If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep), this will also be the progress needed to level it up further by repeating this step again. | No |
| rewardItems | Array[Destiny.DestinyItemQuantity] | A listing of items rewarded as a result of reaching this level. | No |
| icon | string | If this progression step has a specific icon related to it, this is the icon to show. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyProgressionStepDefinition object
const example = {
  stepName: "example value",
  displayEffectType: 123,
  progressTotal: 123,
  rewardItems: [],
  icon: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyProgressionStepDefinition object
example = {
    "stepName": "example value",
    "displayEffectType": 123,
    "progressTotal": 123,
    "rewardItems": [],
    "icon": "example value",
}
```

## Related Entities
- **Destiny.DestinyItemQuantity**: Referenced in this entity
- **Destiny.DestinyProgressionStepDisplayEffect**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyProgressionStepDefinition":   {
      "description": "This defines a single Step in a progression (which roughly equates to a level. See DestinyProgressionDefinition for caveats).",
      "type": "object",
      "properties": {
          "stepName": {
              "description": "Very rarely, Progressions will have localized text describing the Level of the progression. This will be that localized text, if it exists. Otherwise, the standard appears to be to simply show the level numerically.",
              "type": "string"
          },
          "displayEffectType": {
              "format": "int32",
              "description": "This appears to be, when you \"level up\", whether a visual effect will display and on what entity. See DestinyProgressionStepDisplayEffect for slightly more info.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyProgressionStepDisplayEffect"
              }
          },
          "progressTotal": {
              "format": "int32",
              "description": "The total amount of progression points/\"experience\" you will need to initially reach this step. If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep), this will also be the progress needed to level it up further by repeating this step again.",
              "type": "integer"
          },
          "rewardItems": {
              "description": "A listing of items rewarded as a result of reaching this level.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          },
          "icon": {
              "description": "If this progression step has a specific icon related to it, this is the icon to show.",
              "type": "string"
          }
      }
  }
}
```
