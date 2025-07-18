# FireteamFinder.DestinyFireteamFinderKickPlayerRequest

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderKickPlayerRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderkickplayerrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| targetMembershipType | integer (int32) |  | No |
| targetCharacterId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderKickPlayerRequest object
const example = {
  targetMembershipType: 123,
  targetCharacterId: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderKickPlayerRequest object
example = {
    "targetMembershipType": 123,
    "targetCharacterId": 123,
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderKickPlayerRequest":   {
      "type": "object",
      "properties": {
          "targetMembershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "targetCharacterId": {
              "format": "int64",
              "type": "integer"
          }
      }
  }
}
```
