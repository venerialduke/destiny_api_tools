# Destiny.Entities.Items.DestinyItemStatsComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemStatsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If you want the stats on an item's instanced data, get this component.
These are stats like Attack, Defense etc... and *not* historical stats.
Note that some stats have additional computation in-game at runtime - for instance, Magazine Size - and thus these stats might not be 100% accurate compared to what you see in-game for some stats. I know, it sucks. I hate it too.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| stats | object | If the item has stats that it provides (damage, defense, etc...), it will be given here. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemStatsComponent object
const example = {
  stats: null,
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemStatsComponent object
example = {
    "stats": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity
- **Destiny.DestinyStat**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemStatsComponent":   {
      "description": "If you want the stats on an item's instanced data, get this component.\r\nThese are stats like Attack, Defense etc... and *not* historical stats.\r\nNote that some stats have additional computation in-game at runtime - for instance, Magazine Size - and thus these stats might not be 100% accurate compared to what you see in-game for some stats. I know, it sucks. I hate it too.",
      "type": "object",
      "properties": {
          "stats": {
              "description": "If the item has stats that it provides (damage, defense, etc...), it will be given here.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.DestinyStat"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemStats"
  }
}
```
