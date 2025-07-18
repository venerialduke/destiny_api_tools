# Destiny.HistoricalStats.Definitions.PeriodType[]

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.PeriodType[]
- **Entity Type**: Schema (array)
- **Base Type**: array

## Description
Destiny API entity representing periodtype[] data.

## Usage Examples

### JavaScript
```javascript
```

### Python
```python
```

## Related Entities
- **Destiny.HistoricalStats.Definitions.PeriodType**: Referenced in this entity

## Notes
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.PeriodType[]":   {
      "type": "array",
      "items": {
          "format": "int32",
          "type": "integer",
          "x-enum-reference": {
              "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.PeriodType"
          }
      }
  }
}
```
