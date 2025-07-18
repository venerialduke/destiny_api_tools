# Destiny.Definitions.Activities.DestinyActivityDifficultyTierDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivityDifficultyTierDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivitydifficultytierdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| recommendedActivityLevelOffset | integer (int32) |  | No |
| fixedActivitySkulls | Array[Destiny.Definitions.Activities.DestinyActivitySkull] |  | No |
| tierEnabledUnlockExpression | Destiny.Definitions.DestinyUnlockExpressionDefinition |  | No |
| tierType | integer (int32) |  | No |
| optionalRequiredTrait | integer (uint32) |  | No |
| activityLevel | integer (int32) |  | No |
| tierRank | integer (int32) |  | No |
| minimumFireteamLeaderPower | integer (int32) |  | No |
| maximumFireteamLeaderPower | integer (int32) |  | No |
| scoreTimeLimitMultiplier | integer (int32) |  | No |
| selectableSkullCollectionHashes | Array[integer] |  | No |
| skullSubcategoryOverrides | Array[Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivityDifficultyTierDefinition object
const example = {
  displayProperties: null,
  recommendedActivityLevelOffset: 123,
  fixedActivitySkulls: [],
  tierEnabledUnlockExpression: null,
  tierType: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivityDifficultyTierDefinition object
example = {
    "displayProperties": None,
    "recommendedActivityLevelOffset": 123,
    "fixedActivitySkulls": [],
    "tierEnabledUnlockExpression": None,
    "tierType": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySkull**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyUnlockExpressionDefinition**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.DestinyActivityDifficultyTierType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivityDifficultyTierDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "recommendedActivityLevelOffset": {
              "format": "int32",
              "type": "integer"
          },
          "fixedActivitySkulls": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySkull"
              }
          },
          "tierEnabledUnlockExpression": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyUnlockExpressionDefinition"
          },
          "tierType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityDifficultyTierType"
              }
          },
          "optionalRequiredTrait": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Traits.DestinyTraitDefinition"
              }
          },
          "activityLevel": {
              "format": "int32",
              "type": "integer"
          },
          "tierRank": {
              "format": "int32",
              "type": "integer"
          },
          "minimumFireteamLeaderPower": {
              "format": "int32",
              "type": "integer"
          },
          "maximumFireteamLeaderPower": {
              "format": "int32",
              "type": "integer"
          },
          "scoreTimeLimitMultiplier": {
              "format": "int32",
              "type": "integer"
          },
          "selectableSkullCollectionHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition"
              }
          },
          "skullSubcategoryOverrides": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride"
              }
          }
      }
  }
}
```
