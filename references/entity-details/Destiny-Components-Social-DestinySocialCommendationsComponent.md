# Destiny.Components.Social.DestinySocialCommendationsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Social.DestinySocialCommendationsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinysocialcommendationscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| totalScore | integer (int32) |  | No |
| commendationNodePercentagesByHash | object | The percentage for each commendation type out of total received | No |
| scoreDetailValues | Array[integer] |  | No |
| commendationNodeScoresByHash | object |  | No |
| commendationScoresByHash | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Social.DestinySocialCommendationsComponent object
const example = {
  totalScore: 123,
  commendationNodePercentagesByHash: null,
  scoreDetailValues: [],
  commendationNodeScoresByHash: null,
  commendationScoresByHash: null,
};
```

### Python
```python
# Example Destiny.Components.Social.DestinySocialCommendationsComponent object
example = {
    "totalScore": 123,
    "commendationNodePercentagesByHash": None,
    "scoreDetailValues": [],
    "commendationNodeScoresByHash": None,
    "commendationScoresByHash": None,
}
```

## Related Entities
- **Destiny.Definitions.Social.DestinySocialCommendationDefinition**: Referenced in this entity
- **Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Social.DestinySocialCommendationsComponent":   {
      "type": "object",
      "properties": {
          "totalScore": {
              "format": "int32",
              "type": "integer"
          },
          "commendationNodePercentagesByHash": {
              "description": "The percentage for each commendation type out of total received",
              "type": "object",
              "additionalProperties": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "scoreDetailValues": {
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "commendationNodeScoresByHash": {
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition"
              }
          },
          "commendationScoresByHash": {
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Social.DestinySocialCommendationDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "SocialCommendations"
  }
}
```
