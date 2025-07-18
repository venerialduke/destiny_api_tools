# Destiny.Components.Vendors.DestinyVendorGroupComponent

## Entity Information
- **Entity Name**: Destiny.Components.Vendors.DestinyVendorGroupComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This component returns references to all of the Vendors in the response, grouped by categorizations that Bungie has deemed to be interesting, in the order in which both the groups and the vendors within that group should be rendered.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groups | Array[Destiny.Components.Vendors.DestinyVendorGroup] | The ordered list of groups being returned. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Vendors.DestinyVendorGroupComponent object
const example = {
  groups: [],
};
```

### Python
```python
# Example Destiny.Components.Vendors.DestinyVendorGroupComponent object
example = {
    "groups": [],
}
```

## Related Entities
- **Destiny.Components.Vendors.DestinyVendorGroup**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Vendors.DestinyVendorGroupComponent":   {
      "description": "This component returns references to all of the Vendors in the response, grouped by categorizations that Bungie has deemed to be interesting, in the order in which both the groups and the vendors within that group should be rendered.",
      "type": "object",
      "properties": {
          "groups": {
              "description": "The ordered list of groups being returned.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Vendors.DestinyVendorGroup"
              }
          }
      },
      "x-destiny-component-type-dependency": "Vendors"
  }
}
```
