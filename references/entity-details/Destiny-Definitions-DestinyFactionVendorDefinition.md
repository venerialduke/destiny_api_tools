# Destiny.Definitions.DestinyFactionVendorDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyFactionVendorDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
These definitions represent faction vendors at different points in the game.
A single faction may contain multiple vendors, or the same vendor available at two different locations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | The faction vendor hash. | No |
| destinationHash | integer (uint32) | The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry. | No |
| backgroundImagePath | string | The relative path to the background image representing this Vendor at this location, for use in a banner. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyFactionVendorDefinition object
const example = {
  vendorHash: 123,
  destinationHash: 123,
  backgroundImagePath: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyFactionVendorDefinition object
example = {
    "vendorHash": 123,
    "destinationHash": 123,
    "backgroundImagePath": "example value",
}
```

## Related Entities
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyFactionVendorDefinition":   {
      "description": "These definitions represent faction vendors at different points in the game.\r\nA single faction may contain multiple vendors, or the same vendor available at two different locations.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "The faction vendor hash.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "destinationHash": {
              "format": "uint32",
              "description": "The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          },
          "backgroundImagePath": {
              "description": "The relative path to the background image representing this Vendor at this location, for use in a banner.",
              "type": "string"
          }
      }
  }
}
```
