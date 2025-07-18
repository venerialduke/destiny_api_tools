# Destiny.Definitions.DestinyVendorInteractionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorInteractionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A Vendor Interaction is a dialog shown by the vendor other than sale items or transfer screens. The vendor is showing you something, and asking you to reply to it by choosing an option or reward.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| interactionIndex | integer (int32) | The position of this interaction in its parent array. Note that this is NOT content agnostic, and should not be used as such. | No |
| replies | Array[Destiny.Definitions.DestinyVendorInteractionReplyDefinition] | The potential replies that the user can make to the interaction. | No |
| vendorCategoryIndex | integer (int32) | If >= 0, this is the category of sale items to show along with this interaction dialog. | No |
| questlineItemHash | integer (uint32) | If this interaction dialog is about a quest, this is the questline related to the interaction. You can use this to show the quest overview, or even the character's status with the quest if you use it to find the character's current Quest Step by checking their inventory against this questlineItemHash's DestinyInventoryItemDefinition.setData. | No |
| sackInteractionList | Array[Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition] | If this interaction is meant to show you sacks, this is the list of types of sacks to be shown. If empty, the interaction is not meant to show sacks. | No |
| uiInteractionType | integer (uint32) | A UI hint for the behavior of the interaction screen. This is useful to determine what type of interaction is occurring, such as a prompt to receive a rank up reward or a prompt to choose a reward for completing a quest. The hash isn't as useful as the Enum in retrospect, well what can you do. Try using interactionType instead. | No |
| interactionType | integer (int32) | The enumerated version of the possible UI hints for vendor interactions, which is a little easier to grok than the hash found in uiInteractionType. | No |
| rewardBlockLabel | string | If this interaction is displaying rewards, this is the text to use for the header of the reward-displaying section of the interaction. | No |
| rewardVendorCategoryIndex | integer (int32) | If the vendor's reward list is sourced from one of his categories, this is the index into the category array of items to show. | No |
| flavorLineOne | string | If the vendor interaction has flavor text, this is some of it. | No |
| flavorLineTwo | string | If the vendor interaction has flavor text, this is the rest of it. | No |
| headerDisplayProperties | object | The header for the interaction dialog. | No |
| instructions | string | The localized text telling the player what to do when they see this dialog. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorInteractionDefinition object
const example = {
  interactionIndex: 123,
  replies: [],
  vendorCategoryIndex: 123,
  questlineItemHash: 123,
  sackInteractionList: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorInteractionDefinition object
example = {
    "interactionIndex": 123,
    "replies": [],
    "vendorCategoryIndex": 123,
    "questlineItemHash": 123,
    "sackInteractionList": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorInteractionReplyDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition**: Referenced in this entity
- **Destiny.VendorInteractionType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorInteractionDefinition":   {
      "description": "A Vendor Interaction is a dialog shown by the vendor other than sale items or transfer screens. The vendor is showing you something, and asking you to reply to it by choosing an option or reward.",
      "type": "object",
      "properties": {
          "interactionIndex": {
              "format": "int32",
              "description": "The position of this interaction in its parent array. Note that this is NOT content agnostic, and should not be used as such.",
              "type": "integer"
          },
          "replies": {
              "description": "The potential replies that the user can make to the interaction.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorInteractionReplyDefinition"
              }
          },
          "vendorCategoryIndex": {
              "format": "int32",
              "description": "If >= 0, this is the category of sale items to show along with this interaction dialog.",
              "type": "integer"
          },
          "questlineItemHash": {
              "format": "uint32",
              "description": "If this interaction dialog is about a quest, this is the questline related to the interaction. You can use this to show the quest overview, or even the character's status with the quest if you use it to find the character's current Quest Step by checking their inventory against this questlineItemHash's DestinyInventoryItemDefinition.setData.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "sackInteractionList": {
              "description": "If this interaction is meant to show you sacks, this is the list of types of sacks to be shown. If empty, the interaction is not meant to show sacks.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorInteractionSackEntryDefinition"
              }
          },
          "uiInteractionType": {
              "format": "uint32",
              "description": "A UI hint for the behavior of the interaction screen. This is useful to determine what type of interaction is occurring, such as a prompt to receive a rank up reward or a prompt to choose a reward for completing a quest. The hash isn't as useful as the Enum in retrospect, well what can you do. Try using interactionType instead.",
              "type": "integer"
          },
          "interactionType": {
              "format": "int32",
              "description": "The enumerated version of the possible UI hints for vendor interactions, which is a little easier to grok than the hash found in uiInteractionType.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.VendorInteractionType"
              }
          },
          "rewardBlockLabel": {
              "description": "If this interaction is displaying rewards, this is the text to use for the header of the reward-displaying section of the interaction.",
              "type": "string"
          },
          "rewardVendorCategoryIndex": {
              "format": "int32",
              "description": "If the vendor's reward list is sourced from one of his categories, this is the index into the category array of items to show.",
              "type": "integer"
          },
          "flavorLineOne": {
              "description": "If the vendor interaction has flavor text, this is some of it.",
              "type": "string"
          },
          "flavorLineTwo": {
              "description": "If the vendor interaction has flavor text, this is the rest of it.",
              "type": "string"
          },
          "headerDisplayProperties": {
              "description": "The header for the interaction dialog.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "instructions": {
              "description": "The localized text telling the player what to do when they see this dialog.",
              "type": "string"
          }
      }
  }
}
```
