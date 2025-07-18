# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderactivitygraphdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| color | Destiny.Misc.DestinyColor |  | No |
| isPlayerElectedDifficultyNode | boolean |  | No |
| parentHash | integer (uint32) |  | No |
| children | Array[integer] |  | No |
| selfAndAllDescendantHashes | Array[integer] |  | No |
| relatedActivitySetHashes | Array[integer] |  | No |
| specificActivitySetHash | integer (uint32) |  | No |
| relatedActivityHashes | Array[integer] |  | No |
| relatedDirectorNodes | Array[Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference] |  | No |
| relatedInteractableActivities | Array[Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference] |  | No |
| relatedLocationHashes | Array[integer] |  | No |
| sortMatchmadeActivitiesToFront | boolean |  | No |
| enabledOnTreeTypesListEnum | Array[integer] |  | No |
| activityTreeChildSortMode | integer (int32) |  | No |
| sortPriority | integer (int32) |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition object
const example = {
  displayProperties: null,
  color: null,
  isPlayerElectedDifficultyNode: true,
  parentHash: 123,
  children: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition object
example = {
    "displayProperties": None,
    "color": None,
    "isPlayerElectedDifficultyNode": True,
    "parentHash": 123,
    "children": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyLocationDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition**: Referenced in this entity
- **Destiny.DestinyActivityTreeChildSortMode**: Referenced in this entity
- **Destiny.DestinyActivityTreeType**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "color": {
              "$ref": "#/definitions/Destiny.Misc.DestinyColor"
          },
          "isPlayerElectedDifficultyNode": {
              "type": "boolean"
          },
          "parentHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "children": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "selfAndAllDescendantHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "relatedActivitySetHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition"
              }
          },
          "specificActivitySetHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition"
              }
          },
          "relatedActivityHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "relatedDirectorNodes": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference"
              }
          },
          "relatedInteractableActivities": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference"
              }
          },
          "relatedLocationHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyLocationDefinition"
              }
          },
          "sortMatchmadeActivitiesToFront": {
              "type": "boolean"
          },
          "enabledOnTreeTypesListEnum": {
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.DestinyActivityTreeType"
                  }
              }
          },
          "activityTreeChildSortMode": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityTreeChildSortMode"
              }
          },
          "sortPriority": {
              "format": "int32",
              "type": "integer"
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
      "x-mobile-manifest-name": "FireteamFinderActivityGraphs"
  }
}
```
