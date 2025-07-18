# Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Not terribly useful, some basic cooldown interaction info.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| executeSeconds | number (float) |  | No |
| isPositive | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition object
const example = {
  executeSeconds: 123.45,
  isPositive: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition object
example = {
    "executeSeconds": 123.45,
    "isPositive": True,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition":   {
      "description": "Not terribly useful, some basic cooldown interaction info.",
      "type": "object",
      "properties": {
          "executeSeconds": {
              "format": "float",
              "type": "number"
          },
          "isPositive": {
              "type": "boolean"
          }
      }
  }
}
```
