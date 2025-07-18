# Destiny.Definitions.DestinyItemSocketBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSocketBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If defined, the item has at least one socket.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| detail | string | This was supposed to be a string that would give per-item details about sockets. In practice, it turns out that all this ever has is the localized word "details". ... that's lame, but perhaps it will become something cool in the future. | No |
| socketEntries | Array[Destiny.Definitions.DestinyItemSocketEntryDefinition] | Each non-intrinsic (or mutable) socket on an item is defined here. Check inside for more info. | No |
| intrinsicSockets | Array[Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition] | Each intrinsic (or immutable/permanent) socket on an item is defined here, along with the plug that is permanently affixed to the socket. | No |
| socketCategories | Array[Destiny.Definitions.DestinyItemSocketCategoryDefinition] | A convenience property, that refers to the sockets in the "sockets" property, pre-grouped by category and ordered in the manner that they should be grouped in the UI. You could form this yourself with the existing data, but why would you want to? Enjoy life man. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSocketBlockDefinition object
const example = {
  detail: "example value",
  socketEntries: [],
  intrinsicSockets: [],
  socketCategories: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSocketBlockDefinition object
example = {
    "detail": "example value",
    "socketEntries": [],
    "intrinsicSockets": [],
    "socketCategories": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSocketCategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSocketEntryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSocketBlockDefinition":   {
      "description": "If defined, the item has at least one socket.",
      "type": "object",
      "properties": {
          "detail": {
              "description": "This was supposed to be a string that would give per-item details about sockets. In practice, it turns out that all this ever has is the localized word \"details\". ... that's lame, but perhaps it will become something cool in the future.",
              "type": "string"
          },
          "socketEntries": {
              "description": "Each non-intrinsic (or mutable) socket on an item is defined here. Check inside for more info.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemSocketEntryDefinition"
              }
          },
          "intrinsicSockets": {
              "description": "Each intrinsic (or immutable/permanent) socket on an item is defined here, along with the plug that is permanently affixed to the socket.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition"
              }
          },
          "socketCategories": {
              "description": "A convenience property, that refers to the sockets in the \"sockets\" property, pre-grouped by category and ordered in the manner that they should be grouped in the UI. You could form this yourself with the existing data, but why would you want to? Enjoy life man.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemSocketCategoryDefinition"
              }
          }
      }
  }
}
```
