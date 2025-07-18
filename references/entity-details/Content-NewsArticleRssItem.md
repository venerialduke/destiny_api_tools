# Content.NewsArticleRssItem

## Entity Information
- **Entity Name**: Content.NewsArticleRssItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for newsarticlerssitem operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| Title | string |  | No |
| Link | string |  | No |
| PubDate | string (date-time) |  | No |
| UniqueIdentifier | string |  | No |
| Description | string |  | No |
| HtmlContent | string |  | No |
| ImagePath | string |  | No |
| OptionalMobileImagePath | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.NewsArticleRssItem object
const example = {
  Title: "example value",
  Link: "example value",
  PubDate: "example value",
  UniqueIdentifier: "example value",
  Description: "example value",
  // ... more properties
};
```

### Python
```python
# Example Content.NewsArticleRssItem object
example = {
    "Title": "example value",
    "Link": "example value",
    "PubDate": "example value",
    "UniqueIdentifier": "example value",
    "Description": "example value",
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.NewsArticleRssItem":   {
      "type": "object",
      "properties": {
          "Title": {
              "type": "string"
          },
          "Link": {
              "type": "string"
          },
          "PubDate": {
              "format": "date-time",
              "type": "string"
          },
          "UniqueIdentifier": {
              "type": "string"
          },
          "Description": {
              "type": "string"
          },
          "HtmlContent": {
              "type": "string"
          },
          "ImagePath": {
              "type": "string"
          },
          "OptionalMobileImagePath": {
              "type": "string"
          }
      }
  }
}
```
