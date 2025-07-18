# Destiny.Definitions.DestinyStatOverrideDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyStatOverrideDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Stat Groups (DestinyStatGroupDefinition) has the ability to override the localized text associated with stats that are to be shown on the items with which they are associated.
This defines a specific overridden stat. You could theoretically check these before rendering your stat UI, and for each stat that has an override show these displayProperties instead of those on the DestinyStatDefinition.
Or you could be like us, and skip that for now because the game has yet to actually use this feature. But know that it's here, waiting for a resilliant young designer to take up the mantle and make us all look foolish by showing the wrong name for stats.
Note that, if this gets used, the override will apply only to items using the overriding Stat Group. Other items will still show the default stat's name/description.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statHash | integer (uint32) | The hash identifier of the stat whose display properties are being overridden. | No |
| displayProperties | object | The display properties to show instead of the base DestinyStatDefinition display properties. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyStatOverrideDefinition object
const example = {
  statHash: 123,
  displayProperties: null,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyStatOverrideDefinition object
example = {
    "statHash": 123,
    "displayProperties": None,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyStatOverrideDefinition":   {
      "description": "Stat Groups (DestinyStatGroupDefinition) has the ability to override the localized text associated with stats that are to be shown on the items with which they are associated.\r\nThis defines a specific overridden stat. You could theoretically check these before rendering your stat UI, and for each stat that has an override show these displayProperties instead of those on the DestinyStatDefinition.\r\nOr you could be like us, and skip that for now because the game has yet to actually use this feature. But know that it's here, waiting for a resilliant young designer to take up the mantle and make us all look foolish by showing the wrong name for stats.\r\nNote that, if this gets used, the override will apply only to items using the overriding Stat Group. Other items will still show the default stat's name/description.",
      "type": "object",
      "properties": {
          "statHash": {
              "format": "uint32",
              "description": "The hash identifier of the stat whose display properties are being overridden.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "displayProperties": {
              "description": "The display properties to show instead of the base DestinyStatDefinition display properties.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          }
      }
  }
}
```
