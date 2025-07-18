# Destiny.DestinyProgressionResetEntry

## Entity Information
- **Entity Name**: Destiny.DestinyProgressionResetEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a season and the number of resets you had in that season.
 We do not necessarily - even for progressions with resets - track it over all seasons. So be careful and check the season numbers being returned.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| season | integer (int32) |  | No |
| resets | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyProgressionResetEntry object
const example = {
  season: 123,
  resets: 123,
};
```

### Python
```python
# Example Destiny.DestinyProgressionResetEntry object
example = {
    "season": 123,
    "resets": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgressionResetEntry":   {
      "description": "Represents a season and the number of resets you had in that season.\r\n We do not necessarily - even for progressions with resets - track it over all seasons. So be careful and check the season numbers being returned.",
      "type": "object",
      "properties": {
          "season": {
              "format": "int32",
              "type": "integer"
          },
          "resets": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
