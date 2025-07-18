# Applications.OAuthApplicationType

## Entity Information
- **Entity Name**: Applications.OAuthApplicationType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for oauthapplicationtype operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Confidential | Indicates the application is server based and can keep its secrets from end users and other potential snoops. |
| 2 | Public | Indicates the application runs in a public place, and it can't be trusted to keep a secret. |

## Usage Examples

### JavaScript
```javascript
// Applications.OAuthApplicationType enumeration values
const OAuthApplicationType = {
  None: 0,
  Confidential: 1,
  Public: 2,
};

// Using the enumeration
const value = OAuthApplicationType.None;
```

### Python
```python
# Applications.OAuthApplicationType enumeration values
class OAuthApplicationType:
    NONE = 0
    CONFIDENTIAL = 1
    PUBLIC = 2

# Using the enumeration
value = OAuthApplicationType.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Applications.OAuthApplicationType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
