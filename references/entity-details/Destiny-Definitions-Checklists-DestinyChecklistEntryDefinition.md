# Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The properties of an individual checklist item. Note that almost everything is optional: it is *highly* variable what kind of data we'll actually be able to return: at times we may have no other relationships to entities at all.
Whatever UI you build, do it with the knowledge that any given entry might not actually be able to be associated with some other Destiny entity.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| hash | integer (uint32) | The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists. | No |
| displayProperties | object | Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier. | No |
| destinationHash | integer (uint32) |  | No |
| locationHash | integer (uint32) |  | No |
| bubbleHash | integer (uint32) | Note that a Bubble's hash doesn't uniquely identify a "top level" entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning.
You can use this property if it is populated to look up the DestinyLocationDefinition's associated .locationReleases[].activityBubbleName property. | No |
| activityHash | integer (uint32) |  | No |
| itemHash | integer (uint32) |  | No |
| vendorHash | integer (uint32) |  | No |
| vendorInteractionIndex | integer (int32) |  | No |
| scope | integer (int32) | The scope at which this specific entry can be computed. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition object
const example = {
  hash: 123,
  displayProperties: null,
  destinationHash: 123,
  locationHash: 123,
  bubbleHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition object
example = {
    "hash": 123,
    "displayProperties": None,
    "destinationHash": 123,
    "locationHash": 123,
    "bubbleHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyLocationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.DestinyScope**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition":   {
      "description": "The properties of an individual checklist item. Note that almost everything is optional: it is *highly* variable what kind of data we'll actually be able to return: at times we may have no other relationships to entities at all.\r\nWhatever UI you build, do it with the knowledge that any given entry might not actually be able to be associated with some other Destiny entity.",
      "type": "object",
      "properties": {
          "hash": {
              "format": "uint32",
              "description": "The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists.",
              "type": "integer"
          },
          "displayProperties": {
              "description": "Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "destinationHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          },
          "locationHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyLocationDefinition"
              }
          },
          "bubbleHash": {
              "format": "uint32",
              "description": "Note that a Bubble's hash doesn't uniquely identify a \"top level\" entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning.\r\nYou can use this property if it is populated to look up the DestinyLocationDefinition's associated .locationReleases[].activityBubbleName property.",
              "type": "integer"
          },
          "activityHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "itemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "vendorHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "vendorInteractionIndex": {
              "format": "int32",
              "type": "integer"
          },
          "scope": {
              "format": "int32",
              "description": "The scope at which this specific entry can be computed.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyScope"
              }
          }
      }
  }
}
```
