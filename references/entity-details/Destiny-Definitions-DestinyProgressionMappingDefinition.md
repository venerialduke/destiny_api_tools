# Destiny.Definitions.DestinyProgressionMappingDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyProgressionMappingDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Aggregations of multiple progressions.
These are used to apply rewards to multiple progressions at once. They can sometimes have human readable data as well, but only extremely sporadically.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | Infrequently defined in practice. Defer to the individual progressions' display properties. | No |
| displayUnits | string | The localized unit of measurement for progression across the progressions defined in this mapping. Unfortunately, this is very infrequently defined. Defer to the individual progressions' display units. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyProgressionMappingDefinition object
const example = {
  displayProperties: null,
  displayUnits: "example value",
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyProgressionMappingDefinition object
example = {
    "displayProperties": None,
    "displayUnits": "example value",
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyProgressionMappingDefinition":   {
      "description": "Aggregations of multiple progressions.\r\nThese are used to apply rewards to multiple progressions at once. They can sometimes have human readable data as well, but only extremely sporadically.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "Infrequently defined in practice. Defer to the individual progressions' display properties.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "displayUnits": {
              "description": "The localized unit of measurement for progression across the progressions defined in this mapping. Unfortunately, this is very infrequently defined. Defer to the individual progressions' display units.",
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
      }
  }
}
```
