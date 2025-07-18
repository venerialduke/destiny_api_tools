# Destiny.Components.Vendors.DestinyVendorBaseComponent

## Entity Information
- **Entity Name**: Destiny.Components.Vendors.DestinyVendorBaseComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This component contains essential/summary information about the vendor.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition. | No |
| nextRefreshDate | string (date-time) | The date when this vendor's inventory will next rotate/refresh.
Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different.
Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use. | No |
| enabled | boolean | If True, the Vendor is currently accessible. 
If False, they may not actually be visible in the world at the moment. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Vendors.DestinyVendorBaseComponent object
const example = {
  vendorHash: 123,
  nextRefreshDate: "example value",
  enabled: true,
};
```

### Python
```python
# Example Destiny.Components.Vendors.DestinyVendorBaseComponent object
example = {
    "vendorHash": 123,
    "nextRefreshDate": "example value",
    "enabled": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Vendors.DestinyVendorBaseComponent":   {
      "description": "This component contains essential/summary information about the vendor.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "nextRefreshDate": {
              "format": "date-time",
              "description": "The date when this vendor's inventory will next rotate/refresh.\r\nNote that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different.\r\nIssue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use.",
              "type": "string"
          },
          "enabled": {
              "description": "If True, the Vendor is currently accessible. \r\nIf False, they may not actually be visible in the world at the moment.",
              "type": "boolean"
          }
      },
      "x-destiny-component-type-dependency": "Vendors"
  }
}
```
