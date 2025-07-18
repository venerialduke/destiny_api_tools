# Destiny.Components.Collectibles.DestinyCollectiblesComponent

## Entity Information
- **Entity Name**: Destiny.Components.Collectibles.DestinyCollectiblesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycollectiblescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| collectibles | object |  | No |
| collectionCategoriesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Collection categories. | No |
| collectionBadgesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Collection Badges. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Collectibles.DestinyCollectiblesComponent object
const example = {
  collectibles: null,
  collectionCategoriesRootNodeHash: 123,
  collectionBadgesRootNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Collectibles.DestinyCollectiblesComponent object
example = {
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
  "Destiny.Components.Collectibles.DestinyCollectiblesComponent":   {
      "type": "object",
      "properties": {
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
