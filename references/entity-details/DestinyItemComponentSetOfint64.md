# DestinyItemComponentSetOfint64

## Entity Information
- **Entity Name**: DestinyItemComponentSetOfint64
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemcomponentsetofint64 data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| instances | DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent |  | No |
| renderData | DictionaryComponentResponseOfint64AndDestinyItemRenderComponent |  | No |
| stats | DictionaryComponentResponseOfint64AndDestinyItemStatsComponent |  | No |
| sockets | DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent |  | No |
| reusablePlugs | DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent |  | No |
| plugObjectives | DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent |  | No |
| talentGrids | DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent |  | No |
| plugStates | DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent |  | No |
| objectives | DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent |  | No |
| perks | DictionaryComponentResponseOfint64AndDestinyItemPerksComponent |  | No |

## Usage Examples

### JavaScript
```javascript
// Example DestinyItemComponentSetOfint64 object
const example = {
  instances: null,
  renderData: null,
  stats: null,
  sockets: null,
  reusablePlugs: null,
  // ... more properties
};
```

### Python
```python
# Example DestinyItemComponentSetOfint64 object
example = {
    "instances": None,
    "renderData": None,
    "stats": None,
    "sockets": None,
    "reusablePlugs": None,
    # ... more properties
}
```

## Related Entities
- **DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemPerksComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemRenderComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemStatsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DestinyItemComponentSetOfint64":   {
      "type": "object",
      "properties": {
          "instances": {
              "x-destiny-component-type-dependency": "ItemInstances",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent"
          },
          "renderData": {
              "x-destiny-component-type-dependency": "ItemRenderData",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemRenderComponent"
          },
          "stats": {
              "x-destiny-component-type-dependency": "ItemStats",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemStatsComponent"
          },
          "sockets": {
              "x-destiny-component-type-dependency": "ItemSockets",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent"
          },
          "reusablePlugs": {
              "x-destiny-component-type-dependency": "ItemReusablePlugs",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent"
          },
          "plugObjectives": {
              "x-destiny-component-type-dependency": "ItemPlugObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent"
          },
          "talentGrids": {
              "x-destiny-component-type-dependency": "ItemTalentGrids",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent"
          },
          "plugStates": {
              "x-destiny-component-type-dependency": "ItemPlugStates",
              "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent"
          },
          "objectives": {
              "x-destiny-component-type-dependency": "ItemObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent"
          },
          "perks": {
              "x-destiny-component-type-dependency": "ItemPerks",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemPerksComponent"
          }
      }
  }
}
```
