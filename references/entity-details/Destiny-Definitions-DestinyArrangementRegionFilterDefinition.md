# Destiny.Definitions.DestinyArrangementRegionFilterDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyArrangementRegionFilterDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyarrangementregionfilterdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| artArrangementRegionHash | integer (uint32) |  | No |
| artArrangementRegionIndex | integer (int32) |  | No |
| statHash | integer (uint32) |  | No |
| arrangementIndexByStatValue | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyArrangementRegionFilterDefinition object
const example = {
  artArrangementRegionHash: 123,
  artArrangementRegionIndex: 123,
  statHash: 123,
  arrangementIndexByStatValue: null,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyArrangementRegionFilterDefinition object
example = {
    "artArrangementRegionHash": 123,
    "artArrangementRegionIndex": 123,
    "statHash": 123,
    "arrangementIndexByStatValue": None,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyArrangementRegionFilterDefinition":   {
      "type": "object",
      "properties": {
          "artArrangementRegionHash": {
              "format": "uint32",
              "type": "integer"
          },
          "artArrangementRegionIndex": {
              "format": "int32",
              "type": "integer"
          },
          "statHash": {
              "format": "uint32",
              "type": "integer"
          },
          "arrangementIndexByStatValue": {
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
