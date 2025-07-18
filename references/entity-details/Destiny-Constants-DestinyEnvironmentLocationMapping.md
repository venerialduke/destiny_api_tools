# Destiny.Constants.DestinyEnvironmentLocationMapping

## Entity Information
- **Entity Name**: Destiny.Constants.DestinyEnvironmentLocationMapping
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyenvironmentlocationmapping data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| locationHash | integer (uint32) | The location that is revealed on the director by this mapping. | No |
| activationSource | string | A hint that the UI uses to figure out how this location is activated by the player. | No |
| itemHash | integer (uint32) | If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don't) | No |
| objectiveHash | integer (uint32) | If this is populated, this is an objective related to the location. | No |
| activityHash | integer (uint32) | If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don't) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Constants.DestinyEnvironmentLocationMapping object
const example = {
  locationHash: 123,
  activationSource: "example value",
  itemHash: 123,
  objectiveHash: 123,
  activityHash: 123,
};
```

### Python
```python
# Example Destiny.Constants.DestinyEnvironmentLocationMapping object
example = {
    "locationHash": 123,
    "activationSource": "example value",
    "itemHash": 123,
    "objectiveHash": 123,
    "activityHash": 123,
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
  "Destiny.Constants.DestinyEnvironmentLocationMapping":   {
      "type": "object",
      "properties": {
          "locationHash": {
              "format": "uint32",
              "description": "The location that is revealed on the director by this mapping.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyLocationDefinition"
              }
          },
          "activationSource": {
              "description": "A hint that the UI uses to figure out how this location is activated by the player.",
              "type": "string"
          },
          "itemHash": {
              "format": "uint32",
              "description": "If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don't)",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "objectiveHash": {
              "format": "uint32",
              "description": "If this is populated, this is an objective related to the location.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "activityHash": {
              "format": "uint32",
              "description": "If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don't)",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          }
      }
  }
}
```
