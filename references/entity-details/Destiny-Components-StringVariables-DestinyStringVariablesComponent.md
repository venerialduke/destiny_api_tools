# Destiny.Components.StringVariables.DestinyStringVariablesComponent

## Entity Information
- **Entity Name**: Destiny.Components.StringVariables.DestinyStringVariablesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinystringvariablescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| integerValuesByHash | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.StringVariables.DestinyStringVariablesComponent object
const example = {
  integerValuesByHash: null,
};
```

### Python
```python
# Example Destiny.Components.StringVariables.DestinyStringVariablesComponent object
example = {
    "integerValuesByHash": None,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.StringVariables.DestinyStringVariablesComponent":   {
      "type": "object",
      "properties": {
          "integerValuesByHash": {
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      },
      "x-destiny-component-type-dependency": "StringVariables"
  }
}
```
