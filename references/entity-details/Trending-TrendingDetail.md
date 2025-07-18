# Trending.TrendingDetail

## Entity Information
- **Entity Name**: Trending.TrendingDetail
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for trendingdetail operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| identifier | string |  | No |
| entityType | integer (int32) |  | No |
| news | Trending.TrendingEntryNews |  | No |
| support | Trending.TrendingEntrySupportArticle |  | No |
| destinyItem | Trending.TrendingEntryDestinyItem |  | No |
| destinyActivity | Trending.TrendingEntryDestinyActivity |  | No |
| destinyRitual | Trending.TrendingEntryDestinyRitual |  | No |
| creation | Trending.TrendingEntryCommunityCreation |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingDetail object
const example = {
  identifier: "example value",
  entityType: 123,
  news: null,
  support: null,
  destinyItem: null,
  // ... more properties
};
```

### Python
```python
# Example Trending.TrendingDetail object
example = {
    "identifier": "example value",
    "entityType": 123,
    "news": None,
    "support": None,
    "destinyItem": None,
    # ... more properties
}
```

## Related Entities
- **Trending.TrendingEntryCommunityCreation**: Referenced in this entity
- **Trending.TrendingEntryDestinyActivity**: Referenced in this entity
- **Trending.TrendingEntryDestinyItem**: Referenced in this entity
- **Trending.TrendingEntryDestinyRitual**: Referenced in this entity
- **Trending.TrendingEntryNews**: Referenced in this entity
- **Trending.TrendingEntrySupportArticle**: Referenced in this entity
- **Trending.TrendingEntryType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Trending.TrendingDetail":   {
      "type": "object",
      "properties": {
          "identifier": {
              "type": "string"
          },
          "entityType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Trending.TrendingEntryType"
              }
          },
          "news": {
              "$ref": "#/definitions/Trending.TrendingEntryNews"
          },
          "support": {
              "$ref": "#/definitions/Trending.TrendingEntrySupportArticle"
          },
          "destinyItem": {
              "$ref": "#/definitions/Trending.TrendingEntryDestinyItem"
          },
          "destinyActivity": {
              "$ref": "#/definitions/Trending.TrendingEntryDestinyActivity"
          },
          "destinyRitual": {
              "$ref": "#/definitions/Trending.TrendingEntryDestinyRitual"
          },
          "creation": {
              "$ref": "#/definitions/Trending.TrendingEntryCommunityCreation"
          }
      }
  }
}
```
