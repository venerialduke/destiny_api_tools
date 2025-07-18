# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoptionvalues data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| optionalNull | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| optionalFormatString | string |  | No |
| displayFormatType | integer (int32) |  | No |
| type | integer (int32) |  | No |
| valueDefinitions | Array[Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues object
const example = {
  optionalNull: null,
  optionalFormatString: "example value",
  displayFormatType: 123,
  type: 123,
  valueDefinitions: [],
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues object
example = {
    "optionalNull": None,
    "optionalFormatString": "example value",
    "displayFormatType": 123,
    "type": 123,
    "valueDefinitions": [],
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition**: Referenced in this entity
- **Destiny.FireteamFinderOptionDisplayFormat**: Referenced in this entity
- **Destiny.FireteamFinderOptionValueProviderType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues":   {
      "type": "object",
      "properties": {
          "optionalNull": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "optionalFormatString": {
              "type": "string"
          },
          "displayFormatType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionDisplayFormat"
              }
          },
          "type": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionValueProviderType"
              }
          },
          "valueDefinitions": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValueDefinition"
              }
          }
      }
  }
}
```
