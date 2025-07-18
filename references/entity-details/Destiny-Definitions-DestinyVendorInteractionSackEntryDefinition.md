# Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Compare this sackType to the sack identifier in the DestinyInventoryItemDefinition.vendorSackType property of items. If they match, show this sack with this interaction.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| sackType | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition object
const example = {
  sackType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition object
example = {
    "sackType": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition":   {
      "description": "Compare this sackType to the sack identifier in the DestinyInventoryItemDefinition.vendorSackType property of items. If they match, show this sack with this interaction.",
      "type": "object",
      "properties": {
          "sackType": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
