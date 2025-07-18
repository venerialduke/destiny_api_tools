# Destiny.Components.Collectibles.DestinyProfileCollectiblesComponent

## Entity Information
- **Entity Name**: Destiny.Components.Collectibles.DestinyProfileCollectiblesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyprofilecollectiblescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| recentCollectibleHashes | Array[integer] | The list of collectibles determined by the game as having been "recently" acquired. | No |
| newnessFlaggedCollectibleHashes | Array[integer] | The list of collectibles determined by the game as having been "recently" acquired.
The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is. | No |
| collectibles | object |  | No |
| collectionCategoriesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Collection categories. | No |
| collectionBadgesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Collection Badges. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Collectibles.DestinyProfileCollectiblesComponent object
const example = {
  recentCollectibleHashes: [],
  newnessFlaggedCollectibleHashes: [],
  collectibles: null,
  collectionCategoriesRootNodeHash: 123,
  collectionBadgesRootNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Collectibles.DestinyProfileCollectiblesComponent object
example = {
    "recentCollectibleHashes": [],
    "newnessFlaggedCollectibleHashes": [],
    "collectibles": None,
    "collectionCategoriesRootNodeHash": 123,
    "collectionBadgesRootNodeHash": 123,
}
```

## Related Entities
- **Destiny.Components.Collectibles.DestinyCollectibleComponent**: Referenced in this entity
- **Destiny.Definitions.Collectibles.DestinyCollectibleDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Collectibles.DestinyProfileCollectiblesComponent":   {
      "type": "object",
      "properties": {
          "recentCollectibleHashes": {
              "description": "The list of collectibles determined by the game as having been \"recently\" acquired.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleDefinition"
              }
          },
          "newnessFlaggedCollectibleHashes": {
              "description": "The list of collectibles determined by the game as having been \"recently\" acquired.\r\nThe game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleDefinition"
              }
          },
          "collectibles": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Components.Collectibles.DestinyCollectibleComponent"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleDefinition"
              }
          },
          "collectionCategoriesRootNodeHash": {
              "format": "uint32",
              "description": "The hash for the root presentation node definition of Collection categories.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "collectionBadgesRootNodeHash": {
              "format": "uint32",
              "description": "The hash for the root presentation node definition of Collection Badges.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Collectibles"
  }
}
```
