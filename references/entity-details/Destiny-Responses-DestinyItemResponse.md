# Destiny.Responses.DestinyItemResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyItemResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| characterId | integer (int64) | If the item is on a character, this will return the ID of the character that is holding the item. | No |
| item | object | Common data for the item relevant to its non-instanced properties.
COMPONENT TYPE: ItemCommonData | No |
| instance | object | Basic instance data for the item.
COMPONENT TYPE: ItemInstances | No |
| objectives | object | Information specifically about the item's objectives.
COMPONENT TYPE: ItemObjectives | No |
| perks | object | Information specifically about the perks currently active on the item.
COMPONENT TYPE: ItemPerks | No |
| renderData | object | Information about how to render the item in 3D.
COMPONENT TYPE: ItemRenderData | No |
| stats | object | Information about the computed stats of the item: power, defense, etc...
COMPONENT TYPE: ItemStats | No |
| talentGrid | object | Information about the talent grid attached to the item. Talent nodes can provide a variety of benefits and abilities, and in Destiny 2 are used almost exclusively for the character's "Builds".
COMPONENT TYPE: ItemTalentGrids | No |
| sockets | object | Information about the sockets of the item: which are currently active, what potential sockets you could have and the stats/abilities/perks you can gain from them.
COMPONENT TYPE: ItemSockets | No |
| reusablePlugs | object | Information about the Reusable Plugs for sockets on an item. These are plugs that you can insert into the given socket regardless of if you actually own an instance of that plug: they are logic-driven plugs rather than inventory-driven.
 These may need to be combined with Plug Set component data to get a full picture of available plugs on a given socket.
 COMPONENT TYPE: ItemReusablePlugs | No |
| plugObjectives | object | Information about objectives on Plugs for a given item. See the component's documentation for more info.
COMPONENT TYPE: ItemPlugObjectives | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyItemResponse object
const example = {
  characterId: 123,
  item: null,
  instance: null,
  objectives: null,
  perks: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Responses.DestinyItemResponse object
example = {
    "characterId": 123,
    "item": None,
    "instance": None,
    "objectives": None,
    "perks": None,
    # ... more properties
}
```

## Related Entities
- **SingleComponentResponseOfDestinyItemComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemInstanceComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemObjectivesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemPerksComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemPlugObjectivesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemRenderComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemReusablePlugsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemSocketsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemStatsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyItemTalentGridComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyItemResponse":   {
      "description": "The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an \"itemInstanceId\": for those, get your information from the DestinyInventoryDefinition.",
      "type": "object",
      "properties": {
          "characterId": {
              "format": "int64",
              "description": "If the item is on a character, this will return the ID of the character that is holding the item.",
              "type": "integer"
          },
          "item": {
              "description": "Common data for the item relevant to its non-instanced properties.\r\nCOMPONENT TYPE: ItemCommonData",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemCommonData"
          },
          "instance": {
              "description": "Basic instance data for the item.\r\nCOMPONENT TYPE: ItemInstances",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemInstanceComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemInstances"
          },
          "objectives": {
              "description": "Information specifically about the item's objectives.\r\nCOMPONENT TYPE: ItemObjectives",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemObjectivesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemObjectives"
          },
          "perks": {
              "description": "Information specifically about the perks currently active on the item.\r\nCOMPONENT TYPE: ItemPerks",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemPerksComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemPerks"
          },
          "renderData": {
              "description": "Information about how to render the item in 3D.\r\nCOMPONENT TYPE: ItemRenderData",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemRenderComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemRenderData"
          },
          "stats": {
              "description": "Information about the computed stats of the item: power, defense, etc...\r\nCOMPONENT TYPE: ItemStats",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemStatsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemStats"
          },
          "talentGrid": {
              "description": "Information about the talent grid attached to the item. Talent nodes can provide a variety of benefits and abilities, and in Destiny 2 are used almost exclusively for the character's \"Builds\".\r\nCOMPONENT TYPE: ItemTalentGrids",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemTalentGridComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemTalentGrids"
          },
          "sockets": {
              "description": "Information about the sockets of the item: which are currently active, what potential sockets you could have and the stats/abilities/perks you can gain from them.\r\nCOMPONENT TYPE: ItemSockets",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemSocketsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemSockets"
          },
          "reusablePlugs": {
              "description": "Information about the Reusable Plugs for sockets on an item. These are plugs that you can insert into the given socket regardless of if you actually own an instance of that plug: they are logic-driven plugs rather than inventory-driven.\r\n These may need to be combined with Plug Set component data to get a full picture of available plugs on a given socket.\r\n COMPONENT TYPE: ItemReusablePlugs",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemReusablePlugsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemReusablePlugs"
          },
          "plugObjectives": {
              "description": "Information about objectives on Plugs for a given item. See the component's documentation for more info.\r\nCOMPONENT TYPE: ItemPlugObjectives",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyItemPlugObjectivesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemPlugObjectives"
          }
      }
  }
}
```
