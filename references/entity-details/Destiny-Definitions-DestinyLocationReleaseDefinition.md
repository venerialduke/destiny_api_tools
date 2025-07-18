# Destiny.Definitions.DestinyLocationReleaseDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyLocationReleaseDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A specific "spot" referred to by a location. Only one of these can be active at a time for a given Location.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | Sadly, these don't appear to be populated anymore (ever?) | No |
| smallTransparentIcon | string |  | No |
| mapIcon | string |  | No |
| largeTransparentIcon | string |  | No |
| spawnPoint | integer (uint32) | If we had map information, this spawnPoint would be interesting. But sadly, we don't have that info. | No |
| destinationHash | integer (uint32) | The Destination being pointed to by this location. | No |
| activityHash | integer (uint32) | The Activity being pointed to by this location. | No |
| activityGraphHash | integer (uint32) | The Activity Graph being pointed to by this location. | No |
| activityGraphNodeHash | integer (uint32) | The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of) | No |
| activityBubbleName | integer (uint32) | The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition's bubbles and bubbleSettings properties. | No |
| activityPathBundle | integer (uint32) | If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information. | No |
| activityPathDestination | integer (uint32) | If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man. | No |
| navPointType | integer (int32) | The type of Nav Point that this represents. See the enumeration for more info. | No |
| worldPosition | Array[integer] | Looks like it should be the position on the map, but sadly it does not look populated... yet? | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyLocationReleaseDefinition object
const example = {
  displayProperties: null,
  smallTransparentIcon: "example value",
  mapIcon: "example value",
  largeTransparentIcon: "example value",
  spawnPoint: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyLocationReleaseDefinition object
example = {
    "displayProperties": None,
    "smallTransparentIcon": "example value",
    "mapIcon": "example value",
    "largeTransparentIcon": "example value",
    "spawnPoint": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity
- **Destiny.DestinyActivityNavPointType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyLocationReleaseDefinition":   {
      "description": "A specific \"spot\" referred to by a location. Only one of these can be active at a time for a given Location.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "Sadly, these don't appear to be populated anymore (ever?)",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "smallTransparentIcon": {
              "type": "string"
          },
          "mapIcon": {
              "type": "string"
          },
          "largeTransparentIcon": {
              "type": "string"
          },
          "spawnPoint": {
              "format": "uint32",
              "description": "If we had map information, this spawnPoint would be interesting. But sadly, we don't have that info.",
              "type": "integer"
          },
          "destinationHash": {
              "format": "uint32",
              "description": "The Destination being pointed to by this location.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          },
          "activityHash": {
              "format": "uint32",
              "description": "The Activity being pointed to by this location.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "activityGraphHash": {
              "format": "uint32",
              "description": "The Activity Graph being pointed to by this location.",
              "type": "integer"
          },
          "activityGraphNodeHash": {
              "format": "uint32",
              "description": "The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of)",
              "type": "integer"
          },
          "activityBubbleName": {
              "format": "uint32",
              "description": "The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition's bubbles and bubbleSettings properties.",
              "type": "integer"
          },
          "activityPathBundle": {
              "format": "uint32",
              "description": "If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information.",
              "type": "integer"
          },
          "activityPathDestination": {
              "format": "uint32",
              "description": "If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man.",
              "type": "integer"
          },
          "navPointType": {
              "format": "int32",
              "description": "The type of Nav Point that this represents. See the enumeration for more info.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityNavPointType"
              }
          },
          "worldPosition": {
              "description": "Looks like it should be the position on the map, but sadly it does not look populated... yet?",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
