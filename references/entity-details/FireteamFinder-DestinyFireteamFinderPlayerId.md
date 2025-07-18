# FireteamFinder.DestinyFireteamFinderPlayerId

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderPlayerId
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderplayerid data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |
| characterId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderPlayerId object
const example = {
  membershipId: 123,
  membershipType: 123,
  characterId: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderPlayerId object
example = {
    "membershipId": 123,
    "membershipType": 123,
    "characterId": 123,
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
  "FireteamFinder.DestinyFireteamFinderPlayerId":   {
      "type": "object",
      "properties": {
          "membershipId": {
              "format": "int64",
              "type": "integer"
          },
          "membershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "characterId": {
              "format": "int64",
              "type": "integer"
          }
      }
  }
}
```
