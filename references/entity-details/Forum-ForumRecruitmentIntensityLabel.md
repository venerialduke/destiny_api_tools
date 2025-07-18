# Forum.ForumRecruitmentIntensityLabel

## Entity Information
- **Entity Name**: Forum.ForumRecruitmentIntensityLabel
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for forumrecruitmentintensitylabel operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Casual |  |
| 2 | Professional |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumRecruitmentIntensityLabel enumeration values
const ForumRecruitmentIntensityLabel = {
  None: 0,
  Casual: 1,
  Professional: 2,
};

// Using the enumeration
const value = ForumRecruitmentIntensityLabel.None;
```

### Python
```python
# Forum.ForumRecruitmentIntensityLabel enumeration values
class ForumRecruitmentIntensityLabel:
    NONE = 0
    CASUAL = 1
    PROFESSIONAL = 2

# Using the enumeration
value = ForumRecruitmentIntensityLabel.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumRecruitmentIntensityLabel":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
