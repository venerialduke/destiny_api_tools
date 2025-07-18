# Trending.TrendingEntryType

## Entity Information
- **Entity Name**: Trending.TrendingEntryType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The known entity types that you can have returned from Trending.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | News |  |
| 1 | DestinyItem |  |
| 2 | DestinyActivity |  |
| 3 | DestinyRitual |  |
| 4 | SupportArticle |  |
| 5 | Creation |  |
| 6 | Stream |  |
| 7 | Update |  |
| 8 | Link |  |
| 9 | ForumTag |  |
| 10 | Container |  |
| 11 | Release |  |

## Usage Examples

### JavaScript
```javascript
// Trending.TrendingEntryType enumeration values
const TrendingEntryType = {
  News: 0,
  DestinyItem: 1,
  DestinyActivity: 2,
  // ... more values
};

// Using the enumeration
const value = TrendingEntryType.News;
```

### Python
```python
# Trending.TrendingEntryType enumeration values
class TrendingEntryType:
    NEWS = 0
    DESTINYITEM = 1
    DESTINYACTIVITY = 2
    # ... more values

# Using the enumeration
value = TrendingEntryType.NEWS
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Trending.TrendingEntryType":   {
      "format": "int32",
      "description": "The known entity types that you can have returned from Trending.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11"
      ],
      "type": "integer"
  }
}
```
