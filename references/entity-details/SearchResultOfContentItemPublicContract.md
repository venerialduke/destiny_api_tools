# SearchResultOfContentItemPublicContract

## Entity Information
- **Entity Name**: SearchResultOfContentItemPublicContract
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for searchresultofcontentitempubliccontract operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| results | Array[Content.ContentItemPublicContract] |  | No |
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
// Example SearchResultOfContentItemPublicContract object
const example = {
  results: [],
  totalResults: 123,
  hasMore: true,
  query: null,
  replacementContinuationToken: "example value",
  // ... more properties
};
```

### Python
```python
# Example SearchResultOfContentItemPublicContract object
example = {
    "results": [],
    "totalResults": 123,
    "hasMore": True,
    "query": None,
    "replacementContinuationToken": "example value",
    # ... more properties
}
```

## Related Entities
- **Content.ContentItemPublicContract**: Referenced in this entity
- **Queries.PagedQuery**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "SearchResultOfContentItemPublicContract":   {
      "type": "object",
      "properties": {
          "results": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.ContentItemPublicContract"
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
