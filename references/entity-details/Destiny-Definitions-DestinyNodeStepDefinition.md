# Destiny.Definitions.DestinyNodeStepDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyNodeStepDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This defines the properties of a "Talent Node Step". When you see a talent node in game, the actual visible properties that you see (its icon, description, the perks and stats it provides) are not provided by the Node itself, but rather by the currently active Step on the node.
When a Talent Node is activated, the currently active step's benefits are conferred upon the item and character.
The currently active step on talent nodes are determined when an item is first instantiated. Sometimes it is random, sometimes it is more deterministic (particularly when a node has only a single step).
Note that, when dealing with Talent Node Steps, you must ensure that you have the latest version of content. stepIndex and nodeStepHash - two ways of identifying the step within a node - are both content version dependent, and thus are subject to change between content updates.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | These are the display properties actually used to render the Talent Node. The currently active step's displayProperties are shown. | No |
| stepIndex | integer (int32) | The index of this step in the list of Steps on the Talent Node.
Unfortunately, this is the closest thing we have to an identifier for the Step: steps are not provided a content version agnostic identifier. This means that, when you are dealing with talent nodes, you will need to first ensure that you have the latest version of content. | No |
| nodeStepHash | integer (uint32) | The hash of this node step. Unfortunately, while it can be used to uniquely identify the step within a node, it is also content version dependent and should not be relied on without ensuring you have the latest vesion of content. | No |
| interactionDescription | string | If you can interact with this node in some way, this is the localized description of that interaction. | No |
| damageType | integer (int32) | An enum representing a damage type granted by activating this step, if any. | No |
| damageTypeHash | integer (uint32) | If the step provides a damage type, this will be the hash identifier used to look up the damage type's DestinyDamageTypeDefinition. | No |
| activationRequirement | object | If the step has requirements for activation (they almost always do, if nothing else than for the Talent Grid's Progression to have reached a certain level), they will be defined here. | No |
| canActivateNextStep | boolean | There was a time when talent nodes could be activated multiple times, and the effects of subsequent Steps would be compounded on each other, essentially "upgrading" the node. We have moved away from this, but theoretically the capability still exists.
I continue to return this in case it is used in the future: if true and this step is the current step in the node, you are allowed to activate the node a second time to receive the benefits of the next step in the node, which will then become the active step. | No |
| nextStepIndex | integer (int32) | The stepIndex of the next step in the talent node, or -1 if this is the last step or if the next step to be chosen is random.
This doesn't really matter anymore unless canActivateNextStep begins to be used again. | No |
| isNextStepRandom | boolean | If true, the next step to be chosen is random, and if you're allowed to activate the next step. (if canActivateNextStep = true) | No |
| perkHashes | Array[integer] | The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are applied when this step is active. Perks provide a variety of benefits and modifications - examine DestinySandboxPerkDefinition to learn more. | No |
| startProgressionBarAtProgress | integer (int32) | When the Talent Grid's progression reaches this value, the circular "progress bar" that surrounds the talent node should be shown.
This also indicates the lower bound of said progress bar, with the upper bound being the progress required to reach activationRequirement.gridLevel. (at some point I should precalculate the upper bound and put it in the definition to save people time) | No |
| statHashes | Array[integer] | When the step provides stat benefits on the item or character, this is the list of hash identifiers for stats (DestinyStatDefinition) that are provided. | No |
| affectsQuality | boolean | If this is true, the step affects the item's Quality in some way. See DestinyInventoryItemDefinition for more information about the meaning of Quality. I already made a joke about Zen and the Art of Motorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again. Oops too late | No |
| stepGroups | object | In Destiny 1, the Armory's Perk Filtering was driven by a concept of TalentNodeStepGroups: categorizations of talent nodes based on their functionality. While the Armory isn't a BNet-facing thing for now, and the new Armory will need to account for Sockets rather than Talent Nodes, this categorization capability feels useful enough to still keep around. | No |
| affectsLevel | boolean | If true, this step can affect the level of the item. See DestinyInventoryItemDefintion for more information about item levels and their effect on stats. | No |
| socketReplacements | Array[Destiny.Definitions.DestinyNodeSocketReplaceResponse] | If this step is activated, this will be a list of information used to replace socket items with new Plugs. See DestinyInventoryItemDefinition for more information about sockets and plugs. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyNodeStepDefinition object
const example = {
  displayProperties: null,
  stepIndex: 123,
  nodeStepHash: 123,
  interactionDescription: "example value",
  damageType: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyNodeStepDefinition object
example = {
    "displayProperties": None,
    "stepIndex": 123,
    "nodeStepHash": 123,
    "interactionDescription": "example value",
    "damageType": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.DamageType**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDamageTypeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyNodeActivationRequirement**: Referenced in this entity
- **Destiny.Definitions.DestinyNodeSocketReplaceResponse**: Referenced in this entity
- **Destiny.Definitions.DestinySandboxPerkDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyTalentNodeStepGroups**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyNodeStepDefinition":   {
      "description": "This defines the properties of a \"Talent Node Step\". When you see a talent node in game, the actual visible properties that you see (its icon, description, the perks and stats it provides) are not provided by the Node itself, but rather by the currently active Step on the node.\r\nWhen a Talent Node is activated, the currently active step's benefits are conferred upon the item and character.\r\nThe currently active step on talent nodes are determined when an item is first instantiated. Sometimes it is random, sometimes it is more deterministic (particularly when a node has only a single step).\r\nNote that, when dealing with Talent Node Steps, you must ensure that you have the latest version of content. stepIndex and nodeStepHash - two ways of identifying the step within a node - are both content version dependent, and thus are subject to change between content updates.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "These are the display properties actually used to render the Talent Node. The currently active step's displayProperties are shown.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "stepIndex": {
              "format": "int32",
              "description": "The index of this step in the list of Steps on the Talent Node.\r\nUnfortunately, this is the closest thing we have to an identifier for the Step: steps are not provided a content version agnostic identifier. This means that, when you are dealing with talent nodes, you will need to first ensure that you have the latest version of content.",
              "type": "integer"
          },
          "nodeStepHash": {
              "format": "uint32",
              "description": "The hash of this node step. Unfortunately, while it can be used to uniquely identify the step within a node, it is also content version dependent and should not be relied on without ensuring you have the latest vesion of content.",
              "type": "integer"
          },
          "interactionDescription": {
              "description": "If you can interact with this node in some way, this is the localized description of that interaction.",
              "type": "string"
          },
          "damageType": {
              "format": "int32",
              "description": "An enum representing a damage type granted by activating this step, if any.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DamageType"
              }
          },
          "damageTypeHash": {
              "format": "uint32",
              "description": "If the step provides a damage type, this will be the hash identifier used to look up the damage type's DestinyDamageTypeDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDamageTypeDefinition"
              }
          },
          "activationRequirement": {
              "description": "If the step has requirements for activation (they almost always do, if nothing else than for the Talent Grid's Progression to have reached a certain level), they will be defined here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyNodeActivationRequirement"
                  }
              ]
          },
          "canActivateNextStep": {
              "description": "There was a time when talent nodes could be activated multiple times, and the effects of subsequent Steps would be compounded on each other, essentially \"upgrading\" the node. We have moved away from this, but theoretically the capability still exists.\r\nI continue to return this in case it is used in the future: if true and this step is the current step in the node, you are allowed to activate the node a second time to receive the benefits of the next step in the node, which will then become the active step.",
              "type": "boolean"
          },
          "nextStepIndex": {
              "format": "int32",
              "description": "The stepIndex of the next step in the talent node, or -1 if this is the last step or if the next step to be chosen is random.\r\nThis doesn't really matter anymore unless canActivateNextStep begins to be used again.",
              "type": "integer"
          },
          "isNextStepRandom": {
              "description": "If true, the next step to be chosen is random, and if you're allowed to activate the next step. (if canActivateNextStep = true)",
              "type": "boolean"
          },
          "perkHashes": {
              "description": "The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are applied when this step is active. Perks provide a variety of benefits and modifications - examine DestinySandboxPerkDefinition to learn more.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinySandboxPerkDefinition"
              }
          },
          "startProgressionBarAtProgress": {
              "format": "int32",
              "description": "When the Talent Grid's progression reaches this value, the circular \"progress bar\" that surrounds the talent node should be shown.\r\nThis also indicates the lower bound of said progress bar, with the upper bound being the progress required to reach activationRequirement.gridLevel. (at some point I should precalculate the upper bound and put it in the definition to save people time)",
              "type": "integer"
          },
          "statHashes": {
              "description": "When the step provides stat benefits on the item or character, this is the list of hash identifiers for stats (DestinyStatDefinition) that are provided.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "affectsQuality": {
              "description": "If this is true, the step affects the item's Quality in some way. See DestinyInventoryItemDefinition for more information about the meaning of Quality. I already made a joke about Zen and the Art of Motorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again. Oops too late",
              "type": "boolean"
          },
          "stepGroups": {
              "description": "In Destiny 1, the Armory's Perk Filtering was driven by a concept of TalentNodeStepGroups: categorizations of talent nodes based on their functionality. While the Armory isn't a BNet-facing thing for now, and the new Armory will need to account for Sockets rather than Talent Nodes, this categorization capability feels useful enough to still keep around.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyTalentNodeStepGroups"
                  }
              ]
          },
          "affectsLevel": {
              "description": "If true, this step can affect the level of the item. See DestinyInventoryItemDefintion for more information about item levels and their effect on stats.",
              "type": "boolean"
          },
          "socketReplacements": {
              "description": "If this step is activated, this will be a list of information used to replace socket items with new Plugs. See DestinyInventoryItemDefinition for more information about sockets and plugs.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyNodeSocketReplaceResponse"
              }
          }
      }
  }
}
```
