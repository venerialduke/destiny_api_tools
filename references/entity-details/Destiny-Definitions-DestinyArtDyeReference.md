# Destiny.Definitions.DestinyArtDyeReference

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyArtDyeReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyartdyereference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| artDyeChannelHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyArtDyeReference object
const example = {
  artDyeChannelHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyArtDyeReference object
example = {
    "artDyeChannelHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyArtDyeReference":   {
      "type": "object",
      "properties": {
          "artDyeChannelHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
