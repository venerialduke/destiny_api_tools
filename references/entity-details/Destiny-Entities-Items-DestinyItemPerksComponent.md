# Destiny.Entities.Items.DestinyItemPerksComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemPerksComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Instanced items can have perks: benefits that the item bestows.
These are related to DestinySandboxPerkDefinition, and sometimes - but not always - have human readable info. When they do, they are the icons and text that you see in an item's tooltip.
Talent Grids, Sockets, and the item itself can apply Perks, which are then summarized here for your convenience.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| perks | Array[Destiny.Perks.DestinyPerkReference] | The list of perks to display in an item tooltip - and whether or not they have been activated. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemPerksComponent object
const example = {
  perks: [],
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemPerksComponent object
example = {
    "perks": [],
}
```

## Related Entities
- **Destiny.Perks.DestinyPerkReference**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemPerksComponent":   {
      "description": "Instanced items can have perks: benefits that the item bestows.\r\nThese are related to DestinySandboxPerkDefinition, and sometimes - but not always - have human readable info. When they do, they are the icons and text that you see in an item's tooltip.\r\nTalent Grids, Sockets, and the item itself can apply Perks, which are then summarized here for your convenience.",
      "type": "object",
      "properties": {
          "perks": {
              "description": "The list of perks to display in an item tooltip - and whether or not they have been activated.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Perks.DestinyPerkReference"
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemPerks"
  }
}
```
