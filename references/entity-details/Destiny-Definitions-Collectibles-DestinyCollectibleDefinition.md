# Destiny.Definitions.Collectibles.DestinyCollectibleDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Collectibles.DestinyCollectibleDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Defines a

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| scope | integer (int32) | Indicates whether the state of this Collectible is determined on a per-character or on an account-wide basis. | No |
| sourceString | string | A human readable string for a hint about how to acquire the item. | No |
| sourceHash | integer (uint32) | This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources.
I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though.
This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data. | No |
| itemHash | integer (uint32) |  | No |
| acquisitionInfo | Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock |  | No |
| stateInfo | Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock |  | No |
| presentationInfo | Destiny.Definitions.Presentation.DestinyPresentationChildBlock |  | No |
| presentationNodeType | integer (int32) |  | No |
| traitIds | Array[string] |  | No |
| traitHashes | Array[integer] |  | No |
| parentNodeHashes | Array[integer] | A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Collectibles.DestinyCollectibleDefinition object
const example = {
  displayProperties: null,
  scope: 123,
  sourceString: "example value",
  sourceHash: 123,
  itemHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Collectibles.DestinyCollectibleDefinition object
example = {
    "displayProperties": None,
    "scope": 123,
    "sourceString": "example value",
    "sourceHash": 123,
    "itemHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock**: Referenced in this entity
- **Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationChildBlock**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.DestinyPresentationNodeType**: Referenced in this entity
- **Destiny.DestinyScope**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Collectibles.DestinyCollectibleDefinition":   {
      "description": "Defines a",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "scope": {
              "format": "int32",
              "description": "Indicates whether the state of this Collectible is determined on a per-character or on an account-wide basis.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyScope"
              }
          },
          "sourceString": {
              "description": "A human readable string for a hint about how to acquire the item.",
              "type": "string"
          },
          "sourceHash": {
              "format": "uint32",
              "description": "This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources.\r\nI can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though.\r\nThis hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.",
              "type": "integer"
          },
          "itemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "acquisitionInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock"
          },
          "stateInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock"
          },
          "presentationInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationChildBlock"
          },
          "presentationNodeType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationNodeType"
              }
          },
          "traitIds": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "traitHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Traits.DestinyTraitDefinition"
              }
          },
          "parentNodeHashes": {
              "description": "A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
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
      "x-mobile-manifest-name": "Collectibles"
  }
}
```
