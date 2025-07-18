# Destiny.Definitions.Sockets.DestinySocketCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Sockets.DestinySocketCategoryDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Sockets on an item are organized into Categories visually.
You can find references to the socket category defined on an item's DestinyInventoryItemDefinition.sockets.socketCategories property.
This has the display information for rendering the categories' header, and a hint for how the UI should handle showing this category.
The shitty thing about this, however, is that the socket categories' UI style can be overridden by the item's UI style. For instance, the Socket Category used by Emote Sockets says it's "consumable," but that's a lie: they're all reusable, and overridden by the detail UI pages in ways that we can't easily account for in the API.
As a result, I will try to compile these rules into the individual sockets on items, and provide the best hint possible there through the plugSources property. In the future, I may attempt to use this information in conjunction with the item to provide a more usable UI hint on the socket layer, but for now improving the consistency of plugSources is the best I have time to provide. (See https://github.com/Bungie-net/api/issues/522 for more info)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| uiCategoryStyle | integer (uint32) | A string hinting to the game's UI system about how the sockets in this category should be displayed.
BNet doesn't use it: it's up to you to find valid values and make your own special UI if you want to honor this category style. | No |
| categoryStyle | integer (int32) | Same as uiCategoryStyle, but in a more usable enumeration form. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sockets.DestinySocketCategoryDefinition object
const example = {
  displayProperties: null,
  uiCategoryStyle: 123,
  categoryStyle: 123,
  hash: 123,
  index: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Sockets.DestinySocketCategoryDefinition object
example = {
    "displayProperties": None,
    "uiCategoryStyle": 123,
    "categoryStyle": 123,
    "hash": 123,
    "index": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.DestinySocketCategoryStyle**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Sockets.DestinySocketCategoryDefinition":   {
      "description": "Sockets on an item are organized into Categories visually.\r\nYou can find references to the socket category defined on an item's DestinyInventoryItemDefinition.sockets.socketCategories property.\r\nThis has the display information for rendering the categories' header, and a hint for how the UI should handle showing this category.\r\nThe shitty thing about this, however, is that the socket categories' UI style can be overridden by the item's UI style. For instance, the Socket Category used by Emote Sockets says it's \"consumable,\" but that's a lie: they're all reusable, and overridden by the detail UI pages in ways that we can't easily account for in the API.\r\nAs a result, I will try to compile these rules into the individual sockets on items, and provide the best hint possible there through the plugSources property. In the future, I may attempt to use this information in conjunction with the item to provide a more usable UI hint on the socket layer, but for now improving the consistency of plugSources is the best I have time to provide. (See https://github.com/Bungie-net/api/issues/522 for more info)",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "uiCategoryStyle": {
              "format": "uint32",
              "description": "A string hinting to the game's UI system about how the sockets in this category should be displayed.\r\nBNet doesn't use it: it's up to you to find valid values and make your own special UI if you want to honor this category style.",
              "type": "integer"
          },
          "categoryStyle": {
              "format": "int32",
              "description": "Same as uiCategoryStyle, but in a more usable enumeration form.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinySocketCategoryStyle"
              }
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
      "x-mobile-manifest-name": "SocketCategories"
  }
}
```
