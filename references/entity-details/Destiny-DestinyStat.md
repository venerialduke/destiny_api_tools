# Destiny.DestinyStat

## Entity Information
- **Entity Name**: Destiny.DestinyStat
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a stat on an item *or* Character (NOT a Historical Stat, but a physical attribute stat like Attack, Defense etc...)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statHash | integer (uint32) | The hash identifier for the Stat. Use it to look up the DestinyStatDefinition for static data about the stat. | No |
| value | integer (int32) | The current value of the Stat. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyStat object
const example = {
  statHash: 123,
  value: 123,
};
```

### Python
```python
# Example Destiny.DestinyStat object
example = {
    "statHash": 123,
    "value": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyStat":   {
      "description": "Represents a stat on an item *or* Character (NOT a Historical Stat, but a physical attribute stat like Attack, Defense etc...)",
      "type": "object",
      "properties": {
          "statHash": {
              "format": "uint32",
              "description": "The hash identifier for the Stat. Use it to look up the DestinyStatDefinition for static data about the stat.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "value": {
              "format": "int32",
              "description": "The current value of the Stat.",
              "type": "integer"
          }
      }
  }
}
```
