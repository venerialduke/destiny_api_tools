# Destiny.DestinyScope

## Entity Information
- **Entity Name**: Destiny.DestinyScope
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
There's a lot of places where we need to know scope on more than just a profile or character level. For everything else, there's this more generic sense of scope.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Profile |  |
| 1 | Character |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyScope enumeration values
const DestinyScope = {
  Profile: 0,
  Character: 1,
};

// Using the enumeration
const value = DestinyScope.Profile;
```

### Python
```python
# Destiny.DestinyScope enumeration values
class DestinyScope:
    PROFILE = 0
    CHARACTER = 1

# Using the enumeration
value = DestinyScope.PROFILE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyScope":   {
      "format": "int32",
      "description": "There's a lot of places where we need to know scope on more than just a profile or character level. For everything else, there's this more generic sense of scope.",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
