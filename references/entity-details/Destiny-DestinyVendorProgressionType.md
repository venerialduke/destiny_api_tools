# Destiny.DestinyVendorProgressionType

## Entity Information
- **Entity Name**: Destiny.DestinyVendorProgressionType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Describes the type of progression that a vendor has.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default | The original rank progression from token redemption. |
| 1 | Ritual | Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Season 13 Battlegrounds (War Table). |
| 2 | NoSeasonalRefresh | A vendor progression with no seasonal refresh. For example: Xur in the Eternity destination for the 30th Anniversary. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyVendorProgressionType enumeration values
const DestinyVendorProgressionType = {
  Default: 0,
  Ritual: 1,
  NoSeasonalRefresh: 2,
};

// Using the enumeration
const value = DestinyVendorProgressionType.Default;
```

### Python
```python
# Destiny.DestinyVendorProgressionType enumeration values
class DestinyVendorProgressionType:
    DEFAULT = 0
    RITUAL = 1
    NOSEASONALREFRESH = 2

# Using the enumeration
value = DestinyVendorProgressionType.DEFAULT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyVendorProgressionType":   {
      "format": "int32",
      "description": "Describes the type of progression that a vendor has.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
