# Trending.TrendingCategories

## Entity Information
- **Entity Name**: Trending.TrendingCategories
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for trendingcategories operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categories | Array[Trending.TrendingCategory] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingCategories object
const example = {
  categories: [],
};
```

### Python
```python
# Example Trending.TrendingCategories object
example = {
    "categories": [],
}
```

## Related Entities
- **Trending.TrendingCategory**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Trending.TrendingCategories":   {
      "type": "object",
      "properties": {
          "categories": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Trending.TrendingCategory"
              }
          }
      }
  }
}
```
