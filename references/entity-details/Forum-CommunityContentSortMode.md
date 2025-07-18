# Forum.CommunityContentSortMode

## Entity Information
- **Entity Name**: Forum.CommunityContentSortMode
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for communitycontentsortmode operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Trending |  |
| 1 | Latest |  |
| 2 | HighestRated |  |

## Usage Examples

### JavaScript
```javascript
// Forum.CommunityContentSortMode enumeration values
const CommunityContentSortMode = {
  Trending: 0,
  Latest: 1,
  HighestRated: 2,
};

// Using the enumeration
const value = CommunityContentSortMode.Trending;
```

### Python
```python
# Forum.CommunityContentSortMode enumeration values
class CommunityContentSortMode:
    TRENDING = 0
    LATEST = 1
    HIGHESTRATED = 2

# Using the enumeration
value = CommunityContentSortMode.TRENDING
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.CommunityContentSortMode":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
