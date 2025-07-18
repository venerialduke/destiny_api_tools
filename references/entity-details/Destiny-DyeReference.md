# Destiny.DyeReference

## Entity Information
- **Entity Name**: Destiny.DyeReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing dyereference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| channelHash | integer (uint32) |  | No |
| dyeHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DyeReference object
const example = {
  channelHash: 123,
  dyeHash: 123,
};
```

### Python
```python
# Example Destiny.DyeReference object
example = {
    "channelHash": 123,
    "dyeHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DyeReference":   {
      "type": "object",
      "properties": {
          "channelHash": {
              "format": "uint32",
              "type": "integer"
          },
          "dyeHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
