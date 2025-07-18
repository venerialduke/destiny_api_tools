# Destiny.Definitions.Activities.DestinyActivitySkull

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivitySkull
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityskull data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| hash | integer (uint32) |  | No |
| skullIdentifierHash | integer (uint32) |  | No |
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| skullOptions | Array[Destiny.Definitions.Activities.DestinyActivitySkullOption] |  | No |
| dynamicUse | integer (int32) |  | No |
| modifierPowerContribution | integer (int32) |  | No |
| modifierMultiplierContribution | number (float) |  | No |
| skullExclusionGroupHash | integer (uint32) |  | No |
| hasUi | boolean |  | No |
| displayDescriptionOverrideForNavMode | string |  | No |
| activityModifierDisplayCategory | integer (int32) |  | No |
| activityModifierConnotation | integer (int32) |  | No |
| displayInNavMode | boolean |  | No |
| displayInActivitySelection | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivitySkull object
const example = {
  hash: 123,
  skullIdentifierHash: 123,
  displayProperties: null,
  skullOptions: [],
  dynamicUse: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivitySkull object
example = {
    "hash": 123,
    "skullIdentifierHash": 123,
    "displayProperties": None,
    "skullOptions": [],
    "dynamicUse": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Activities.DestinyActivitySelectableSkullExclusionGroupDefinition**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySkullOption**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.DestinyActivityModifierConnotation**: Referenced in this entity
- **Destiny.DestinyActivityModifierDisplayCategory**: Referenced in this entity
- **Destiny.DestinyActivitySkullDynamicUse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivitySkull":   {
      "type": "object",
      "properties": {
          "hash": {
              "format": "uint32",
              "type": "integer"
          },
          "skullIdentifierHash": {
              "format": "uint32",
              "type": "integer"
          },
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "skullOptions": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySkullOption"
              }
          },
          "dynamicUse": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivitySkullDynamicUse"
              }
          },
          "modifierPowerContribution": {
              "format": "int32",
              "type": "integer"
          },
          "modifierMultiplierContribution": {
              "format": "float",
              "type": "number"
          },
          "skullExclusionGroupHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySelectableSkullExclusionGroupDefinition"
              }
          },
          "hasUi": {
              "type": "boolean"
          },
          "displayDescriptionOverrideForNavMode": {
              "type": "string"
          },
          "activityModifierDisplayCategory": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityModifierDisplayCategory"
              }
          },
          "activityModifierConnotation": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityModifierConnotation"
              }
          },
          "displayInNavMode": {
              "type": "boolean"
          },
          "displayInActivitySelection": {
              "type": "boolean"
          }
      }
  }
}
```
