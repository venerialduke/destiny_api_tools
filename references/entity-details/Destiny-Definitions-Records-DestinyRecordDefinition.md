# Destiny.Definitions.Records.DestinyRecordDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyrecorddefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| scope | integer (int32) | Indicates whether this Record's state is determined on a per-character or on an account-wide basis. | No |
| presentationInfo | Destiny.Definitions.Presentation.DestinyPresentationChildBlock |  | No |
| loreHash | integer (uint32) |  | No |
| objectiveHashes | Array[integer] |  | No |
| recordValueStyle | integer (int32) |  | No |
| forTitleGilding | boolean |  | No |
| shouldShowLargeIcons | boolean | A hint to show a large icon for a reward | No |
| titleInfo | Destiny.Definitions.Records.DestinyRecordTitleBlock |  | No |
| completionInfo | Destiny.Definitions.Records.DestinyRecordCompletionBlock |  | No |
| stateInfo | Destiny.Definitions.Records.SchemaRecordStateBlock |  | No |
| requirements | Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock |  | No |
| expirationInfo | Destiny.Definitions.Records.DestinyRecordExpirationBlock |  | No |
| intervalInfo | object | Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval | No |
| rewardItems | Array[Destiny.DestinyItemQuantity] | If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.
 However, note that some records intentionally have "hidden" rewards. These will not be returned in this list. | No |
| recordTypeName | string | A display name for the type of record this is (Triumphs, Lore, Medals, Seasonal Challenge, etc.). | No |
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
// Example Destiny.Definitions.Records.DestinyRecordDefinition object
const example = {
  displayProperties: null,
  scope: 123,
  presentationInfo: null,
  loreHash: 123,
  objectiveHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordDefinition object
example = {
    "displayProperties": None,
    "scope": 123,
    "presentationInfo": None,
    "loreHash": 123,
    "objectiveHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity
- **Destiny.Definitions.Lore.DestinyLoreDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationChildBlock**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordCompletionBlock**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordExpirationBlock**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordIntervalBlock**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordTitleBlock**: Referenced in this entity
- **Destiny.Definitions.Records.SchemaRecordStateBlock**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.DestinyItemQuantity**: Referenced in this entity
- **Destiny.DestinyPresentationNodeType**: Referenced in this entity
- **Destiny.DestinyRecordValueStyle**: Referenced in this entity
- **Destiny.DestinyScope**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "scope": {
              "format": "int32",
              "description": "Indicates whether this Record's state is determined on a per-character or on an account-wide basis.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyScope"
              }
          },
          "presentationInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationChildBlock"
          },
          "loreHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Lore.DestinyLoreDefinition"
              }
          },
          "objectiveHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "recordValueStyle": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyRecordValueStyle"
              }
          },
          "forTitleGilding": {
              "type": "boolean"
          },
          "shouldShowLargeIcons": {
              "description": "A hint to show a large icon for a reward",
              "type": "boolean"
          },
          "titleInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordTitleBlock"
          },
          "completionInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordCompletionBlock"
          },
          "stateInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Records.SchemaRecordStateBlock"
          },
          "requirements": {
              "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock"
          },
          "expirationInfo": {
              "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordExpirationBlock"
          },
          "intervalInfo": {
              "description": "Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordIntervalBlock"
                  }
              ]
          },
          "rewardItems": {
              "description": "If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.\r\n However, note that some records intentionally have \"hidden\" rewards. These will not be returned in this list.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          },
          "recordTypeName": {
              "description": "A display name for the type of record this is (Triumphs, Lore, Medals, Seasonal Challenge, etc.).",
              "type": "string"
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
      "x-mobile-manifest-name": "Records"
  }
}
```
