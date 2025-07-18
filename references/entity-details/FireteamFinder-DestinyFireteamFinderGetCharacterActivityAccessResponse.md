# FireteamFinder.DestinyFireteamFinderGetCharacterActivityAccessResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderGetCharacterActivityAccessResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindergetcharacteractivityaccessresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| fireteamFinderActivityGraphStates | object | A map of fireteam finder activity graph hashes to visibility and availability states. | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderGetCharacterActivityAccessResponse object
const example = {
  fireteamFinderActivityGraphStates: null,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderGetCharacterActivityAccessResponse object
example = {
    "fireteamFinderActivityGraphStates": None,
}
```

## Related Entities
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderActivityGraphState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderGetCharacterActivityAccessResponse":   {
      "type": "object",
      "properties": {
          "fireteamFinderActivityGraphStates": {
              "description": "A map of fireteam finder activity graph hashes to visibility and availability states.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderActivityGraphState"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          }
      }
  }
}
```
