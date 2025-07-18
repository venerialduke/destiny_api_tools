# Trending.TrendingCategory

## Entity Information
- **Entity Name**: Trending.TrendingCategory
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for trendingcategory operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categoryName | string |  | No |
| entries | SearchResultOfTrendingEntry |  | No |
| categoryId | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingCategory object
const example = {
  categoryName: "example value",
  entries: null,
  categoryId: "example value",
};
```

### Python
```python
# Example Trending.TrendingCategory object
example = {
    "categoryName": "example value",
    "entries": None,
    "categoryId": "example value",
}
```

## Related Entities
- **SearchResultOfTrendingEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Trending.TrendingCategory":   {
      "type": "object",
      "properties": {
          "categoryName": {
              "type": "string"
          },
          "entries": {
              "$ref": "#/definitions/SearchResultOfTrendingEntry"
          },
          "categoryId": {
              "type": "string"
          }
      }
  }
}
```
