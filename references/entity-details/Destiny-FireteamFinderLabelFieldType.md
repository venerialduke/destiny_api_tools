# Destiny.FireteamFinderLabelFieldType

## Entity Information
- **Entity Name**: Destiny.FireteamFinderLabelFieldType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderlabelfieldtype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Title |  |
| 1 | Label |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderLabelFieldType enumeration values
const FireteamFinderLabelFieldType = {
  Title: 0,
  Label: 1,
};

// Using the enumeration
const value = FireteamFinderLabelFieldType.Title;
```

### Python
```python
# Destiny.FireteamFinderLabelFieldType enumeration values
class FireteamFinderLabelFieldType:
    TITLE = 0
    LABEL = 1

# Using the enumeration
value = FireteamFinderLabelFieldType.TITLE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderLabelFieldType":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
