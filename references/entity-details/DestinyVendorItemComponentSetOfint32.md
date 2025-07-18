# DestinyVendorItemComponentSetOfint32

## Entity Information
- **Entity Name**: DestinyVendorItemComponentSetOfint32
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyvendoritemcomponentsetofint32 data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemComponents | DictionaryComponentResponseOfint32AndDestinyItemComponent |  | No |
| instances | DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent |  | No |
| renderData | DictionaryComponentResponseOfint32AndDestinyItemRenderComponent |  | No |
| stats | DictionaryComponentResponseOfint32AndDestinyItemStatsComponent |  | No |
| sockets | DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent |  | No |
| reusablePlugs | DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent |  | No |
| plugObjectives | DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent |  | No |
| talentGrids | DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent |  | No |
| plugStates | DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent |  | No |
| objectives | DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent |  | No |
| perks | DictionaryComponentResponseOfint32AndDestinyItemPerksComponent |  | No |

## Usage Examples

### JavaScript
```javascript
// Example DestinyVendorItemComponentSetOfint32 object
const example = {
  itemComponents: null,
  instances: null,
  renderData: null,
  stats: null,
  sockets: null,
  // ... more properties
};
```

### Python
```python
# Example DestinyVendorItemComponentSetOfint32 object
example = {
    "itemComponents": None,
    "instances": None,
    "renderData": None,
    "stats": None,
    "sockets": None,
    # ... more properties
}
```

## Related Entities
- **DictionaryComponentResponseOfint32AndDestinyItemComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemPerksComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemRenderComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemStatsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DestinyVendorItemComponentSetOfint32":   {
      "type": "object",
      "properties": {
          "itemComponents": {
              "x-destiny-component-type-dependency": "ItemCommonData",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemComponent"
          },
          "instances": {
              "x-destiny-component-type-dependency": "ItemInstances",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent"
          },
          "renderData": {
              "x-destiny-component-type-dependency": "ItemRenderData",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemRenderComponent"
          },
          "stats": {
              "x-destiny-component-type-dependency": "ItemStats",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemStatsComponent"
          },
          "sockets": {
              "x-destiny-component-type-dependency": "ItemSockets",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent"
          },
          "reusablePlugs": {
              "x-destiny-component-type-dependency": "ItemReusablePlugs",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent"
          },
          "plugObjectives": {
              "x-destiny-component-type-dependency": "ItemPlugObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent"
          },
          "talentGrids": {
              "x-destiny-component-type-dependency": "ItemTalentGrids",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent"
          },
          "plugStates": {
              "x-destiny-component-type-dependency": "ItemPlugStates",
              "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent"
          },
          "objectives": {
              "x-destiny-component-type-dependency": "ItemObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent"
          },
          "perks": {
              "x-destiny-component-type-dependency": "ItemPerks",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemPerksComponent"
          }
      }
  }
}
```
