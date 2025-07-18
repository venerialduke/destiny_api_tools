# Destiny.Definitions.DestinyEntitySearchResultItem

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyEntitySearchResultItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
An individual Destiny Entity returned from the entity search.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| hash | integer (uint32) | The hash identifier of the entity. You will use this to look up the DestinyDefinition relevant for the entity found. | No |
| entityType | string | The type of entity, returned as a string matching the DestinyDefinition's contract class name. You'll have to have your own mapping from class names to actually looking up those definitions in the manifest databases. | No |
| displayProperties | object | Basic display properties on the entity, so you don't have to look up the definition to show basic results for the item. | No |
| weight | number (double) | The ranking value for sorting that we calculated using our relevance formula. This will hopefully get better with time and iteration. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyEntitySearchResultItem object
const example = {
  hash: 123,
  entityType: "example value",
  displayProperties: null,
  weight: 123.45,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyEntitySearchResultItem object
example = {
    "hash": 123,
    "entityType": "example value",
    "displayProperties": None,
    "weight": 123.45,
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
  "Destiny.Definitions.DestinyEntitySearchResultItem":   {
      "description": "An individual Destiny Entity returned from the entity search.",
      "type": "object",
      "properties": {
          "hash": {
              "format": "uint32",
              "description": "The hash identifier of the entity. You will use this to look up the DestinyDefinition relevant for the entity found.",
              "type": "integer"
          },
          "entityType": {
              "description": "The type of entity, returned as a string matching the DestinyDefinition's contract class name. You'll have to have your own mapping from class names to actually looking up those definitions in the manifest databases.",
              "type": "string"
          },
          "displayProperties": {
              "description": "Basic display properties on the entity, so you don't have to look up the definition to show basic results for the item.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "weight": {
              "format": "double",
              "description": "The ranking value for sorting that we calculated using our relevance formula. This will hopefully get better with time and iteration.",
              "type": "number"
          }
      }
  }
}
```
