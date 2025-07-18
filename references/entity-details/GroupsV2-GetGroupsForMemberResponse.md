# GroupsV2.GetGroupsForMemberResponse

## Entity Information
- **Entity Name**: GroupsV2.GetGroupsForMemberResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for getgroupsformemberresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| areAllMembershipsInactive | object | A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
 The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive. | No |
| results | Array[GroupsV2.GroupMembership] |  | No |
| totalResults | integer (int32) |  | No |
| hasMore | boolean |  | No |
| query | Queries.PagedQuery |  | No |
| replacementContinuationToken | string |  | No |
| useTotalResults | boolean | If useTotalResults is true, then totalResults represents an accurate count.
If False, it does not, and may be estimated/only the size of the current page.
Either way, you should probably always only trust hasMore.
This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GetGroupsForMemberResponse object
const example = {
  areAllMembershipsInactive: null,
  results: [],
  totalResults: 123,
  hasMore: true,
  query: null,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GetGroupsForMemberResponse object
example = {
    "areAllMembershipsInactive": None,
    "results": [],
    "totalResults": 123,
    "hasMore": True,
    "query": None,
    # ... more properties
}
```

## Related Entities
- **GroupsV2.GroupMembership**: Referenced in this entity
- **Queries.PagedQuery**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GetGroupsForMemberResponse":   {
      "type": "object",
      "properties": {
          "areAllMembershipsInactive": {
              "description": "A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.\r\n The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive.",
              "type": "object",
              "additionalProperties": {
                  "type": "boolean"
              }
          },
          "results": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/GroupsV2.GroupMembership"
              }
          },
          "totalResults": {
              "format": "int32",
              "type": "integer"
          },
          "hasMore": {
              "type": "boolean"
          },
          "query": {
              "$ref": "#/definitions/Queries.PagedQuery"
          },
          "replacementContinuationToken": {
              "type": "string"
          },
          "useTotalResults": {
              "description": "If useTotalResults is true, then totalResults represents an accurate count.\r\nIf False, it does not, and may be estimated/only the size of the current page.\r\nEither way, you should probably always only trust hasMore.\r\nThis is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.",
              "type": "boolean"
          }
      }
  }
}
```
