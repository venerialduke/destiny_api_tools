# Destiny.Components.Profiles.DestinyProfileProgressionComponent

## Entity Information
- **Entity Name**: Destiny.Components.Profiles.DestinyProfileProgressionComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The set of progression-related information that applies at a Profile-wide level for your Destiny experience. This differs from the Jimi Hendrix Experience because there's less guitars on fire. Yet. #spoileralert?
This will include information such as Checklist info.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| checklists | object | The set of checklists that can be examined on a profile-wide basis, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)
For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet. | No |
| seasonalArtifact | object | Data related to your progress on the current season's artifact that is the same across characters. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Profiles.DestinyProfileProgressionComponent object
const example = {
  checklists: null,
  seasonalArtifact: null,
};
```

### Python
```python
# Example Destiny.Components.Profiles.DestinyProfileProgressionComponent object
example = {
    "checklists": None,
    "seasonalArtifact": None,
}
```

## Related Entities
- **Destiny.Artifacts.DestinyArtifactProfileScoped**: Referenced in this entity
- **Destiny.Definitions.Checklists.DestinyChecklistDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Profiles.DestinyProfileProgressionComponent":   {
      "description": "The set of progression-related information that applies at a Profile-wide level for your Destiny experience. This differs from the Jimi Hendrix Experience because there's less guitars on fire. Yet. #spoileralert?\r\nThis will include information such as Checklist info.",
      "type": "object",
      "properties": {
          "checklists": {
              "description": "The set of checklists that can be examined on a profile-wide basis, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)\r\nFor each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.",
              "type": "object",
              "additionalProperties": {
                  "type": "object",
                  "additionalProperties": {
                      "type": "boolean"
                  }
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Checklists.DestinyChecklistDefinition"
              }
          },
          "seasonalArtifact": {
              "description": "Data related to your progress on the current season's artifact that is the same across characters.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Artifacts.DestinyArtifactProfileScoped"
                  }
              ]
          }
      },
      "x-destiny-component-type-dependency": "ProfileProgression"
  }
}
```
