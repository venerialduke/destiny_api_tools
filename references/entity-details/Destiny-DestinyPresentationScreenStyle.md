# Destiny.DestinyPresentationScreenStyle

## Entity Information
- **Entity Name**: Destiny.DestinyPresentationScreenStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A hint for what screen should be shown when this presentation node is clicked into. How you use this is your UI is up to you.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default | Use the "default" view for the presentation nodes. |
| 1 | CategorySets | Show sub-items as "category sets". In-game, you'd see these as a vertical list of child presentation nodes - armor sets for example - and the icons of items within those sets displayed horizontally. |
| 2 | Badge | Show sub-items as Badges. (I know, I know. We don't need no stinkin' badges har har har) |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyPresentationScreenStyle enumeration values
const DestinyPresentationScreenStyle = {
  Default: 0,
  CategorySets: 1,
  Badge: 2,
};

// Using the enumeration
const value = DestinyPresentationScreenStyle.Default;
```

### Python
```python
# Destiny.DestinyPresentationScreenStyle enumeration values
class DestinyPresentationScreenStyle:
    DEFAULT = 0
    CATEGORYSETS = 1
    BADGE = 2

# Using the enumeration
value = DestinyPresentationScreenStyle.DEFAULT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyPresentationScreenStyle":   {
      "format": "int32",
      "description": "A hint for what screen should be shown when this presentation node is clicked into. How you use this is your UI is up to you.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
