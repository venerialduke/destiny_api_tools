# Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymilestonechallengeactivityphase data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| phaseHash | integer (uint32) | The hash identifier of the activity's phase. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase object
const example = {
  phaseHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase object
example = {
    "phaseHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase":   {
      "type": "object",
      "properties": {
          "phaseHash": {
              "format": "uint32",
              "description": "The hash identifier of the activity's phase.",
              "type": "integer"
          }
      }
  }
}
```
