# Destiny.Components.Vendors.DestinyVendorGroup

## Entity Information
- **Entity Name**: Destiny.Components.Vendors.DestinyVendorGroup
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a specific group of vendors that can be rendered in the recommended order.
How do we figure out this order? It's a long story, and will likely get more complicated over time.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorGroupHash | integer (uint32) |  | No |
| vendorHashes | Array[integer] | The ordered list of vendors within a particular group. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Vendors.DestinyVendorGroup object
const example = {
  vendorGroupHash: 123,
  vendorHashes: [],
};
```

### Python
```python
# Example Destiny.Components.Vendors.DestinyVendorGroup object
example = {
    "vendorGroupHash": 123,
    "vendorHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorGroupDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Vendors.DestinyVendorGroup":   {
      "description": "Represents a specific group of vendors that can be rendered in the recommended order.\r\nHow do we figure out this order? It's a long story, and will likely get more complicated over time.",
      "type": "object",
      "properties": {
          "vendorGroupHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorGroupDefinition"
              }
          },
          "vendorHashes": {
              "description": "The ordered list of vendors within a particular group.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          }
      }
  }
}
```
