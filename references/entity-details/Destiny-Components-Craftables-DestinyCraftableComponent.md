# Destiny.Components.Craftables.DestinyCraftableComponent

## Entity Information
- **Entity Name**: Destiny.Components.Craftables.DestinyCraftableComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycraftablecomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| visible | boolean |  | No |
| failedRequirementIndexes | Array[integer] | If the requirements are not met for crafting this item, these will index into the list of failure strings. | No |
| sockets | Array[Destiny.Components.Craftables.DestinyCraftableSocketComponent] | Plug item state for the crafting sockets. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Craftables.DestinyCraftableComponent object
const example = {
  visible: true,
  failedRequirementIndexes: [],
  sockets: [],
};
```

### Python
```python
# Example Destiny.Components.Craftables.DestinyCraftableComponent object
example = {
    "visible": True,
    "failedRequirementIndexes": [],
    "sockets": [],
}
```

## Related Entities
- **Destiny.Components.Craftables.DestinyCraftableSocketComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Craftables.DestinyCraftableComponent":   {
      "type": "object",
      "properties": {
          "visible": {
              "type": "boolean"
          },
          "failedRequirementIndexes": {
              "description": "If the requirements are not met for crafting this item, these will index into the list of failure strings.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "sockets": {
              "description": "Plug item state for the crafting sockets.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Craftables.DestinyCraftableSocketComponent"
              }
          }
      }
  }
}
```
