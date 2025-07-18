# Destiny.Components.Items.DestinyItemPlugObjectivesComponent

## Entity Information
- **Entity Name**: Destiny.Components.Items.DestinyItemPlugObjectivesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemplugobjectivescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectivesPerPlug | object | This set of data is keyed by the Item Hash (DestinyInventoryItemDefinition) of the plug whose objectives are being returned, with the value being the list of those objectives.
 What if two plugs with the same hash are returned for an item, you ask?
 Good question! They share the same item-scoped state, and as such would have identical objective state as a result. How's that for convenient.
 Sometimes, Plugs may have objectives: generally, these are used for flavor and display purposes. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Items.DestinyItemPlugObjectivesComponent object
const example = {
  objectivesPerPlug: null,
};
```

### Python
```python
# Example Destiny.Components.Items.DestinyItemPlugObjectivesComponent object
example = {
    "objectivesPerPlug": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Items.DestinyItemPlugObjectivesComponent":   {
      "type": "object",
      "properties": {
          "objectivesPerPlug": {
              "description": "This set of data is keyed by the Item Hash (DestinyInventoryItemDefinition) of the plug whose objectives are being returned, with the value being the list of those objectives.\r\n What if two plugs with the same hash are returned for an item, you ask?\r\n Good question! They share the same item-scoped state, and as such would have identical objective state as a result. How's that for convenient.\r\n Sometimes, Plugs may have objectives: generally, these are used for flavor and display purposes. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.",
              "type": "object",
              "additionalProperties": {
                  "type": "array",
                  "items": {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemPlugObjectives"
  }
}
```
