# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoptionvaluedefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| value | integer (uint32) |  | No |
| flags | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition object
const example = {
  displayProperties: null,
  value: 123,
  flags: 123,
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition object
example = {
    "displayProperties": None,
    "value": 123,
    "flags": 123,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.FireteamFinderOptionValueFlags**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "value": {
              "format": "uint32",
              "type": "integer"
          },
          "flags": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionValueFlags"
              }
          }
      }
  }
}
```
