# Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent

## Entity Information
- **Entity Name**: Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycraftablesocketplugcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugItemHash | integer (uint32) |  | No |
| failedRequirementIndexes | Array[integer] | Index into the unlock requirements to display failure descriptions | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent object
const example = {
  plugItemHash: 123,
  failedRequirementIndexes: [],
};
```

### Python
```python
# Example Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent object
example = {
    "plugItemHash": 123,
    "failedRequirementIndexes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent":   {
      "type": "object",
      "properties": {
          "plugItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "failedRequirementIndexes": {
              "description": "Index into the unlock requirements to display failure descriptions",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
