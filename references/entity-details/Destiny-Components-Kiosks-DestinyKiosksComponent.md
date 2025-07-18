# Destiny.Components.Kiosks.DestinyKiosksComponent

## Entity Information
- **Entity Name**: Destiny.Components.Kiosks.DestinyKiosksComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A Kiosk is a Vendor (DestinyVendorDefinition) that sells items based on whether you have already acquired that item before.
This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the individual character's DestinyCharacterKiosksComponent.
Note that, because this component returns vendorItemIndexes (that is to say, indexes into the Kiosk Vendor's itemList property), these results are necessarily content version dependent. Make sure that you have the latest version of the content manifest databases before using this data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| kioskItems | object | A dictionary keyed by the Kiosk Vendor's hash identifier (use it to look up the DestinyVendorDefinition for the relevant kiosk vendor), and whose value is a list of all the items that the user can "see" in the Kiosk, and any other interesting metadata. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Kiosks.DestinyKiosksComponent object
const example = {
  kioskItems: null,
};
```

### Python
```python
# Example Destiny.Components.Kiosks.DestinyKiosksComponent object
example = {
    "kioskItems": None,
}
```

## Related Entities
- **Destiny.Components.Kiosks.DestinyKioskItem**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Kiosks.DestinyKiosksComponent":   {
      "description": "A Kiosk is a Vendor (DestinyVendorDefinition) that sells items based on whether you have already acquired that item before.\r\nThis component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the individual character's DestinyCharacterKiosksComponent.\r\nNote that, because this component returns vendorItemIndexes (that is to say, indexes into the Kiosk Vendor's itemList property), these results are necessarily content version dependent. Make sure that you have the latest version of the content manifest databases before using this data.",
      "type": "object",
      "properties": {
          "kioskItems": {
              "description": "A dictionary keyed by the Kiosk Vendor's hash identifier (use it to look up the DestinyVendorDefinition for the relevant kiosk vendor), and whose value is a list of all the items that the user can \"see\" in the Kiosk, and any other interesting metadata.",
              "type": "object",
              "additionalProperties": {
                  "type": "array",
                  "items": {
                      "$ref": "#/definitions/Destiny.Components.Kiosks.DestinyKioskItem"
                  }
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Kiosks"
  }
}
```
