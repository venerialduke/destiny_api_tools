# Destiny.Components.Profiles.DestinyProfileTransitoryJoinability

## Entity Information
- **Entity Name**: Destiny.Components.Profiles.DestinyProfileTransitoryJoinability
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Some basic information about whether you can be joined, how many slots are left etc. Note that this can change quickly, so it may not actually be useful. But perhaps it will be in some use cases?

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| openSlots | integer (int32) | The number of slots still available on this person's fireteam. | No |
| privacySetting | integer (int32) | Who the person is currently allowing invites from. | No |
| closedReasons | integer (int32) | Reasons why a person can't join this person's fireteam. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Profiles.DestinyProfileTransitoryJoinability object
const example = {
  openSlots: 123,
  privacySetting: 123,
  closedReasons: 123,
};
```

### Python
```python
# Example Destiny.Components.Profiles.DestinyProfileTransitoryJoinability object
example = {
    "openSlots": 123,
    "privacySetting": 123,
    "closedReasons": 123,
}
```

## Related Entities
- **Destiny.DestinyGamePrivacySetting**: Referenced in this entity
- **Destiny.DestinyJoinClosedReasons**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Profiles.DestinyProfileTransitoryJoinability":   {
      "description": "Some basic information about whether you can be joined, how many slots are left etc. Note that this can change quickly, so it may not actually be useful. But perhaps it will be in some use cases?",
      "type": "object",
      "properties": {
          "openSlots": {
              "format": "int32",
              "description": "The number of slots still available on this person's fireteam.",
              "type": "integer"
          },
          "privacySetting": {
              "format": "int32",
              "description": "Who the person is currently allowing invites from.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGamePrivacySetting"
              }
          },
          "closedReasons": {
              "format": "int32",
              "description": "Reasons why a person can't join this person's fireteam.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyJoinClosedReasons"
              }
          }
      }
  }
}
```
