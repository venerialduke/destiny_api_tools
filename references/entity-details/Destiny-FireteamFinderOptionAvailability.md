# Destiny.FireteamFinderOptionAvailability

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionAvailability
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptionavailability data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | CreateListingBuilder |  |
| 2 | SearchListingBuilder |  |
| 4 | ListingViewer |  |
| 8 | LobbyViewer |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionAvailability enumeration values
const FireteamFinderOptionAvailability = {
  None: 0,
  CreateListingBuilder: 1,
  SearchListingBuilder: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamFinderOptionAvailability.None;
```

### Python
```python
# Destiny.FireteamFinderOptionAvailability enumeration values
class FireteamFinderOptionAvailability:
    NONE = 0
    CREATELISTINGBUILDER = 1
    SEARCHLISTINGBUILDER = 2
    # ... more values

# Using the enumeration
value = FireteamFinderOptionAvailability.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionAvailability":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8"
      ],
      "type": "integer"
  }
}
```
