# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoptionsearchersettings data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| control | Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl |  | No |
| searchFilterType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings object
const example = {
  control: null,
  searchFilterType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings object
example = {
    "control": None,
    "searchFilterType": 123,
}
```

## Related Entities
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl**: Referenced in this entity
- **Destiny.FireteamFinderOptionSearchFilterType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings":   {
      "type": "object",
      "properties": {
          "control": {
              "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSettingsControl"
          },
          "searchFilterType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionSearchFilterType"
              }
          }
      }
  }
}
```
