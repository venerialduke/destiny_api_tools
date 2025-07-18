# Destiny.Advanced.AwaResponseReason

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaResponseReason
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing awaresponsereason data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Answered | User provided an answer |
| 2 | TimedOut | The HTTP request timed out, a new request may be made and an answer may still be provided. |
| 3 | Replaced | This request was replaced by another request. |

## Usage Examples

### JavaScript
```javascript
// Destiny.Advanced.AwaResponseReason enumeration values
const AwaResponseReason = {
  None: 0,
  Answered: 1,
  TimedOut: 2,
  // ... more values
};

// Using the enumeration
const value = AwaResponseReason.None;
```

### Python
```python
# Destiny.Advanced.AwaResponseReason enumeration values
class AwaResponseReason:
    NONE = 0
    ANSWERED = 1
    TIMEDOUT = 2
    # ... more values

# Using the enumeration
value = AwaResponseReason.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaResponseReason":   {
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
