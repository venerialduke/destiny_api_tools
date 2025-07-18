# Fireteam.FireteamPlatformInviteResult

## Entity Information
- **Entity Name**: Fireteam.FireteamPlatformInviteResult
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for fireteamplatforminviteresult operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Success |  |
| 2 | AlreadyInFireteam |  |
| 3 | Throttled |  |
| 4 | ServiceError |  |

## Usage Examples

### JavaScript
```javascript
// Fireteam.FireteamPlatformInviteResult enumeration values
const FireteamPlatformInviteResult = {
  None: 0,
  Success: 1,
  AlreadyInFireteam: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamPlatformInviteResult.None;
```

### Python
```python
# Fireteam.FireteamPlatformInviteResult enumeration values
class FireteamPlatformInviteResult:
    NONE = 0
    SUCCESS = 1
    ALREADYINFIRETEAM = 2
    # ... more values

# Using the enumeration
value = FireteamPlatformInviteResult.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Fireteam.FireteamPlatformInviteResult":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
