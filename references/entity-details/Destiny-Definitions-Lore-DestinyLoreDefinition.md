# Destiny.Definitions.Lore.DestinyLoreDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Lore.DestinyLoreDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
These are definitions for in-game "Lore," meant to be narrative enhancements of the game experience.
DestinyInventoryItemDefinitions for interesting items point to these definitions, but nothing's stopping you from scraping all of these and doing something cool with them. If they end up having cool data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| subtitle | string |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Lore.DestinyLoreDefinition object
const example = {
  displayProperties: null,
  subtitle: "example value",
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Lore.DestinyLoreDefinition object
example = {
    "displayProperties": None,
    "subtitle": "example value",
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Lore.DestinyLoreDefinition":   {
      "description": "These are definitions for in-game \"Lore,\" meant to be narrative enhancements of the game experience.\r\nDestinyInventoryItemDefinitions for interesting items point to these definitions, but nothing's stopping you from scraping all of these and doing something cool with them. If they end up having cool data.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "subtitle": {
              "type": "string"
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "Lore"
  }
}
```
