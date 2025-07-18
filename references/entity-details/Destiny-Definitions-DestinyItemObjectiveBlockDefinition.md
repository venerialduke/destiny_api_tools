# Destiny.Definitions.DestinyItemObjectiveBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemObjectiveBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
An item can have objectives on it. In practice, these are the exclusive purview of "Quest Step" items: DestinyInventoryItemDefinitions that represent a specific step in a Quest.
Quest steps have 1:M objectives that we end up processing and returning in live data as DestinyQuestStatus data, and other useful information.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectiveHashes | Array[integer] | The hashes to Objectives (DestinyObjectiveDefinition) that are part of this Quest Step, in the order that they should be rendered. | No |
| displayActivityHashes | Array[integer] | For every entry in objectiveHashes, there is a corresponding entry in this array at the same index. If the objective is meant to be associated with a specific DestinyActivityDefinition, there will be a valid hash at that index. Otherwise, it will be invalid (0).
Rendered somewhat obsolete by perObjectiveDisplayProperties, which currently has much the same information but may end up with more info in the future. | No |
| requireFullObjectiveCompletion | boolean | If True, all objectives must be completed for the step to be completed. If False, any one objective can be completed for the step to be completed. | No |
| questlineItemHash | integer (uint32) | The hash for the DestinyInventoryItemDefinition representing the Quest to which this Quest Step belongs. | No |
| narrative | string | The localized string for narrative text related to this quest step, if any. | No |
| objectiveVerbName | string | The localized string describing an action to be performed associated with the objectives, if any. | No |
| questTypeIdentifier | string | The identifier for the type of quest being performed, if any. Not associated with any fixed definition, yet. | No |
| questTypeHash | integer (uint32) | A hashed value for the questTypeIdentifier, because apparently I like to be redundant. | No |
| perObjectiveDisplayProperties | Array[Destiny.Definitions.DestinyObjectiveDisplayProperties] | One entry per Objective on the item, it will have related display information. | No |
| displayAsStatTracker | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemObjectiveBlockDefinition object
const example = {
  objectiveHashes: [],
  displayActivityHashes: [],
  requireFullObjectiveCompletion: true,
  questlineItemHash: 123,
  narrative: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemObjectiveBlockDefinition object
example = {
    "objectiveHashes": [],
    "displayActivityHashes": [],
    "requireFullObjectiveCompletion": True,
    "questlineItemHash": 123,
    "narrative": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDisplayProperties**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemObjectiveBlockDefinition":   {
      "description": "An item can have objectives on it. In practice, these are the exclusive purview of \"Quest Step\" items: DestinyInventoryItemDefinitions that represent a specific step in a Quest.\r\nQuest steps have 1:M objectives that we end up processing and returning in live data as DestinyQuestStatus data, and other useful information.",
      "type": "object",
      "properties": {
          "objectiveHashes": {
              "description": "The hashes to Objectives (DestinyObjectiveDefinition) that are part of this Quest Step, in the order that they should be rendered.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "displayActivityHashes": {
              "description": "For every entry in objectiveHashes, there is a corresponding entry in this array at the same index. If the objective is meant to be associated with a specific DestinyActivityDefinition, there will be a valid hash at that index. Otherwise, it will be invalid (0).\r\nRendered somewhat obsolete by perObjectiveDisplayProperties, which currently has much the same information but may end up with more info in the future.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "requireFullObjectiveCompletion": {
              "description": "If True, all objectives must be completed for the step to be completed. If False, any one objective can be completed for the step to be completed.",
              "type": "boolean"
          },
          "questlineItemHash": {
              "format": "uint32",
              "description": "The hash for the DestinyInventoryItemDefinition representing the Quest to which this Quest Step belongs.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "narrative": {
              "description": "The localized string for narrative text related to this quest step, if any.",
              "type": "string"
          },
          "objectiveVerbName": {
              "description": "The localized string describing an action to be performed associated with the objectives, if any.",
              "type": "string"
          },
          "questTypeIdentifier": {
              "description": "The identifier for the type of quest being performed, if any. Not associated with any fixed definition, yet.",
              "type": "string"
          },
          "questTypeHash": {
              "format": "uint32",
              "description": "A hashed value for the questTypeIdentifier, because apparently I like to be redundant.",
              "type": "integer"
          },
          "perObjectiveDisplayProperties": {
              "description": "One entry per Objective on the item, it will have related display information.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDisplayProperties"
              }
          },
          "displayAsStatTracker": {
              "type": "boolean"
          }
      }
  }
}
```
