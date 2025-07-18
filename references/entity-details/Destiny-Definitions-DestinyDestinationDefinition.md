# Destiny.Definitions.DestinyDestinationDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyDestinationDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
On to one of the more confusing subjects of the API. What is a Destination, and what is the relationship between it, Activities, Locations, and Places?
A "Destination" is a specific region/city/area of a larger "Place". For instance, a Place might be Earth where a Destination might be Bellevue, Washington. (Please, pick a more interesting destination if you come to visit Earth).

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| placeHash | integer (uint32) | The place that "owns" this Destination. Use this hash to look up the DestinyPlaceDefinition. | No |
| defaultFreeroamActivityHash | integer (uint32) | If this Destination has a default Free-Roam activity, this is the hash for that Activity. Use it to look up the DestinyActivityDefintion. | No |
| activityGraphEntries | Array[Destiny.Definitions.DestinyActivityGraphListEntryDefinition] | If the Destination has default Activity Graphs (i.e. "Map") that should be shown in the director, this is the list of those Graphs. At most, only one should be active at any given time for a Destination: these would represent, for example, different variants on a Map if the Destination is changing on a macro level based on game state. | No |
| bubbleSettings | Array[Destiny.Definitions.DestinyDestinationBubbleSettingDefinition] | A Destination may have many "Bubbles" zones with human readable properties.
We don't get as much info as I'd like about them - I'd love to return info like where on the map they are located - but at least this gives you the name of those bubbles. bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data.
DEPRECATED - Just use bubbles, it now has this data. | No |
| bubbles | Array[Destiny.Definitions.DestinyBubbleDefinition] | This provides the unique identifiers for every bubble in the destination (only guaranteed unique within the destination), and any intrinsic properties of the bubble.
bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyDestinationDefinition object
const example = {
  displayProperties: null,
  placeHash: 123,
  defaultFreeroamActivityHash: 123,
  activityGraphEntries: [],
  bubbleSettings: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyDestinationDefinition object
example = {
    "displayProperties": None,
    "placeHash": 123,
    "defaultFreeroamActivityHash": 123,
    "activityGraphEntries": [],
    "bubbleSettings": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityGraphListEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyBubbleDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationBubbleSettingDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyPlaceDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyDestinationDefinition":   {
      "description": "On to one of the more confusing subjects of the API. What is a Destination, and what is the relationship between it, Activities, Locations, and Places?\r\nA \"Destination\" is a specific region/city/area of a larger \"Place\". For instance, a Place might be Earth where a Destination might be Bellevue, Washington. (Please, pick a more interesting destination if you come to visit Earth).",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "placeHash": {
              "format": "uint32",
              "description": "The place that \"owns\" this Destination. Use this hash to look up the DestinyPlaceDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyPlaceDefinition"
              }
          },
          "defaultFreeroamActivityHash": {
              "format": "uint32",
              "description": "If this Destination has a default Free-Roam activity, this is the hash for that Activity. Use it to look up the DestinyActivityDefintion.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "activityGraphEntries": {
              "description": "If the Destination has default Activity Graphs (i.e. \"Map\") that should be shown in the director, this is the list of those Graphs. At most, only one should be active at any given time for a Destination: these would represent, for example, different variants on a Map if the Destination is changing on a macro level based on game state.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityGraphListEntryDefinition"
              }
          },
          "bubbleSettings": {
              "description": "A Destination may have many \"Bubbles\" zones with human readable properties.\r\nWe don't get as much info as I'd like about them - I'd love to return info like where on the map they are located - but at least this gives you the name of those bubbles. bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data.\r\nDEPRECATED - Just use bubbles, it now has this data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationBubbleSettingDefinition"
              }
          },
          "bubbles": {
              "description": "This provides the unique identifiers for every bubble in the destination (only guaranteed unique within the destination), and any intrinsic properties of the bubble.\r\nbubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyBubbleDefinition"
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
      "x-mobile-manifest-name": "Destinations"
  }
}
```
