# Destiny.Definitions.DestinyItemValueBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemValueBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This defines an item's "Value". Unfortunately, this appears to be used in different ways depending on the way that the item itself is used.
For items being sold at a Vendor, this is the default "sale price" of the item. These days, the vendor itself almost always sets the price, but it still possible for the price to fall back to this value. For quests, it is a preview of rewards you can gain by completing the quest. For dummy items, if the itemValue refers to an Emblem, it is the emblem that should be shown as the reward. (jeez louise)
It will likely be used in a number of other ways in the future, it appears to be a bucket where they put arbitrary items and quantities into the item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemValue | Array[Destiny.DestinyItemQuantity] | References to the items that make up this item's "value", and the quantity. | No |
| valueDescription | string | If there's a localized text description of the value provided, this will be said description. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemValueBlockDefinition object
const example = {
  itemValue: [],
  valueDescription: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemValueBlockDefinition object
example = {
    "itemValue": [],
    "valueDescription": "example value",
}
```

## Related Entities
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemValueBlockDefinition":   {
      "description": "This defines an item's \"Value\". Unfortunately, this appears to be used in different ways depending on the way that the item itself is used.\r\nFor items being sold at a Vendor, this is the default \"sale price\" of the item. These days, the vendor itself almost always sets the price, but it still possible for the price to fall back to this value. For quests, it is a preview of rewards you can gain by completing the quest. For dummy items, if the itemValue refers to an Emblem, it is the emblem that should be shown as the reward. (jeez louise)\r\nIt will likely be used in a number of other ways in the future, it appears to be a bucket where they put arbitrary items and quantities into the item.",
      "type": "object",
      "properties": {
          "itemValue": {
              "description": "References to the items that make up this item's \"value\", and the quantity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          },
          "valueDescription": {
              "description": "If there's a localized text description of the value provided, this will be said description.",
              "type": "string"
          }
      }
  }
}
```
