# Destiny.DestinySocketVisibility

## Entity Information
- **Entity Name**: Destiny.DestinySocketVisibility
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinysocketvisibility data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Visible |  |
| 1 | Hidden |  |
| 2 | HiddenWhenEmpty |  |
| 3 | HiddenIfNoPlugsAvailable |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinySocketVisibility enumeration values
const DestinySocketVisibility = {
  Visible: 0,
  Hidden: 1,
  HiddenWhenEmpty: 2,
  // ... more values
};

// Using the enumeration
const value = DestinySocketVisibility.Visible;
```

### Python
```python
# Destiny.DestinySocketVisibility enumeration values
class DestinySocketVisibility:
    VISIBLE = 0
    HIDDEN = 1
    HIDDENWHENEMPTY = 2
    # ... more values

# Using the enumeration
value = DestinySocketVisibility.VISIBLE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinySocketVisibility":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
