# Destiny.Entities.Characters.DestinyCharacterRenderComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Characters.DestinyCharacterRenderComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Only really useful if you're attempting to render the character's current appearance in 3D, this returns a bare minimum of information, pre-aggregated, that you'll need to perform that rendering. Note that you need to combine this with other 3D assets and data from our servers.
Examine the Javascript returned by https://bungie.net/sharedbundle/spasm to see how we use this data, but be warned: the rabbit hole goes pretty deep.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| customDyes | Array[Destiny.DyeReference] | Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server. | No |
| customization | object | This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that. | No |
| peerView | object | A minimal view of:
- Equipped items
- The rendering-related custom options on those equipped items
Combined, that should be enough to render all of the items on the equipped character. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Characters.DestinyCharacterRenderComponent object
const example = {
  customDyes: [],
  customization: null,
  peerView: null,
};
```

### Python
```python
# Example Destiny.Entities.Characters.DestinyCharacterRenderComponent object
example = {
    "customDyes": [],
    "customization": None,
    "peerView": None,
}
```

## Related Entities
- **Destiny.Character.DestinyCharacterCustomization**: Referenced in this entity
- **Destiny.Character.DestinyCharacterPeerView**: Referenced in this entity
- **Destiny.DyeReference**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Characters.DestinyCharacterRenderComponent":   {
      "description": "Only really useful if you're attempting to render the character's current appearance in 3D, this returns a bare minimum of information, pre-aggregated, that you'll need to perform that rendering. Note that you need to combine this with other 3D assets and data from our servers.\r\nExamine the Javascript returned by https://bungie.net/sharedbundle/spasm to see how we use this data, but be warned: the rabbit hole goes pretty deep.",
      "type": "object",
      "properties": {
          "customDyes": {
              "description": "Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DyeReference"
              }
          },
          "customization": {
              "description": "This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Character.DestinyCharacterCustomization"
                  }
              ]
          },
          "peerView": {
              "description": "A minimal view of:\r\n- Equipped items\r\n- The rendering-related custom options on those equipped items\r\nCombined, that should be enough to render all of the items on the equipped character.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Character.DestinyCharacterPeerView"
                  }
              ]
          }
      },
      "x-destiny-component-type-dependency": "CharacterRenderData"
  }
}
```
