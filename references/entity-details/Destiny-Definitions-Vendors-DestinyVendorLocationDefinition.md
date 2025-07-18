# Destiny.Definitions.Vendors.DestinyVendorLocationDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Vendors.DestinyVendorLocationDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
These definitions represent vendors' locations and relevant display information at different times in the game.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| destinationHash | integer (uint32) | The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry. | No |
| backgroundImagePath | string | The relative path to the background image representing this Vendor at this location, for use in a banner. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Vendors.DestinyVendorLocationDefinition object
const example = {
  destinationHash: 123,
  backgroundImagePath: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Vendors.DestinyVendorLocationDefinition object
example = {
    "destinationHash": 123,
    "backgroundImagePath": "example value",
}
```

## Related Entities
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Vendors.DestinyVendorLocationDefinition":   {
      "description": "These definitions represent vendors' locations and relevant display information at different times in the game.",
      "type": "object",
      "properties": {
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
