# GroupsV2.GroupUserInfoCard

## Entity Information
- **Entity Name**: GroupsV2.GroupUserInfoCard
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupuserinfocard operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| LastSeenDisplayName | string | This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property. | No |
| LastSeenDisplayNameType | integer (int32) | The platform of the LastSeenDisplayName | No |
| supplementalDisplayName | string | A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc. | No |
| iconPath | string | URL the Icon if available. | No |
| crossSaveOverride | integer (int32) | If there is a cross save override in effect, this value will tell you the type that is overridding this one. | No |
| applicableMembershipTypes | Array[integer] | The list of Membership Types indicating the platforms on which this Membership can be used.
 Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list | No |
| isPublic | boolean | If True, this is a public user membership. | No |
| membershipType | integer (int32) | Type of the membership. Not necessarily the native type. | No |
| membershipId | integer (int64) | Membership ID as they user is known in the Accounts service | No |
| displayName | string | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. | No |
| bungieGlobalDisplayName | string | The bungie global display name, if set. | No |
| bungieGlobalDisplayNameCode | integer (int16) | The bungie global display name code, if set. | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupUserInfoCard object
const example = {
  LastSeenDisplayName: "example value",
  LastSeenDisplayNameType: 123,
  supplementalDisplayName: "example value",
  iconPath: "example value",
  crossSaveOverride: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupUserInfoCard object
example = {
    "LastSeenDisplayName": "example value",
    "LastSeenDisplayNameType": 123,
    "supplementalDisplayName": "example value",
    "iconPath": "example value",
    "crossSaveOverride": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupUserInfoCard":   {
      "type": "object",
      "properties": {
          "LastSeenDisplayName": {
              "description": "This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property.",
              "type": "string"
          },
          "LastSeenDisplayNameType": {
              "format": "int32",
              "description": "The platform of the LastSeenDisplayName",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "supplementalDisplayName": {
              "description": "A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.",
              "type": "string"
          },
          "iconPath": {
              "description": "URL the Icon if available.",
              "type": "string"
          },
          "crossSaveOverride": {
              "format": "int32",
              "description": "If there is a cross save override in effect, this value will tell you the type that is overridding this one.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "applicableMembershipTypes": {
              "description": "The list of Membership Types indicating the platforms on which this Membership can be used.\r\n Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/BungieMembershipType"
                  }
              }
          },
          "isPublic": {
              "description": "If True, this is a public user membership.",
              "type": "boolean"
          },
          "membershipType": {
              "format": "int32",
              "description": "Type of the membership. Not necessarily the native type.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "membershipId": {
              "format": "int64",
              "description": "Membership ID as they user is known in the Accounts service",
              "type": "integer"
          },
          "displayName": {
              "description": "Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.",
              "type": "string"
          },
          "bungieGlobalDisplayName": {
              "description": "The bungie global display name, if set.",
              "type": "string"
          },
          "bungieGlobalDisplayNameCode": {
              "format": "int16",
              "description": "The bungie global display name code, if set.",
              "type": "integer"
          }
      }
  }
}
```
