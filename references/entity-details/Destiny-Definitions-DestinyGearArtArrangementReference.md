# Destiny.Definitions.DestinyGearArtArrangementReference

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyGearArtArrangementReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinygearartarrangementreference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| classHash | integer (uint32) |  | No |
| artArrangementHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyGearArtArrangementReference object
const example = {
  classHash: 123,
  artArrangementHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyGearArtArrangementReference object
example = {
    "classHash": 123,
    "artArrangementHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyClassDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyGearArtArrangementReference":   {
      "type": "object",
      "properties": {
          "classHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyClassDefinition"
              }
          },
          "artArrangementHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
