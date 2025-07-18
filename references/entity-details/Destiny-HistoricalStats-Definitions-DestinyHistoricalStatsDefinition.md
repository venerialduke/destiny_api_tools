# Destiny.HistoricalStats.Definitions.DestinyHistoricalStatsDefinition

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.DestinyHistoricalStatsDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatsdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statId | string | Unique programmer friendly ID for this stat | No |
| group | integer (int32) | Statistic group | No |
| periodTypes | Array[integer] | Time periods the statistic covers | No |
| modes | Array[integer] | Game modes where this statistic can be reported. | No |
| category | integer (int32) | Category for the stat. | No |
| statName | string | Display name | No |
| statNameAbbr | string | Display name abbreviated | No |
| statDescription | string | Description of a stat if applicable. | No |
| unitType | integer (int32) | Unit, if any, for the statistic | No |
| iconImage | string | Optional URI to an icon for the statistic | No |
| mergeMethod | integer (int32) | Optional icon for the statistic | No |
| unitLabel | string | Localized Unit Name for the stat. | No |
| weight | integer (int32) | Weight assigned to this stat indicating its relative impressiveness. | No |
| medalTierHash | integer (uint32) | The tier associated with this medal - be it implicitly or explicitly. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.Definitions.DestinyHistoricalStatsDefinition object
const example = {
  statId: "example value",
  group: 123,
  periodTypes: [],
  modes: [],
  category: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.HistoricalStats.Definitions.DestinyHistoricalStatsDefinition object
example = {
    "statId": "example value",
    "group": 123,
    "periodTypes": [],
    "modes": [],
    "category": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyMedalTierDefinition**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyStatsGroupType**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.PeriodType**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.UnitType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.DestinyHistoricalStatsDefinition":   {
      "type": "object",
      "properties": {
          "statId": {
              "description": "Unique programmer friendly ID for this stat",
              "type": "string"
          },
          "group": {
              "format": "int32",
              "description": "Statistic group",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyStatsGroupType"
              }
          },
          "periodTypes": {
              "description": "Time periods the statistic covers",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.PeriodType"
                  }
              }
          },
          "modes": {
              "description": "Game modes where this statistic can be reported.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
                  }
              }
          },
          "category": {
              "format": "int32",
              "description": "Category for the stat.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType"
              }
          },
          "statName": {
              "description": "Display name",
              "type": "string"
          },
          "statNameAbbr": {
              "description": "Display name abbreviated",
              "type": "string"
          },
          "statDescription": {
              "description": "Description of a stat if applicable.",
              "type": "string"
          },
          "unitType": {
              "format": "int32",
              "description": "Unit, if any, for the statistic",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.UnitType"
              }
          },
          "iconImage": {
              "description": "Optional URI to an icon for the statistic",
              "type": "string"
          },
          "mergeMethod": {
              "format": "int32",
              "description": "Optional icon for the statistic",
              "enum": [
                  "0",
                  "1",
                  "2"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Add",
                      "description": "When collapsing multiple instances of the stat together, add the values."
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Min",
                      "description": "When collapsing multiple instances of the stat together, take the lower value."
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Max",
                      "description": "When collapsing multiple instances of the stat together, take the higher value."
                  }
              ]
          },
          "unitLabel": {
              "description": "Localized Unit Name for the stat.",
              "type": "string"
          },
          "weight": {
              "format": "int32",
              "description": "Weight assigned to this stat indicating its relative impressiveness.",
              "type": "integer"
          },
          "medalTierHash": {
              "format": "uint32",
              "description": "The tier associated with this medal - be it implicitly or explicitly.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMedalTierDefinition"
              }
          }
      },
      "x-mobile-manifest-name": "HistoricalStats"
  }
}
```
