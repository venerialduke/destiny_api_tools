# Trending.TrendingEntrySupportArticle

## Entity Information
- **Entity Name**: Trending.TrendingEntrySupportArticle
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for trendingentrysupportarticle operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| article | Content.ContentItemPublicContract |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntrySupportArticle object
const example = {
  article: null,
};
```

### Python
```python
# Example Trending.TrendingEntrySupportArticle object
example = {
    "article": None,
}
```

## Related Entities
- **Content.ContentItemPublicContract**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Trending.TrendingEntrySupportArticle":   {
      "type": "object",
      "properties": {
          "article": {
              "$ref": "#/definitions/Content.ContentItemPublicContract"
          }
      }
  }
}
```
