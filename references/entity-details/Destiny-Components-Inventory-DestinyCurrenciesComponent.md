# Destiny.Components.Inventory.DestinyCurrenciesComponent

## Entity Information
- **Entity Name**: Destiny.Components.Inventory.DestinyCurrenciesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This component provides a quick lookup of every item the requested character has and how much of that item they have.
Requesting this component will allow you to circumvent manually putting together the list of which currencies you have for the purpose of testing currency requirements on an item being purchased, or operations that have costs.
You *could* figure this out yourself by doing a GetCharacter or GetProfile request and forming your own lookup table, but that is inconvenient enough that this feels like a worthwhile (and optional) redundancy. Don't bother requesting it if you have already created your own lookup from prior GetCharacter/GetProfile calls.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemQuantities | object | A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing.
This allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself. | No |
| materialRequirementSetStates | object | A map of material requirement hashes and their status information. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Inventory.DestinyCurrenciesComponent object
const example = {
  itemQuantities: null,
  materialRequirementSetStates: null,
};
```

### Python
```python
# Example Destiny.Components.Inventory.DestinyCurrenciesComponent object
example = {
    "itemQuantities": None,
    "materialRequirementSetStates": None,
}
```

## Related Entities
- **Destiny.Components.Inventory.DestinyMaterialRequirementSetState**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Inventory.DestinyCurrenciesComponent":   {
      "description": "This component provides a quick lookup of every item the requested character has and how much of that item they have.\r\nRequesting this component will allow you to circumvent manually putting together the list of which currencies you have for the purpose of testing currency requirements on an item being purchased, or operations that have costs.\r\nYou *could* figure this out yourself by doing a GetCharacter or GetProfile request and forming your own lookup table, but that is inconvenient enough that this feels like a worthwhile (and optional) redundancy. Don't bother requesting it if you have already created your own lookup from prior GetCharacter/GetProfile calls.",
      "type": "object",
      "properties": {
          "itemQuantities": {
              "description": "A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing.\r\nThis allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.",
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "materialRequirementSetStates": {
              "description": "A map of material requirement hashes and their status information.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Components.Inventory.DestinyMaterialRequirementSetState"
              }
          }
      },
      "x-destiny-component-type-dependency": "CurrencyLookups"
  }
}
```
