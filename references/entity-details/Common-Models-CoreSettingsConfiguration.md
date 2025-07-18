# Common.Models.CoreSettingsConfiguration

## Entity Information
- **Entity Name**: Common.Models.CoreSettingsConfiguration
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for coresettingsconfiguration operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| environment | string |  | No |
| systems | object |  | No |
| ignoreReasons | Array[Common.Models.CoreSetting] |  | No |
| forumCategories | Array[Common.Models.CoreSetting] |  | No |
| groupAvatars | Array[Common.Models.CoreSetting] |  | No |
| defaultGroupTheme | Common.Models.CoreSetting |  | No |
| destinyMembershipTypes | Array[Common.Models.CoreSetting] |  | No |
| recruitmentPlatformTags | Array[Common.Models.CoreSetting] |  | No |
| recruitmentMiscTags | Array[Common.Models.CoreSetting] |  | No |
| recruitmentActivities | Array[Common.Models.CoreSetting] |  | No |
| userContentLocales | Array[Common.Models.CoreSetting] |  | No |
| systemContentLocales | Array[Common.Models.CoreSetting] |  | No |
| clanBannerDecals | Array[Common.Models.CoreSetting] |  | No |
| clanBannerDecalColors | Array[Common.Models.CoreSetting] |  | No |
| clanBannerGonfalons | Array[Common.Models.CoreSetting] |  | No |
| clanBannerGonfalonColors | Array[Common.Models.CoreSetting] |  | No |
| clanBannerGonfalonDetails | Array[Common.Models.CoreSetting] |  | No |
| clanBannerGonfalonDetailColors | Array[Common.Models.CoreSetting] |  | No |
| clanBannerStandards | Array[Common.Models.CoreSetting] |  | No |
| destiny2CoreSettings | Common.Models.Destiny2CoreSettings |  | No |
| emailSettings | User.EmailSettings |  | No |
| fireteamActivities | Array[Common.Models.CoreSetting] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Common.Models.CoreSettingsConfiguration object
const example = {
  environment: "example value",
  systems: null,
  ignoreReasons: [],
  forumCategories: [],
  groupAvatars: [],
  // ... more properties
};
```

### Python
```python
# Example Common.Models.CoreSettingsConfiguration object
example = {
    "environment": "example value",
    "systems": None,
    "ignoreReasons": [],
    "forumCategories": [],
    "groupAvatars": [],
    # ... more properties
}
```

## Related Entities
- **Common.Models.CoreSetting**: Referenced in this entity
- **Common.Models.CoreSystem**: Referenced in this entity
- **Common.Models.Destiny2CoreSettings**: Referenced in this entity
- **User.EmailSettings**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Common.Models.CoreSettingsConfiguration":   {
      "type": "object",
      "properties": {
          "environment": {
              "type": "string"
          },
          "systems": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Common.Models.CoreSystem"
              }
          },
          "ignoreReasons": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "forumCategories": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "groupAvatars": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "defaultGroupTheme": {
              "$ref": "#/definitions/Common.Models.CoreSetting"
          },
          "destinyMembershipTypes": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "recruitmentPlatformTags": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "recruitmentMiscTags": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "recruitmentActivities": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "userContentLocales": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "systemContentLocales": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerDecals": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerDecalColors": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerGonfalons": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerGonfalonColors": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerGonfalonDetails": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerGonfalonDetailColors": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "clanBannerStandards": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          },
          "destiny2CoreSettings": {
              "$ref": "#/definitions/Common.Models.Destiny2CoreSettings"
          },
          "emailSettings": {
              "$ref": "#/definitions/User.EmailSettings"
          },
          "fireteamActivities": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          }
      }
  }
}
```
