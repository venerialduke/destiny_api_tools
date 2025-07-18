# Destiny.Definitions.Records.DestinyRecordIntervalRewards

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordIntervalRewards
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordintervalrewards data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| intervalRewardItems | Array[Destiny.DestinyItemQuantity] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.DestinyRecordIntervalRewards object
const example = {
  intervalRewardItems: [],
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordIntervalRewards object
example = {
    "intervalRewardItems": [],
}
```

## Related Entities
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordIntervalRewards":   {
      "type": "object",
      "properties": {
          "intervalRewardItems": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          }
      }
  }
}
```
