# Destiny.Definitions.Common.DestinyPositionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Common.DestinyPositionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypositiondefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| x | integer (int32) |  | No |
| y | integer (int32) |  | No |
| z | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Common.DestinyPositionDefinition object
const example = {
  x: 123,
  y: 123,
  z: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Common.DestinyPositionDefinition object
example = {
    "x": 123,
    "y": 123,
    "z": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Common.DestinyPositionDefinition":   {
      "type": "object",
      "properties": {
          "x": {
              "format": "int32",
              "type": "integer"
          },
          "y": {
              "format": "int32",
              "type": "integer"
          },
          "z": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
