# Destiny.Entities.Vendors.DestinyVendorComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Vendors.DestinyVendorComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This component contains essential/summary information about the vendor.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| canPurchase | boolean | If True, you can purchase from the Vendor. | No |
| progression | object | If the Vendor has a related Reputation, this is the Progression data that represents the character's Reputation level with this Vendor. | No |
| vendorLocationIndex | integer (int32) | An index into the vendor definition's "locations" property array, indicating which location they are at currently. If -1, then the vendor has no known location (and you may choose not to show them in your UI as a result. I mean, it's your bag honey) | No |
| seasonalRank | integer (int32) | If this vendor has a seasonal rank, this will be the calculated value of that rank. How nice is that? I mean, that's pretty sweeet. It's a whole 32 bit integer. | No |
| vendorHash | integer (uint32) | The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition. | No |
| nextRefreshDate | string (date-time) | The date when this vendor's inventory will next rotate/refresh.
Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different.
Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use. | No |
| enabled | boolean | If True, the Vendor is currently accessible. 
If False, they may not actually be visible in the world at the moment. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Vendors.DestinyVendorComponent object
const example = {
  canPurchase: true,
  progression: null,
  vendorLocationIndex: 123,
  seasonalRank: 123,
  vendorHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Vendors.DestinyVendorComponent object
example = {
    "canPurchase": True,
    "progression": None,
    "vendorLocationIndex": 123,
    "seasonalRank": 123,
    "vendorHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.DestinyProgression**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Vendors.DestinyVendorComponent":   {
      "description": "This component contains essential/summary information about the vendor.",
      "type": "object",
      "properties": {
          "canPurchase": {
              "description": "If True, you can purchase from the Vendor.",
              "type": "boolean"
          },
          "progression": {
              "description": "If the Vendor has a related Reputation, this is the Progression data that represents the character's Reputation level with this Vendor.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.DestinyProgression"
                  }
              ]
          },
          "vendorLocationIndex": {
              "format": "int32",
              "description": "An index into the vendor definition's \"locations\" property array, indicating which location they are at currently. If -1, then the vendor has no known location (and you may choose not to show them in your UI as a result. I mean, it's your bag honey)",
              "type": "integer"
          },
          "seasonalRank": {
              "format": "int32",
              "description": "If this vendor has a seasonal rank, this will be the calculated value of that rank. How nice is that? I mean, that's pretty sweeet. It's a whole 32 bit integer.",
              "type": "integer"
          },
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
