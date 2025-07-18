# Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivitydifficultytiersubcategoryoverride data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| skullSubcategoryHash | integer (uint32) |  | No |
| refreshTimeMinutes | integer (int32) |  | No |
| refreshTimeOffsetMinutes | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride object
const example = {
  skullSubcategoryHash: 123,
  refreshTimeMinutes: 123,
  refreshTimeOffsetMinutes: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride object
example = {
    "skullSubcategoryHash": 123,
    "refreshTimeMinutes": 123,
    "refreshTimeOffsetMinutes": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivityDifficultyTierSubcategoryOverride":   {
      "type": "object",
      "properties": {
          "skullSubcategoryHash": {
              "format": "uint32",
              "type": "integer"
          },
          "refreshTimeMinutes": {
              "format": "int32",
              "type": "integer"
          },
          "refreshTimeOffsetMinutes": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
