# Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinysockettypescalarmaterialrequiremententry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| currencyItemHash | integer (uint32) |  | No |
| scalarValue | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry object
const example = {
  currencyItemHash: 123,
  scalarValue: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry object
example = {
    "currencyItemHash": 123,
    "scalarValue": 123,
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
  "Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry":   {
      "type": "object",
      "properties": {
          "currencyItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "scalarValue": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
