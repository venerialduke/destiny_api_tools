# Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymilestonechallengeactivitygraphnodeentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityGraphHash | integer (uint32) |  | No |
| activityGraphNodeHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry object
const example = {
  activityGraphHash: 123,
  activityGraphNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry object
example = {
    "activityGraphHash": 123,
    "activityGraphNodeHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry":   {
      "type": "object",
      "properties": {
          "activityGraphHash": {
              "format": "uint32",
              "type": "integer"
          },
          "activityGraphNodeHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
