# Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition for an "inventory flyout": a UI screen where we show you part of an otherwise hidden vendor inventory: like the Vault inventory buckets.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lockedDescription | string | If the flyout is locked, this is the reason why. | No |
| displayProperties | object | The title and other common properties of the flyout. | No |
| buckets | Array[Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition] | A list of inventory buckets and other metadata to show on the screen. | No |
| flyoutId | integer (uint32) | An identifier for the flyout, in case anything else needs to refer to them. | No |
| suppressNewness | boolean | If this is true, don't show any of the glistening "this is a new item" UI elements, like we show on the inventory items themselves in in-game UI. | No |
| equipmentSlotHash | integer (uint32) | If this flyout is meant to show you the contents of the player's equipment slot, this is the slot to show. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition object
const example = {
  lockedDescription: "example value",
  displayProperties: null,
  buckets: [],
  flyoutId: 123,
  suppressNewness: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition object
example = {
    "lockedDescription": "example value",
    "displayProperties": None,
    "buckets": [],
    "flyoutId": 123,
    "suppressNewness": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition":   {
      "description": "The definition for an \"inventory flyout\": a UI screen where we show you part of an otherwise hidden vendor inventory: like the Vault inventory buckets.",
      "type": "object",
      "properties": {
          "lockedDescription": {
              "description": "If the flyout is locked, this is the reason why.",
              "type": "string"
          },
          "displayProperties": {
              "description": "The title and other common properties of the flyout.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "buckets": {
              "description": "A list of inventory buckets and other metadata to show on the screen.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorInventoryFlyoutBucketDefinition"
              }
          },
          "flyoutId": {
              "format": "uint32",
              "description": "An identifier for the flyout, in case anything else needs to refer to them.",
              "type": "integer"
          },
          "suppressNewness": {
              "description": "If this is true, don't show any of the glistening \"this is a new item\" UI elements, like we show on the inventory items themselves in in-game UI.",
              "type": "boolean"
          },
          "equipmentSlotHash": {
              "format": "uint32",
              "description": "If this flyout is meant to show you the contents of the player's equipment slot, this is the slot to show.",
              "type": "integer"
          }
      }
  }
}
```
