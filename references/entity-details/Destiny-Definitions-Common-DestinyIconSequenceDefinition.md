# Destiny.Definitions.Common.DestinyIconSequenceDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Common.DestinyIconSequenceDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyiconsequencedefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| frames | Array[string] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Common.DestinyIconSequenceDefinition object
const example = {
  frames: [],
};
```

### Python
```python
# Example Destiny.Definitions.Common.DestinyIconSequenceDefinition object
example = {
    "frames": [],
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Common.DestinyIconSequenceDefinition":   {
      "type": "object",
      "properties": {
          "frames": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          }
      }
  }
}
```
