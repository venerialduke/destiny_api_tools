# FireteamFinder.DestinyFireteamFinderActivityGraphState

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderActivityGraphState
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderactivitygraphstate data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| isVisible | boolean | Indicates if this fireteam finder activity graph node is visible for this character. | No |
| isAvailable | boolean | Indicates if this fireteam finder activity graph node is available to select for this character. | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderActivityGraphState object
const example = {
  isVisible: true,
  isAvailable: true,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderActivityGraphState object
example = {
    "isVisible": True,
    "isAvailable": True,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderActivityGraphState":   {
      "type": "object",
      "properties": {
          "isVisible": {
              "description": "Indicates if this fireteam finder activity graph node is visible for this character.",
              "type": "boolean"
          },
          "isAvailable": {
              "description": "Indicates if this fireteam finder activity graph node is available to select for this character.",
              "type": "boolean"
          }
      }
  }
}
```
