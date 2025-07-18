# Destiny.Misc.DestinyColor

## Entity Information
- **Entity Name**: Destiny.Misc.DestinyColor
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a color whose RGBA values are all represented as values between 0 and 255.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| red | string (byte) |  | No |
| green | string (byte) |  | No |
| blue | string (byte) |  | No |
| alpha | string (byte) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Misc.DestinyColor object
const example = {
  red: "example value",
  green: "example value",
  blue: "example value",
  alpha: "example value",
};
```

### Python
```python
# Example Destiny.Misc.DestinyColor object
example = {
    "red": "example value",
    "green": "example value",
    "blue": "example value",
    "alpha": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Misc.DestinyColor":   {
      "description": "Represents a color whose RGBA values are all represented as values between 0 and 255.",
      "type": "object",
      "properties": {
          "red": {
              "format": "byte",
              "type": "string"
          },
          "green": {
              "format": "byte",
              "type": "string"
          },
          "blue": {
              "format": "byte",
              "type": "string"
          },
          "alpha": {
              "format": "byte",
              "type": "string"
          }
      }
  }
}
```
