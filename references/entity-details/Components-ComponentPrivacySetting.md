# Components.ComponentPrivacySetting

## Entity Information
- **Entity Name**: Components.ComponentPrivacySetting
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A set of flags for reason(s) why the component populated in the way that it did. Inspect the individual flags for the reasons.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Public |  |
| 2 | Private |  |

## Usage Examples

### JavaScript
```javascript
// Components.ComponentPrivacySetting enumeration values
const ComponentPrivacySetting = {
  None: 0,
  Public: 1,
  Private: 2,
};

// Using the enumeration
const value = ComponentPrivacySetting.None;
```

### Python
```python
# Components.ComponentPrivacySetting enumeration values
class ComponentPrivacySetting:
    NONE = 0
    PUBLIC = 1
    PRIVATE = 2

# Using the enumeration
value = ComponentPrivacySetting.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Components.ComponentPrivacySetting":   {
      "format": "int32",
      "description": "A set of flags for reason(s) why the component populated in the way that it did. Inspect the individual flags for the reasons.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
