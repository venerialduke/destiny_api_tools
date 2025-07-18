# Destiny.Definitions.Seasons.DestinyEventCardDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinyEventCardDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Defines the properties of an 'Event Card' in Destiny 2, to coincide with a seasonal event for additional challenges, premium rewards, a new seal, and a special title. For example: Solstice of Heroes 2022.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| linkRedirectPath | string |  | No |
| color | Destiny.Misc.DestinyColor |  | No |
| images | Destiny.Definitions.Seasons.DestinyEventCardImages |  | No |
| triumphsPresentationNodeHash | integer (uint32) |  | No |
| sealPresentationNodeHash | integer (uint32) |  | No |
| eventCardCurrencyList | Array[integer] |  | No |
| ticketCurrencyItemHash | integer (uint32) |  | No |
| ticketVendorHash | integer (uint32) |  | No |
| ticketVendorCategoryHash | integer (uint32) |  | No |
| endTime | integer (int64) |  | No |
| rewardProgressionHash | integer (uint32) |  | No |
| weeklyChallengesPresentationNodeHash | integer (uint32) |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinyEventCardDefinition object
const example = {
  displayProperties: null,
  linkRedirectPath: "example value",
  color: null,
  images: null,
  triumphsPresentationNodeHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinyEventCardDefinition object
example = {
    "displayProperties": None,
    "linkRedirectPath": "example value",
    "color": None,
    "images": None,
    "triumphsPresentationNodeHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinyEventCardImages**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinyEventCardDefinition":   {
      "description": "Defines the properties of an 'Event Card' in Destiny 2, to coincide with a seasonal event for additional challenges, premium rewards, a new seal, and a special title. For example: Solstice of Heroes 2022.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "linkRedirectPath": {
              "type": "string"
          },
          "color": {
              "$ref": "#/definitions/Destiny.Misc.DestinyColor"
          },
          "images": {
              "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinyEventCardImages"
          },
          "triumphsPresentationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "sealPresentationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "eventCardCurrencyList": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "ticketCurrencyItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "ticketVendorHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "ticketVendorCategoryHash": {
              "format": "uint32",
              "type": "integer"
          },
          "endTime": {
              "format": "int64",
              "type": "integer"
          },
          "rewardProgressionHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "weeklyChallengesPresentationNodeHash": {
              "format": "uint32",
              "type": "integer",
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
      "x-mobile-manifest-name": "EventCards"
  }
}
```
