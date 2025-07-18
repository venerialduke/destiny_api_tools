# Destiny.Definitions.DestinyTalentNodeStepGroups

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeStepGroups
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
These properties are an attempt to categorize talent node steps by certain common properties. See the related enumerations for the type of properties being categorized.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| weaponPerformance | integer (int32) |  | No |
| impactEffects | integer (int32) |  | No |
| guardianAttributes | integer (int32) |  | No |
| lightAbilities | integer (int32) |  | No |
| damageTypes | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyTalentNodeStepGroups object
const example = {
  weaponPerformance: 123,
  impactEffects: 123,
  guardianAttributes: 123,
  lightAbilities: 123,
  damageTypes: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyTalentNodeStepGroups object
example = {
    "weaponPerformance": 123,
    "impactEffects": 123,
    "guardianAttributes": 123,
    "lightAbilities": 123,
    "damageTypes": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyTalentNodeStepDamageTypes**: Referenced in this entity
- **Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes**: Referenced in this entity
- **Destiny.Definitions.DestinyTalentNodeStepImpactEffects**: Referenced in this entity
- **Destiny.Definitions.DestinyTalentNodeStepLightAbilities**: Referenced in this entity
- **Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeStepGroups":   {
      "description": "These properties are an attempt to categorize talent node steps by certain common properties. See the related enumerations for the type of properties being categorized.",
      "type": "object",
      "properties": {
          "weaponPerformance": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances"
              }
          },
          "impactEffects": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.DestinyTalentNodeStepImpactEffects"
              }
          },
          "guardianAttributes": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes"
              }
          },
          "lightAbilities": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.DestinyTalentNodeStepLightAbilities"
              }
          },
          "damageTypes": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.DestinyTalentNodeStepDamageTypes"
              }
          }
      }
  }
}
```
