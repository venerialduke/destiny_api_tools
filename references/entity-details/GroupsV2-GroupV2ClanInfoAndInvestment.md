# GroupsV2.GroupV2ClanInfoAndInvestment

## Entity Information
- **Entity Name**: GroupsV2.GroupV2ClanInfoAndInvestment
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The same as GroupV2ClanInfo, but includes any investment data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| d2ClanProgressions | object |  | No |
| clanCallsign | string |  | No |
| clanBannerData | GroupsV2.ClanBanner |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupV2ClanInfoAndInvestment object
const example = {
  d2ClanProgressions: null,
  clanCallsign: "example value",
  clanBannerData: null,
};
```

### Python
```python
# Example GroupsV2.GroupV2ClanInfoAndInvestment object
example = {
    "d2ClanProgressions": None,
    "clanCallsign": "example value",
    "clanBannerData": None,
}
```

## Related Entities
- **Destiny.DestinyProgression**: Referenced in this entity
- **GroupsV2.ClanBanner**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupV2ClanInfoAndInvestment":   {
      "description": "The same as GroupV2ClanInfo, but includes any investment data.",
      "type": "object",
      "properties": {
          "d2ClanProgressions": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.DestinyProgression"
              }
          },
          "clanCallsign": {
              "type": "string"
          },
          "clanBannerData": {
              "$ref": "#/definitions/GroupsV2.ClanBanner"
          }
      }
  }
}
```
