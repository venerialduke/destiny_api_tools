# Destiny.Entities.Items.DestinyItemInstanceEnergy

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemInstanceEnergy
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyiteminstanceenergy data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| energyTypeHash | integer (uint32) | The type of energy for this item. Plugs that require Energy can only be inserted if they have the "Any" Energy Type or the matching energy type of this item. This is a reference to the DestinyEnergyTypeDefinition for the energy type, where you can find extended info about it. | No |
| energyType | integer (int32) | This is the enum version of the Energy Type value, for convenience. | No |
| energyCapacity | integer (int32) | The total capacity of Energy that the item currently has, regardless of if it is currently being used. | No |
| energyUsed | integer (int32) | The amount of Energy currently in use by inserted plugs. | No |
| energyUnused | integer (int32) | The amount of energy still available for inserting new plugs. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemInstanceEnergy object
const example = {
  energyTypeHash: 123,
  energyType: 123,
  energyCapacity: 123,
  energyUsed: 123,
  energyUnused: 123,
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemInstanceEnergy object
example = {
    "energyTypeHash": 123,
    "energyType": 123,
    "energyCapacity": 123,
    "energyUsed": 123,
    "energyUnused": 123,
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
  "Destiny.Entities.Items.DestinyItemInstanceEnergy":   {
      "type": "object",
      "properties": {
          "energyTypeHash": {
              "format": "uint32",
              "description": "The type of energy for this item. Plugs that require Energy can only be inserted if they have the \"Any\" Energy Type or the matching energy type of this item. This is a reference to the DestinyEnergyTypeDefinition for the energy type, where you can find extended info about it.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.EnergyTypes.DestinyEnergyTypeDefinition"
              }
          },
          "energyType": {
              "format": "int32",
              "description": "This is the enum version of the Energy Type value, for convenience.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyEnergyType"
              }
          },
          "energyCapacity": {
              "format": "int32",
              "description": "The total capacity of Energy that the item currently has, regardless of if it is currently being used.",
              "type": "integer"
          },
          "energyUsed": {
              "format": "int32",
              "description": "The amount of Energy currently in use by inserted plugs.",
              "type": "integer"
          },
          "energyUnused": {
              "format": "int32",
              "description": "The amount of energy still available for inserting new plugs.",
              "type": "integer"
          }
      }
  }
}
```
