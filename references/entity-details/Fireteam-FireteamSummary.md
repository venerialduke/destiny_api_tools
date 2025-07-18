# Fireteam.FireteamSummary

## Entity Information
- **Entity Name**: Fireteam.FireteamSummary
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for fireteamsummary operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| fireteamId | integer (int64) |  | No |
| groupId | integer (int64) |  | No |
| platform | integer (byte) |  | No |
| activityType | integer (int32) |  | No |
| isImmediate | boolean |  | No |
| scheduledTime | string (date-time) |  | No |
| ownerMembershipId | integer (int64) |  | No |
| playerSlotCount | integer (int32) |  | No |
| alternateSlotCount | integer (int32) |  | No |
| availablePlayerSlotCount | integer (int32) |  | No |
| availableAlternateSlotCount | integer (int32) |  | No |
| title | string |  | No |
| dateCreated | string (date-time) |  | No |
| dateModified | string (date-time) |  | No |
| isPublic | boolean |  | No |
| locale | string |  | No |
| isValid | boolean |  | No |
| datePlayerModified | string (date-time) |  | No |
| titleBeforeModeration | string |  | No |
| ownerCurrentGuardianRankSnapshot | integer (int32) |  | No |
| ownerHighestLifetimeGuardianRankSnapshot | integer (int32) |  | No |
| ownerTotalCommendationScoreSnapshot | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Fireteam.FireteamSummary object
const example = {
  fireteamId: 123,
  groupId: 123,
  platform: 123,
  activityType: 123,
  isImmediate: true,
  // ... more properties
};
```

### Python
```python
# Example Fireteam.FireteamSummary object
example = {
    "fireteamId": 123,
    "groupId": 123,
    "platform": 123,
    "activityType": 123,
    "isImmediate": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition**: Referenced in this entity
- **Fireteam.FireteamPlatform**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Fireteam.FireteamSummary":   {
      "type": "object",
      "properties": {
          "fireteamId": {
              "format": "int64",
              "type": "integer"
          },
          "groupId": {
              "format": "int64",
              "type": "integer"
          },
          "platform": {
              "format": "byte",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Fireteam.FireteamPlatform"
              }
          },
          "activityType": {
              "format": "int32",
              "type": "integer"
          },
          "isImmediate": {
              "type": "boolean"
          },
          "scheduledTime": {
              "format": "date-time",
              "type": "string"
          },
          "ownerMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "playerSlotCount": {
              "format": "int32",
              "type": "integer"
          },
          "alternateSlotCount": {
              "format": "int32",
              "type": "integer"
          },
          "availablePlayerSlotCount": {
              "format": "int32",
              "type": "integer"
          },
          "availableAlternateSlotCount": {
              "format": "int32",
              "type": "integer"
          },
          "title": {
              "type": "string"
          },
          "dateCreated": {
              "format": "date-time",
              "type": "string"
          },
          "dateModified": {
              "format": "date-time",
              "type": "string"
          },
          "isPublic": {
              "type": "boolean"
          },
          "locale": {
              "type": "string"
          },
          "isValid": {
              "type": "boolean"
          },
          "datePlayerModified": {
              "format": "date-time",
              "type": "string"
          },
          "titleBeforeModeration": {
              "type": "string"
          },
          "ownerCurrentGuardianRankSnapshot": {
              "format": "int32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition"
              }
          },
          "ownerHighestLifetimeGuardianRankSnapshot": {
              "format": "int32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition"
              }
          },
          "ownerTotalCommendationScoreSnapshot": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
