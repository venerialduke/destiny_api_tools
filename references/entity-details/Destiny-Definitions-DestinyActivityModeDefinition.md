# Destiny.Definitions.DestinyActivityModeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityModeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
This definition represents an "Activity Mode" as it exists in the Historical Stats endpoints. An individual Activity Mode represents a collection of activities that are played in a certain way. For example, Nightfall Strikes are part of a "Nightfall" activity mode, and any activities played as the PVP mode "Clash" are part of the "Clash activity mode.
Activity modes are nested under each other in a hierarchy, so that if you ask for - for example - "AllPvP", you will get any PVP activities that the user has played, regardless of what specific PVP mode was being played.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| pgcrImage | string | If this activity mode has a related PGCR image, this will be the path to said image. | No |
| modeType | integer (int32) | The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode. | No |
| activityModeCategory | integer (int32) | The type of play being performed in broad terms (PVP, PVE) | No |
| isTeamBased | boolean | If True, this mode has oppositional teams fighting against each other rather than "Free-For-All" or Co-operative modes of play.
Note that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren't team based, and then this boolean won't make much sense (the aggregation would become "sometimes team based"). Let's not deal with that right now. | No |
| isAggregateMode | boolean | If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash. | No |
| parentHashes | Array[integer] | The hash identifiers of the DestinyActivityModeDefinitions that represent all of the "parent" modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE. | No |
| friendlyName | string | A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it's worth. | No |
| activityModeMappings | object | If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played. | No |
| display | boolean | If FALSE, we want to ignore this type when we're showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose. | No |
| order | integer (int32) | The relative ordering of activity modes. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityModeDefinition object
const example = {
  displayProperties: null,
  pgcrImage: "example value",
  modeType: 123,
  activityModeCategory: 123,
  isTeamBased: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityModeDefinition object
example = {
    "displayProperties": None,
    "pgcrImage": "example value",
    "modeType": 123,
    "activityModeCategory": 123,
    "isTeamBased": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.DestinyActivityModeCategory**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityModeDefinition":   {
      "description": "This definition represents an \"Activity Mode\" as it exists in the Historical Stats endpoints. An individual Activity Mode represents a collection of activities that are played in a certain way. For example, Nightfall Strikes are part of a \"Nightfall\" activity mode, and any activities played as the PVP mode \"Clash\" are part of the \"Clash activity mode.\r\nActivity modes are nested under each other in a hierarchy, so that if you ask for - for example - \"AllPvP\", you will get any PVP activities that the user has played, regardless of what specific PVP mode was being played.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "pgcrImage": {
              "description": "If this activity mode has a related PGCR image, this will be the path to said image.",
              "type": "string"
          },
          "modeType": {
              "format": "int32",
              "description": "The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
              }
          },
          "activityModeCategory": {
              "format": "int32",
              "description": "The type of play being performed in broad terms (PVP, PVE)",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityModeCategory"
              }
          },
          "isTeamBased": {
              "description": "If True, this mode has oppositional teams fighting against each other rather than \"Free-For-All\" or Co-operative modes of play.\r\nNote that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren't team based, and then this boolean won't make much sense (the aggregation would become \"sometimes team based\"). Let's not deal with that right now.",
              "type": "boolean"
          },
          "isAggregateMode": {
              "description": "If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash.",
              "type": "boolean"
          },
          "parentHashes": {
              "description": "The hash identifiers of the DestinyActivityModeDefinitions that represent all of the \"parent\" modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "friendlyName": {
              "description": "A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it's worth.",
              "type": "string"
          },
          "activityModeMappings": {
              "description": "If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played.",
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "description": "For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
                  }
              }
          },
          "display": {
              "description": "If FALSE, we want to ignore this type when we're showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose.",
              "type": "boolean"
          },
          "order": {
              "format": "int32",
              "description": "The relative ordering of activity modes.",
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
      "x-mobile-manifest-name": "ActivityModes"
  }
}
```
