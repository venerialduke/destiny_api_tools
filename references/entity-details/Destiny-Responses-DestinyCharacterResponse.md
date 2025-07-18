# Destiny.Responses.DestinyCharacterResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyCharacterResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| inventory | object | The character-level non-equipped inventory items.
COMPONENT TYPE: CharacterInventories | No |
| character | object | Base information about the character in question.
COMPONENT TYPE: Characters | No |
| progressions | object | Character progression data, including Milestones.
COMPONENT TYPE: CharacterProgressions | No |
| renderData | object | Character rendering data - a minimal set of information about equipment and dyes used for rendering.
COMPONENT TYPE: CharacterRenderData | No |
| activities | object | Activity data - info about current activities available to the player.
COMPONENT TYPE: CharacterActivities | No |
| equipment | object | Equipped items on the character.
COMPONENT TYPE: CharacterEquipment | No |
| loadouts | object | The loadouts available to the character.
COMPONENT TYPE: CharacterLoadouts | No |
| kiosks | object | Items available from Kiosks that are available to this specific character. 
COMPONENT TYPE: Kiosks | No |
| plugSets | object | When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are scoped to this character.
This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.
COMPONENT TYPE: ItemSockets | No |
| presentationNodes | object | COMPONENT TYPE: PresentationNodes | No |
| records | object | COMPONENT TYPE: Records | No |
| collectibles | object | COMPONENT TYPE: Collectibles | No |
| itemComponents | object | The set of components belonging to the player's instanced items.
COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.] | No |
| uninstancedItemComponents | object | The set of components belonging to the player's UNinstanced items. Because apparently now those too can have information relevant to the character's state.
COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.] | No |
| currencyLookups | object | A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
COMPONENT TYPE: CurrencyLookups | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyCharacterResponse object
const example = {
  inventory: null,
  character: null,
  progressions: null,
  renderData: null,
  activities: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Responses.DestinyCharacterResponse object
example = {
    "inventory": None,
    "character": None,
    "progressions": None,
    "renderData": None,
    "activities": None,
    # ... more properties
}
```

## Related Entities
- **DestinyBaseItemComponentSetOfuint32**: Referenced in this entity
- **DestinyItemComponentSetOfint64**: Referenced in this entity
- **SingleComponentResponseOfDestinyCharacterActivitiesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCharacterComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCharacterProgressionComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCharacterRecordsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCharacterRenderComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCollectiblesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCurrenciesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyInventoryComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyKiosksComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyLoadoutsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyPlugSetsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyPresentationNodesComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyCharacterResponse":   {
      "description": "The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.",
      "type": "object",
      "properties": {
          "inventory": {
              "description": "The character-level non-equipped inventory items.\r\nCOMPONENT TYPE: CharacterInventories",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyInventoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterInventories"
          },
          "character": {
              "description": "Base information about the character in question.\r\nCOMPONENT TYPE: Characters",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCharacterComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Characters"
          },
          "progressions": {
              "description": "Character progression data, including Milestones.\r\nCOMPONENT TYPE: CharacterProgressions",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCharacterProgressionComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterProgressions"
          },
          "renderData": {
              "description": "Character rendering data - a minimal set of information about equipment and dyes used for rendering.\r\nCOMPONENT TYPE: CharacterRenderData",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCharacterRenderComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterRenderData"
          },
          "activities": {
              "description": "Activity data - info about current activities available to the player.\r\nCOMPONENT TYPE: CharacterActivities",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCharacterActivitiesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterActivities"
          },
          "equipment": {
              "description": "Equipped items on the character.\r\nCOMPONENT TYPE: CharacterEquipment",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyInventoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterEquipment"
          },
          "loadouts": {
              "description": "The loadouts available to the character.\r\nCOMPONENT TYPE: CharacterLoadouts",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyLoadoutsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterLoadouts"
          },
          "kiosks": {
              "description": "Items available from Kiosks that are available to this specific character. \r\nCOMPONENT TYPE: Kiosks",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyKiosksComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Kiosks"
          },
          "plugSets": {
              "description": "When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are scoped to this character.\r\nThis comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.\r\nCOMPONENT TYPE: ItemSockets",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyPlugSetsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemSockets"
          },
          "presentationNodes": {
              "description": "COMPONENT TYPE: PresentationNodes",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyPresentationNodesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "PresentationNodes"
          },
          "records": {
              "description": "COMPONENT TYPE: Records",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCharacterRecordsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Records"
          },
          "collectibles": {
              "description": "COMPONENT TYPE: Collectibles",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCollectiblesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Collectibles"
          },
          "itemComponents": {
              "description": "The set of components belonging to the player's instanced items.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DestinyItemComponentSetOfint64"
                  }
              ]
          },
          "uninstancedItemComponents": {
              "description": "The set of components belonging to the player's UNinstanced items. Because apparently now those too can have information relevant to the character's state.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DestinyBaseItemComponentSetOfuint32"
                  }
              ]
          },
          "currencyLookups": {
              "description": "A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.\r\nCOMPONENT TYPE: CurrencyLookups",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCurrenciesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CurrencyLookups"
          }
      }
  }
}
```
