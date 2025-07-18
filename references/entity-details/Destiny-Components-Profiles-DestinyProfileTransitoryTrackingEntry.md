# Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry

## Entity Information
- **Entity Name**: Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This represents a single "thing" being tracked by the player.
This can point to many types of entities, but only a subset of them will actually have a valid hash identifier for whatever it is being pointed to.
It's up to you to interpret what it means when various combinations of these entries have values being tracked.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| locationHash | integer (uint32) | OPTIONAL - If this is tracking a DestinyLocationDefinition, this is the identifier for that location. | No |
| itemHash | integer (uint32) | OPTIONAL - If this is tracking the status of a DestinyInventoryItemDefinition, this is the identifier for that item. | No |
| objectiveHash | integer (uint32) | OPTIONAL - If this is tracking the status of a DestinyObjectiveDefinition, this is the identifier for that objective. | No |
| activityHash | integer (uint32) | OPTIONAL - If this is tracking the status of a DestinyActivityDefinition, this is the identifier for that activity. | No |
| questlineItemHash | integer (uint32) | OPTIONAL - If this is tracking the status of a quest, this is the identifier for the DestinyInventoryItemDefinition that containst that questline data. | No |
| trackedDate | string (date-time) | OPTIONAL - I've got to level with you, I don't really know what this is. Is it when you started tracking it? Is it only populated for tracked items that have time limits?
I don't know, but we can get at it - when I get time to actually test what it is, I'll update this. In the meantime, bask in the mysterious data. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry object
const example = {
  locationHash: 123,
  itemHash: 123,
  objectiveHash: 123,
  activityHash: 123,
  questlineItemHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry object
example = {
    "locationHash": 123,
    "itemHash": 123,
    "objectiveHash": 123,
    "activityHash": 123,
    "questlineItemHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyLocationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Profiles.DestinyProfileTransitoryTrackingEntry":   {
      "description": "This represents a single \"thing\" being tracked by the player.\r\nThis can point to many types of entities, but only a subset of them will actually have a valid hash identifier for whatever it is being pointed to.\r\nIt's up to you to interpret what it means when various combinations of these entries have values being tracked.",
      "type": "object",
      "properties": {
          "locationHash": {
              "format": "uint32",
              "description": "OPTIONAL - If this is tracking a DestinyLocationDefinition, this is the identifier for that location.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyLocationDefinition"
              }
          },
          "itemHash": {
              "format": "uint32",
              "description": "OPTIONAL - If this is tracking the status of a DestinyInventoryItemDefinition, this is the identifier for that item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "objectiveHash": {
              "format": "uint32",
              "description": "OPTIONAL - If this is tracking the status of a DestinyObjectiveDefinition, this is the identifier for that objective.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "activityHash": {
              "format": "uint32",
              "description": "OPTIONAL - If this is tracking the status of a DestinyActivityDefinition, this is the identifier for that activity.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "questlineItemHash": {
              "format": "uint32",
              "description": "OPTIONAL - If this is tracking the status of a quest, this is the identifier for the DestinyInventoryItemDefinition that containst that questline data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "trackedDate": {
              "format": "date-time",
              "description": "OPTIONAL - I've got to level with you, I don't really know what this is. Is it when you started tracking it? Is it only populated for tracked items that have time limits?\r\nI don't know, but we can get at it - when I get time to actually test what it is, I'll update this. In the meantime, bask in the mysterious data.",
              "type": "string"
          }
      }
  }
}
```
