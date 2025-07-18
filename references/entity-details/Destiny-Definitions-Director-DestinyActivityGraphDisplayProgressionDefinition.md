# Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
When a Graph needs to show active Progressions, this defines those objectives as well as an identifier.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| id | integer (uint32) |  | No |
| progressionHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition object
const example = {
  id: 123,
  progressionHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition object
example = {
    "id": 123,
    "progressionHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition":   {
      "description": "When a Graph needs to show active Progressions, this defines those objectives as well as an identifier.",
      "type": "object",
      "properties": {
          "id": {
              "format": "uint32",
              "type": "integer"
          },
          "progressionHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
