# Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutnamedefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition object
const example = {
  name: "example value",
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition object
example = {
    "name": "example value",
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "LoadoutNames"
  }
}
```
