# Destiny.Definitions.DestinyActivityGuidedBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityGuidedBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Guided Game information for this activity.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| guidedMaxLobbySize | integer (int32) | The maximum amount of people that can be in the waiting lobby. | No |
| guidedMinLobbySize | integer (int32) | The minimum amount of people that can be in the waiting lobby. | No |
| guidedDisbandCount | integer (int32) | If -1, the guided group cannot be disbanded. Otherwise, take the total # of players in the activity and subtract this number: that is the total # of votes needed for the guided group to disband. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityGuidedBlockDefinition object
const example = {
  guidedMaxLobbySize: 123,
  guidedMinLobbySize: 123,
  guidedDisbandCount: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityGuidedBlockDefinition object
example = {
    "guidedMaxLobbySize": 123,
    "guidedMinLobbySize": 123,
    "guidedDisbandCount": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityGuidedBlockDefinition":   {
      "description": "Guided Game information for this activity.",
      "type": "object",
      "properties": {
          "guidedMaxLobbySize": {
              "format": "int32",
              "description": "The maximum amount of people that can be in the waiting lobby.",
              "type": "integer"
          },
          "guidedMinLobbySize": {
              "format": "int32",
              "description": "The minimum amount of people that can be in the waiting lobby.",
              "type": "integer"
          },
          "guidedDisbandCount": {
              "format": "int32",
              "description": "If -1, the guided group cannot be disbanded. Otherwise, take the total # of players in the activity and subtract this number: that is the total # of votes needed for the guided group to disband.",
              "type": "integer"
          }
      }
  }
}
```
