# Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityselectableskullcollectionselectiontype data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| selectionCount | integer (int32) |  | No |
| refreshTimeMinutes | integer (int32) |  | No |
| refreshTimeOffsetMinutes | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType object
const example = {
  selectionCount: 123,
  refreshTimeMinutes: 123,
  refreshTimeOffsetMinutes: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType object
example = {
    "selectionCount": 123,
    "refreshTimeMinutes": 123,
    "refreshTimeOffsetMinutes": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType":   {
      "type": "object",
      "properties": {
          "selectionCount": {
              "format": "int32",
              "type": "integer"
          },
          "refreshTimeMinutes": {
              "format": "int32",
              "type": "integer"
          },
          "refreshTimeOffsetMinutes": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
