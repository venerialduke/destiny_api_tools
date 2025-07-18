# Content.NewsArticleRssResponse

## Entity Information
- **Entity Name**: Content.NewsArticleRssResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for newsarticlerssresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| CurrentPaginationToken | integer (int32) |  | No |
| NextPaginationToken | integer (int32) |  | No |
| ResultCountThisPage | integer (int32) |  | No |
| NewsArticles | Array[Content.NewsArticleRssItem] |  | No |
| CategoryFilter | string |  | No |
| PagerAction | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.NewsArticleRssResponse object
const example = {
  CurrentPaginationToken: 123,
  NextPaginationToken: 123,
  ResultCountThisPage: 123,
  NewsArticles: [],
  CategoryFilter: "example value",
  // ... more properties
};
```

### Python
```python
# Example Content.NewsArticleRssResponse object
example = {
    "CurrentPaginationToken": 123,
    "NextPaginationToken": 123,
    "ResultCountThisPage": 123,
    "NewsArticles": [],
    "CategoryFilter": "example value",
    # ... more properties
}
```

## Related Entities
- **Content.NewsArticleRssItem**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.NewsArticleRssResponse":   {
      "type": "object",
      "properties": {
          "CurrentPaginationToken": {
              "format": "int32",
              "type": "integer"
          },
          "NextPaginationToken": {
              "format": "int32",
              "type": "integer"
          },
          "ResultCountThisPage": {
              "format": "int32",
              "type": "integer"
          },
          "NewsArticles": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.NewsArticleRssItem"
              }
          },
          "CategoryFilter": {
              "type": "string"
          },
          "PagerAction": {
              "type": "string"
          }
      }
  }
}
```
