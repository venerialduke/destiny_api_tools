# Forum.PostSearchResponse

## Entity Information
- **Entity Name**: Forum.PostSearchResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for postsearchresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| relatedPosts | Array[Forum.PostResponse] |  | No |
| authors | Array[User.GeneralUser] |  | No |
| groups | Array[GroupsV2.GroupResponse] |  | No |
| searchedTags | Array[Tags.Models.Contracts.TagResponse] |  | No |
| polls | Array[Forum.PollResponse] |  | No |
| recruitmentDetails | Array[Forum.ForumRecruitmentDetail] |  | No |
| availablePages | integer (int32) |  | No |
| results | Array[Forum.PostResponse] |  | No |
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
// Example Forum.PostSearchResponse object
const example = {
  relatedPosts: [],
  authors: [],
  groups: [],
  searchedTags: [],
  polls: [],
  // ... more properties
};
```

### Python
```python
# Example Forum.PostSearchResponse object
example = {
    "relatedPosts": [],
    "authors": [],
    "groups": [],
    "searchedTags": [],
    "polls": [],
    # ... more properties
}
```

## Related Entities
- **Forum.ForumRecruitmentDetail**: Referenced in this entity
- **Forum.PollResponse**: Referenced in this entity
- **Forum.PostResponse**: Referenced in this entity
- **GroupsV2.GroupResponse**: Referenced in this entity
- **Queries.PagedQuery**: Referenced in this entity
- **Tags.Models.Contracts.TagResponse**: Referenced in this entity
- **User.GeneralUser**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Forum.PostSearchResponse":   {
      "type": "object",
      "properties": {
          "relatedPosts": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Forum.PostResponse"
              }
          },
          "authors": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.GeneralUser"
              }
          },
          "groups": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/GroupsV2.GroupResponse"
              }
          },
          "searchedTags": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Tags.Models.Contracts.TagResponse"
              }
          },
          "polls": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Forum.PollResponse"
              }
          },
          "recruitmentDetails": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Forum.ForumRecruitmentDetail"
              }
          },
          "availablePages": {
              "format": "int32",
              "type": "integer"
          },
          "results": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Forum.PostResponse"
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
