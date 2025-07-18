# Destiny.Definitions.DestinyVendorGroupReference

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorGroupReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyvendorgroupreference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorGroupHash | integer (uint32) | The DestinyVendorGroupDefinition to which this Vendor can belong. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorGroupReference object
const example = {
  vendorGroupHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorGroupReference object
example = {
    "vendorGroupHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorGroupDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorGroupReference":   {
      "type": "object",
      "properties": {
          "vendorGroupHash": {
              "format": "uint32",
              "description": "The DestinyVendorGroupDefinition to which this Vendor can belong.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorGroupDefinition"
              }
          }
      }
  }
}
```
