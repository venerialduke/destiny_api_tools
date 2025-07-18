# GroupsV2.GroupV2ClanInfo

## Entity Information
- **Entity Name**: GroupsV2.GroupV2ClanInfo
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This contract contains clan-specific group information. It does not include any investment data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| clanCallsign | string |  | No |
| clanBannerData | GroupsV2.ClanBanner |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupV2ClanInfo object
const example = {
  clanCallsign: "example value",
  clanBannerData: null,
};
```

### Python
```python
# Example GroupsV2.GroupV2ClanInfo object
example = {
    "clanCallsign": "example value",
    "clanBannerData": None,
}
```

## Related Entities
- **GroupsV2.ClanBanner**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupV2ClanInfo":   {
      "description": "This contract contains clan-specific group information. It does not include any investment data.",
      "type": "object",
      "properties": {
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
