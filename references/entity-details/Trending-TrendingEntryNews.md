# Trending.TrendingEntryNews

## Entity Information
- **Entity Name**: Trending.TrendingEntryNews
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for trendingentrynews operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| article | Content.ContentItemPublicContract |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntryNews object
const example = {
  article: null,
};
```

### Python
```python
# Example Trending.TrendingEntryNews object
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
  "Trending.TrendingEntryNews":   {
      "type": "object",
      "properties": {
          "article": {
              "$ref": "#/definitions/Content.ContentItemPublicContract"
          }
      }
  }
}
```
