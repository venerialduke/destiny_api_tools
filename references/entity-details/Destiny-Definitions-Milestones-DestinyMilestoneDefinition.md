# Destiny.Definitions.Milestones.DestinyMilestoneDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Milestones are an in-game concept where they're attempting to tell you what you can do next in-game.
If that sounds a lot like Advisors in Destiny 1, it is! So we threw out Advisors in the Destiny 2 API and tacked all of the data we would have put on Advisors onto Milestones instead.
Each Milestone represents something going on in the game right now:
- A "ritual activity" you can perform, like nightfall
- A "special event" that may have activities related to it, like Taco Tuesday (there's no Taco Tuesday in Destiny 2)
- A checklist you can fulfill, like helping your Clan complete all of its weekly objectives
- A tutorial quest you can play through, like the introduction to the Crucible.
Most of these milestones appear in game as well. Some of them are BNet only, because we're so extra. You're welcome.
There are some important caveats to understand about how we currently render Milestones and their deficiencies. The game currently doesn't have any content that actually tells you oughtright *what* the Milestone is: that is to say, what you'll be doing. The best we get is either a description of the overall Milestone, or of the Quest that the Milestone is having you partake in: which is usually something that assumes you already know what it's talking about, like "Complete 5 Challenges". 5 Challenges for what? What's a challenge? These are not questions that the Milestone data will answer for you unfortunately.
This isn't great, and in the future I'd like to add some custom text to give you more contextual information to pass on to your users. But for now, you can do what we do to render what little display info we do have:
Start by looking at the currently active quest (ideally, you've fetched DestinyMilestone or DestinyPublicMilestone data from the API, so you know the currently active quest for the Milestone in question). Look up the Quests property in the Milestone Definition, and check if it has display properties. If it does, show that as the description of the Milestone. If it doesn't, fall back on the Milestone's description.
This approach will let you avoid, whenever possible, the even less useful (and sometimes nonexistant) milestone-level names and descriptions.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| displayPreference | integer (int32) | A hint to the UI to indicate what to show as the display properties for this Milestone when showing "Live" milestone data. Feel free to show more than this if desired: this hint is meant to simplify our own UI, but it may prove useful to you as well. | No |
| image | string | A custom image someone made just for the milestone. Isn't that special? | No |
| milestoneType | integer (int32) | An enumeration listing one of the possible types of milestones. Check out the DestinyMilestoneType enum for more info! | No |
| recruitable | boolean | If True, then the Milestone has been integrated with BNet's recruiting feature. | No |
| friendlyName | string | If the milestone has a friendly identifier for association with other features - such as Recruiting - that identifier can be found here. This is "friendly" in that it looks better in a URL than whatever the identifier for the Milestone actually is. | No |
| showInExplorer | boolean | If TRUE, this entry should be returned in the list of milestones for the "Explore Destiny" (i.e. new BNet homepage) features of Bungie.net (as long as the underlying event is active) Note that this is a property specifically used by BNet and the companion app for the "Live Events" feature of the front page/welcome view: it's not a reflection of what you see in-game. | No |
| showInMilestones | boolean | Determines whether we'll show this Milestone in the user's personal Milestones list. | No |
| explorePrioritizesActivityImage | boolean | If TRUE, "Explore Destiny" (the front page of BNet and the companion app) prioritize using the activity image over any overriding Quest or Milestone image provided. This unfortunate hack is brought to you by Trials of The Nine. | No |
| hasPredictableDates | boolean | A shortcut for clients - and the server - to understand whether we can predict the start and end dates for this event. In practice, there are multiple ways that an event could have predictable date ranges, but not all events will be able to be predicted via any mechanism (for instance, events that are manually triggered on and off) | No |
| quests | object | The full set of possible Quests that give the overview of the Milestone event/activity in question. Only one of these can be active at a time for a given Conceptual Milestone, but many of them may be "available" for the user to choose from. (for instance, with Milestones you can choose from the three available Quests, but only one can be active at a time) Keyed by the quest item.
As of Forsaken (~September 2018), Quest-style Milestones are being removed for many types of activities. There will likely be further revisions to the Milestone concept in the future. | No |
| rewards | object | If this milestone can provide rewards, this will define the categories into which the individual reward entries are placed.
This is keyed by the Category's hash, which is only guaranteed to be unique within a given Milestone. | No |
| vendorsDisplayTitle | string | If you're going to show Vendors for the Milestone, you can use this as a localized "header" for the section where you show that vendor data. It'll provide a more context-relevant clue about what the vendor's role is in the Milestone. | No |
| vendors | Array[Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition] | Sometimes, milestones will have rewards provided by Vendors. This definition gives the information needed to understand which vendors are relevant, the order in which they should be returned if order matters, and the conditions under which the Vendor is relevant to the user. | No |
| values | object | Sometimes, milestones will have arbitrary values associated with them that are of interest to us or to third party developers. This is the collection of those values' definitions, keyed by the identifier of the value and providing useful definition information such as localizable names and descriptions for the value. | No |
| isInGameMilestone | boolean | Some milestones are explicit objectives that you can see and interact with in the game. Some milestones are more conceptual, built by BNet to help advise you on activities and events that happen in-game but that aren't explicitly shown in game as Milestones. If this is TRUE, you can see this as a milestone in the game. If this is FALSE, it's an event or activity you can participate in, but you won't see it as a Milestone in the game's UI. | No |
| activities | Array[Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition] | A Milestone can now be represented by one or more activities directly (without a backing Quest), and that activity can have many challenges, modifiers, and related to it. | No |
| defaultOrder | integer (int32) |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneDefinition object
const example = {
  displayProperties: null,
  displayPreference: 123,
  image: "example value",
  milestoneType: 123,
  recruitable: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneDefinition object
example = {
    "displayProperties": None,
    "displayPreference": 123,
    "image": "example value",
    "milestoneType": 123,
    "recruitable": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneType**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneDefinition":   {
      "description": "Milestones are an in-game concept where they're attempting to tell you what you can do next in-game.\r\nIf that sounds a lot like Advisors in Destiny 1, it is! So we threw out Advisors in the Destiny 2 API and tacked all of the data we would have put on Advisors onto Milestones instead.\r\nEach Milestone represents something going on in the game right now:\r\n- A \"ritual activity\" you can perform, like nightfall\r\n- A \"special event\" that may have activities related to it, like Taco Tuesday (there's no Taco Tuesday in Destiny 2)\r\n- A checklist you can fulfill, like helping your Clan complete all of its weekly objectives\r\n- A tutorial quest you can play through, like the introduction to the Crucible.\r\nMost of these milestones appear in game as well. Some of them are BNet only, because we're so extra. You're welcome.\r\nThere are some important caveats to understand about how we currently render Milestones and their deficiencies. The game currently doesn't have any content that actually tells you oughtright *what* the Milestone is: that is to say, what you'll be doing. The best we get is either a description of the overall Milestone, or of the Quest that the Milestone is having you partake in: which is usually something that assumes you already know what it's talking about, like \"Complete 5 Challenges\". 5 Challenges for what? What's a challenge? These are not questions that the Milestone data will answer for you unfortunately.\r\nThis isn't great, and in the future I'd like to add some custom text to give you more contextual information to pass on to your users. But for now, you can do what we do to render what little display info we do have:\r\nStart by looking at the currently active quest (ideally, you've fetched DestinyMilestone or DestinyPublicMilestone data from the API, so you know the currently active quest for the Milestone in question). Look up the Quests property in the Milestone Definition, and check if it has display properties. If it does, show that as the description of the Milestone. If it doesn't, fall back on the Milestone's description.\r\nThis approach will let you avoid, whenever possible, the even less useful (and sometimes nonexistant) milestone-level names and descriptions.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "displayPreference": {
              "format": "int32",
              "description": "A hint to the UI to indicate what to show as the display properties for this Milestone when showing \"Live\" milestone data. Feel free to show more than this if desired: this hint is meant to simplify our own UI, but it may prove useful to you as well.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference"
              }
          },
          "image": {
              "description": "A custom image someone made just for the milestone. Isn't that special?",
              "type": "string"
          },
          "milestoneType": {
              "format": "int32",
              "description": "An enumeration listing one of the possible types of milestones. Check out the DestinyMilestoneType enum for more info!",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.Milestones.DestinyMilestoneType"
              }
          },
          "recruitable": {
              "description": "If True, then the Milestone has been integrated with BNet's recruiting feature.",
              "type": "boolean"
          },
          "friendlyName": {
              "description": "If the milestone has a friendly identifier for association with other features - such as Recruiting - that identifier can be found here. This is \"friendly\" in that it looks better in a URL than whatever the identifier for the Milestone actually is.",
              "type": "string"
          },
          "showInExplorer": {
              "description": "If TRUE, this entry should be returned in the list of milestones for the \"Explore Destiny\" (i.e. new BNet homepage) features of Bungie.net (as long as the underlying event is active) Note that this is a property specifically used by BNet and the companion app for the \"Live Events\" feature of the front page/welcome view: it's not a reflection of what you see in-game.",
              "type": "boolean"
          },
          "showInMilestones": {
              "description": "Determines whether we'll show this Milestone in the user's personal Milestones list.",
              "type": "boolean"
          },
          "explorePrioritizesActivityImage": {
              "description": "If TRUE, \"Explore Destiny\" (the front page of BNet and the companion app) prioritize using the activity image over any overriding Quest or Milestone image provided. This unfortunate hack is brought to you by Trials of The Nine.",
              "type": "boolean"
          },
          "hasPredictableDates": {
              "description": "A shortcut for clients - and the server - to understand whether we can predict the start and end dates for this event. In practice, there are multiple ways that an event could have predictable date ranges, but not all events will be able to be predicted via any mechanism (for instance, events that are manually triggered on and off)",
              "type": "boolean"
          },
          "quests": {
              "description": "The full set of possible Quests that give the overview of the Milestone event/activity in question. Only one of these can be active at a time for a given Conceptual Milestone, but many of them may be \"available\" for the user to choose from. (for instance, with Milestones you can choose from the three available Quests, but only one can be active at a time) Keyed by the quest item.\r\nAs of Forsaken (~September 2018), Quest-style Milestones are being removed for many types of activities. There will likely be further revisions to the Milestone concept in the future.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition"
              }
          },
          "rewards": {
              "description": "If this milestone can provide rewards, this will define the categories into which the individual reward entries are placed.\r\nThis is keyed by the Category's hash, which is only guaranteed to be unique within a given Milestone.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition"
              }
          },
          "vendorsDisplayTitle": {
              "description": "If you're going to show Vendors for the Milestone, you can use this as a localized \"header\" for the section where you show that vendor data. It'll provide a more context-relevant clue about what the vendor's role is in the Milestone.",
              "type": "string"
          },
          "vendors": {
              "description": "Sometimes, milestones will have rewards provided by Vendors. This definition gives the information needed to understand which vendors are relevant, the order in which they should be returned if order matters, and the conditions under which the Vendor is relevant to the user.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition"
              }
          },
          "values": {
              "description": "Sometimes, milestones will have arbitrary values associated with them that are of interest to us or to third party developers. This is the collection of those values' definitions, keyed by the identifier of the value and providing useful definition information such as localizable names and descriptions for the value.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition"
              }
          },
          "isInGameMilestone": {
              "description": "Some milestones are explicit objectives that you can see and interact with in the game. Some milestones are more conceptual, built by BNet to help advise you on activities and events that happen in-game but that aren't explicitly shown in game as Milestones. If this is TRUE, you can see this as a milestone in the game. If this is FALSE, it's an event or activity you can participate in, but you won't see it as a Milestone in the game's UI.",
              "type": "boolean"
          },
          "activities": {
              "description": "A Milestone can now be represented by one or more activities directly (without a backing Quest), and that activity can have many challenges, modifiers, and related to it.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition"
              }
          },
          "defaultOrder": {
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
      "x-mobile-manifest-name": "Milestones"
  }
}
```
