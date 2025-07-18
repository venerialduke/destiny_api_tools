# Destiny.Definitions.Items.DestinyEnergyCostEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyEnergyCostEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Some plugs cost Energy, which is a stat on the item that can be increased by other plugs (that, at least in Armor 2.0, have a "masterworks-like" mechanic for upgrading). If a plug has costs, the details of that cost are defined here.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| energyCost | integer (int32) | The Energy cost for inserting this plug. | No |
| energyTypeHash | integer (uint32) | The type of energy that this plug costs, as a reference to the DestinyEnergyTypeDefinition of the energy type. | No |
| energyType | integer (int32) | The type of energy that this plug costs, in enum form. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyEnergyCostEntry object
const example = {
  energyCost: 123,
  energyTypeHash: 123,
  energyType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyEnergyCostEntry object
example = {
    "energyCost": 123,
    "energyTypeHash": 123,
    "energyType": 123,
}
```

## Related Entities
- **Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition**: Referenced in this entity
- **Destiny.DestinyEnergyType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyEnergyCostEntry":   {
      "description": "Some plugs cost Energy, which is a stat on the item that can be increased by other plugs (that, at least in Armor 2.0, have a \"masterworks-like\" mechanic for upgrading). If a plug has costs, the details of that cost are defined here.",
      "type": "object",
      "properties": {
          "energyCost": {
              "format": "int32",
              "description": "The Energy cost for inserting this plug.",
              "type": "integer"
          },
          "energyTypeHash": {
              "format": "uint32",
              "description": "The type of energy that this plug costs, as a reference to the DestinyEnergyTypeDefinition of the energy type.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition"
              }
          },
          "energyType": {
              "format": "int32",
              "description": "The type of energy that this plug costs, in enum form.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyEnergyType"
              }
          }
      }
  }
}
```
