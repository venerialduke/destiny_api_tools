# Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Represents types of Energy that can be used for costs and payments related to Armor 2.0 mods.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | The description of the energy type, icon etc... | No |
| transparentIconPath | string | A variant of the icon that is transparent and colorless. | No |
| showIcon | boolean | If TRUE, the game shows this Energy type's icon. Otherwise, it doesn't. Whether you show it or not is up to you. | No |
| enumValue | integer (int32) | We have an enumeration for Energy types for quick reference. This is the current definition's Energy type enum value. | No |
| capacityStatHash | integer (uint32) | If this Energy Type can be used for determining the Type of Energy that an item can consume, this is the hash for the DestinyInvestmentStatDefinition that represents the stat which holds the Capacity for that energy type. (Note that this is optional because "Any" is a valid cost, but not valid for Capacity - an Armor must have a specific Energy Type for determining the energy type that the Armor is restricted to use) | No |
| costStatHash | integer (uint32) | If this Energy Type can be used as a cost to pay for socketing Armor 2.0 items, this is the hash for the DestinyInvestmentStatDefinition that stores the plug's raw cost. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition object
const example = {
  displayProperties: null,
  transparentIconPath: "example value",
  showIcon: true,
  enumValue: 123,
  capacityStatHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition object
example = {
    "displayProperties": None,
    "transparentIconPath": "example value",
    "showIcon": True,
    "enumValue": 123,
    "capacityStatHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity
- **Destiny.DestinyEnergyType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition":   {
      "description": "Represents types of Energy that can be used for costs and payments related to Armor 2.0 mods.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "The description of the energy type, icon etc...",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "transparentIconPath": {
              "description": "A variant of the icon that is transparent and colorless.",
              "type": "string"
          },
          "showIcon": {
              "description": "If TRUE, the game shows this Energy type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.",
              "type": "boolean"
          },
          "enumValue": {
              "format": "int32",
              "description": "We have an enumeration for Energy types for quick reference. This is the current definition's Energy type enum value.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyEnergyType"
              }
          },
          "capacityStatHash": {
              "format": "uint32",
              "description": "If this Energy Type can be used for determining the Type of Energy that an item can consume, this is the hash for the DestinyInvestmentStatDefinition that represents the stat which holds the Capacity for that energy type. (Note that this is optional because \"Any\" is a valid cost, but not valid for Capacity - an Armor must have a specific Energy Type for determining the energy type that the Armor is restricted to use)",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "costStatHash": {
              "format": "uint32",
              "description": "If this Energy Type can be used as a cost to pay for socketing Armor 2.0 items, this is the hash for the DestinyInvestmentStatDefinition that stores the plug's raw cost.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "EnergyTypes"
  }
}
```
