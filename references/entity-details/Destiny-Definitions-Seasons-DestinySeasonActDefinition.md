# Destiny.Definitions.Seasons.DestinySeasonActDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinySeasonActDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines the name, start time and ranks included in an Act of an Episode.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayName | string | The name of the Act. | No |
| startTime | string (date-time) | The start time of the Act. | No |
| rankCount | integer (int32) | The number of ranks included in the Act. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinySeasonActDefinition object
const example = {
  displayName: "example value",
  startTime: "example value",
  rankCount: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinySeasonActDefinition object
example = {
    "displayName": "example value",
    "startTime": "example value",
    "rankCount": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinySeasonActDefinition":   {
      "description": "Defines the name, start time and ranks included in an Act of an Episode.",
      "type": "object",
      "properties": {
          "displayName": {
              "description": "The name of the Act.",
              "type": "string"
          },
          "startTime": {
              "format": "date-time",
              "description": "The start time of the Act.",
              "type": "string"
          },
          "rankCount": {
              "format": "int32",
              "description": "The number of ranks included in the Act.",
              "type": "integer"
          }
      }
  }
}
```
