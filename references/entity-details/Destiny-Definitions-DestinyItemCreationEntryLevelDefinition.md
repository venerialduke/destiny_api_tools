# Destiny.Definitions.DestinyItemCreationEntryLevelDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemCreationEntryLevelDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
An overly complicated wrapper for the item level at which the item should spawn.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| level | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemCreationEntryLevelDefinition object
const example = {
  level: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemCreationEntryLevelDefinition object
example = {
    "level": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemCreationEntryLevelDefinition":   {
      "description": "An overly complicated wrapper for the item level at which the item should spawn.",
      "type": "object",
      "properties": {
          "level": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
