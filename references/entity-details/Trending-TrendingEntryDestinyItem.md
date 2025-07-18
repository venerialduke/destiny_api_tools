# Trending.TrendingEntryDestinyItem

## Entity Information
- **Entity Name**: Trending.TrendingEntryDestinyItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing trendingentrydestinyitem data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntryDestinyItem object
const example = {
  itemHash: 123,
};
```

### Python
```python
# Example Trending.TrendingEntryDestinyItem object
example = {
    "itemHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Trending.TrendingEntryDestinyItem":   {
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
