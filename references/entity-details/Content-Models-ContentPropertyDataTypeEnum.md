# Content.Models.ContentPropertyDataTypeEnum

## Entity Information
- **Entity Name**: Content.Models.ContentPropertyDataTypeEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for contentpropertydatatypeenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Plaintext |  |
| 2 | Html |  |
| 3 | Dropdown |  |
| 4 | List |  |
| 5 | Json |  |
| 6 | Content |  |
| 7 | Representation |  |
| 8 | Set |  |
| 9 | File |  |
| 10 | FolderSet |  |
| 11 | Date |  |
| 12 | MultilinePlaintext |  |
| 13 | DestinyContent |  |
| 14 | Color |  |

## Usage Examples

### JavaScript
```javascript
// Content.Models.ContentPropertyDataTypeEnum enumeration values
const ContentPropertyDataTypeEnum = {
  None: 0,
  Plaintext: 1,
  Html: 2,
  // ... more values
};

// Using the enumeration
const value = ContentPropertyDataTypeEnum.None;
```

### Python
```python
# Content.Models.ContentPropertyDataTypeEnum enumeration values
class ContentPropertyDataTypeEnum:
    NONE = 0
    PLAINTEXT = 1
    HTML = 2
    # ... more values

# Using the enumeration
value = ContentPropertyDataTypeEnum.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Content.Models.ContentPropertyDataTypeEnum":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13",
          "14"
      ],
      "type": "integer"
  }
}
```
