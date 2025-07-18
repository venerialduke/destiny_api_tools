# Destiny.Definitions.Activities.DestinyActivitySkullOption

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivitySkullOption
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityskulloption data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| optionHash | integer (uint32) |  | No |
| stringValue | string |  | No |
| boolValue | boolean |  | No |
| integerValue | integer (int32) |  | No |
| floatValue | number (float) |  | No |
| minDisplayDifficultyId | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivitySkullOption object
const example = {
  optionHash: 123,
  stringValue: "example value",
  boolValue: true,
  integerValue: 123,
  floatValue: 123.45,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivitySkullOption object
example = {
    "optionHash": 123,
    "stringValue": "example value",
    "boolValue": True,
    "integerValue": 123,
    "floatValue": 123.45,
    # ... more properties
}
```

## Related Entities
- **Destiny.DestinyActivityDifficultyId**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivitySkullOption":   {
      "type": "object",
      "properties": {
          "optionHash": {
              "format": "uint32",
              "type": "integer"
          },
          "stringValue": {
              "type": "string"
          },
          "boolValue": {
              "type": "boolean"
          },
          "integerValue": {
              "format": "int32",
              "type": "integer"
          },
          "floatValue": {
              "format": "float",
              "type": "number"
          },
          "minDisplayDifficultyId": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityDifficultyId"
              }
          }
      }
  }
}
```
