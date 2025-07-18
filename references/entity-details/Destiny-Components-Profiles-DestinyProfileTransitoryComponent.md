# Destiny.Components.Profiles.DestinyProfileTransitoryComponent

## Entity Information
- **Entity Name**: Destiny.Components.Profiles.DestinyProfileTransitoryComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is an experimental set of data that Bungie considers to be "transitory" - information that may be useful for API users, but that is coming from a non-authoritative data source about information that could potentially change at a more frequent pace than Bungie.net will receive updates about it.
This information is provided exclusively for convenience should any of it be useful to users: we provide no guarantees to the accuracy or timeliness of data that comes from this source. Know that this data can potentially be out-of-date or even wrong entirely if the user disconnected from the game or suddenly changed their status before we can receive refreshed data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| partyMembers | Array[Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember] | If you have any members currently in your party, this is some (very) bare-bones information about those members. | No |
| currentActivity | object | If you are in an activity, this is some transitory info about the activity currently being played. | No |
| joinability | object | Information about whether and what might prevent you from joining this person on a fireteam. | No |
| tracking | Array[Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry] | Information about tracked entities. | No |
| lastOrbitedDestinationHash | integer (uint32) | The hash identifier for the DestinyDestinationDefinition of the last location you were orbiting when in orbit. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Profiles.DestinyProfileTransitoryComponent object
const example = {
  partyMembers: [],
  currentActivity: null,
  joinability: null,
  tracking: [],
  lastOrbitedDestinationHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Profiles.DestinyProfileTransitoryComponent object
example = {
    "partyMembers": [],
    "currentActivity": None,
    "joinability": None,
    "tracking": [],
    "lastOrbitedDestinationHash": 123,
}
```

## Related Entities
- **Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity**: Referenced in this entity
- **Destiny.Components.Profiles.DestinyProfileTransitoryJoinability**: Referenced in this entity
- **Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember**: Referenced in this entity
- **Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Profiles.DestinyProfileTransitoryComponent":   {
      "description": "This is an experimental set of data that Bungie considers to be \"transitory\" - information that may be useful for API users, but that is coming from a non-authoritative data source about information that could potentially change at a more frequent pace than Bungie.net will receive updates about it.\r\nThis information is provided exclusively for convenience should any of it be useful to users: we provide no guarantees to the accuracy or timeliness of data that comes from this source. Know that this data can potentially be out-of-date or even wrong entirely if the user disconnected from the game or suddenly changed their status before we can receive refreshed data.",
      "type": "object",
      "properties": {
          "partyMembers": {
              "description": "If you have any members currently in your party, this is some (very) bare-bones information about those members.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember"
              }
          },
          "currentActivity": {
              "description": "If you are in an activity, this is some transitory info about the activity currently being played.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity"
                  }
              ]
          },
          "joinability": {
              "description": "Information about whether and what might prevent you from joining this person on a fireteam.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Components.Profiles.DestinyProfileTransitoryJoinability"
                  }
              ]
          },
          "tracking": {
              "description": "Information about tracked entities.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry"
              }
          },
          "lastOrbitedDestinationHash": {
              "format": "uint32",
              "description": "The hash identifier for the DestinyDestinationDefinition of the last location you were orbiting when in orbit.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Transitory"
  }
}
```
