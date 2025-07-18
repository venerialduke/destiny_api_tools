# Destiny.Definitions.Items.DestinyEnergyCapacityEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyEnergyCapacityEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Items can have Energy Capacity, and plugs can provide that capacity such as on a piece of Armor in Armor 2.0. This is how much "Energy" can be spent on activating plugs for this item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| capacityValue | integer (int32) | How much energy capacity this plug provides. | No |
| energyTypeHash | integer (uint32) | Energy provided by a plug is always of a specific type - this is the hash identifier for the energy type for which it provides Capacity. | No |
| energyType | integer (int32) | The Energy Type for this energy capacity, in enum form for easy use. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyEnergyCapacityEntry object
const example = {
  capacityValue: 123,
  energyTypeHash: 123,
  energyType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyEnergyCapacityEntry object
example = {
    "capacityValue": 123,
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
  "Destiny.Definitions.Items.DestinyEnergyCapacityEntry":   {
      "description": "Items can have Energy Capacity, and plugs can provide that capacity such as on a piece of Armor in Armor 2.0. This is how much \"Energy\" can be spent on activating plugs for this item.",
      "type": "object",
      "properties": {
          "capacityValue": {
              "format": "int32",
              "description": "How much energy capacity this plug provides.",
              "type": "integer"
          },
          "energyTypeHash": {
              "format": "uint32",
              "description": "Energy provided by a plug is always of a specific type - this is the hash identifier for the energy type for which it provides Capacity.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition"
              }
          },
          "energyType": {
              "format": "int32",
              "description": "The Energy Type for this energy capacity, in enum form for easy use.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyEnergyType"
              }
          }
      }
  }
}
```
