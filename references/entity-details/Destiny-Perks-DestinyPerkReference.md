# Destiny.Perks.DestinyPerkReference

## Entity Information
- **Entity Name**: Destiny.Perks.DestinyPerkReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The list of perks to display in an item tooltip - and whether or not they have been activated.
Perks apply a variety of effects to a character, and are generally either intrinsic to the item or provided in activated talent nodes or sockets.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| perkHash | integer (uint32) | The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user. | No |
| iconPath | string | The icon for the perk. | No |
| isActive | boolean | Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.) | No |
| visible | boolean | Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Perks.DestinyPerkReference object
const example = {
  perkHash: 123,
  iconPath: "example value",
  isActive: true,
  visible: true,
};
```

### Python
```python
# Example Destiny.Perks.DestinyPerkReference object
example = {
    "perkHash": 123,
    "iconPath": "example value",
    "isActive": True,
    "visible": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinySandboxPerkDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Perks.DestinyPerkReference":   {
      "description": "The list of perks to display in an item tooltip - and whether or not they have been activated.\r\nPerks apply a variety of effects to a character, and are generally either intrinsic to the item or provided in activated talent nodes or sockets.",
      "type": "object",
      "properties": {
          "perkHash": {
              "format": "uint32",
              "description": "The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinySandboxPerkDefinition"
              }
          },
          "iconPath": {
              "description": "The icon for the perk.",
              "type": "string"
          },
          "isActive": {
              "description": "Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)",
              "type": "boolean"
          },
          "visible": {
              "description": "Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI.",
              "type": "boolean"
          }
      }
  }
}
```
