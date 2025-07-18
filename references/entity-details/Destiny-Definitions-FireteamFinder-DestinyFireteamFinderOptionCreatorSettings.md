# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoptioncreatorsettings data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| control | Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings object
const example = {
  control: null,
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings object
example = {
    "control": None,
}
```

## Related Entities
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings":   {
      "type": "object",
      "properties": {
          "control": {
              "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl"
          }
      }
  }
}
```
