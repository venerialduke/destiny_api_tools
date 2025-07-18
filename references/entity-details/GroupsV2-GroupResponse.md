# GroupsV2.GroupResponse

## Entity Information
- **Entity Name**: GroupsV2.GroupResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| detail | GroupsV2.GroupV2 |  | No |
| founder | GroupsV2.GroupMember |  | No |
| alliedIds | Array[integer] |  | No |
| parentGroup | GroupsV2.GroupV2 |  | No |
| allianceStatus | integer (int32) |  | No |
| groupJoinInviteCount | integer (int32) |  | No |
| currentUserMembershipsInactiveForDestiny | boolean | A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save. | No |
| currentUserMemberMap | object | This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available. | No |
| currentUserPotentialMemberMap | object | This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once. | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupResponse object
const example = {
  detail: null,
  founder: null,
  alliedIds: [],
  parentGroup: null,
  allianceStatus: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupResponse object
example = {
    "detail": None,
    "founder": None,
    "alliedIds": [],
    "parentGroup": None,
    "allianceStatus": 123,
    # ... more properties
}
```

## Related Entities
- **GroupsV2.GroupAllianceStatus**: Referenced in this entity
- **GroupsV2.GroupMember**: Referenced in this entity
- **GroupsV2.GroupPotentialMember**: Referenced in this entity
- **GroupsV2.GroupV2**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupResponse":   {
      "type": "object",
      "properties": {
          "detail": {
              "$ref": "#/definitions/GroupsV2.GroupV2"
          },
          "founder": {
              "$ref": "#/definitions/GroupsV2.GroupMember"
          },
          "alliedIds": {
              "type": "array",
              "items": {
                  "format": "int64",
                  "type": "integer"
              }
          },
          "parentGroup": {
              "$ref": "#/definitions/GroupsV2.GroupV2"
          },
          "allianceStatus": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupAllianceStatus"
              }
          },
          "groupJoinInviteCount": {
              "format": "int32",
              "type": "integer"
          },
          "currentUserMembershipsInactiveForDestiny": {
              "description": "A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.",
              "type": "boolean"
          },
          "currentUserMemberMap": {
              "description": "This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/GroupsV2.GroupMember"
              }
          },
          "currentUserPotentialMemberMap": {
              "description": "This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/GroupsV2.GroupPotentialMember"
              }
          }
      }
  }
}
```
