# Destiny.DestinyEquipItemResults

## Entity Information
- **Entity Name**: Destiny.DestinyEquipItemResults
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The results of a bulk Equipping operation performed through the Destiny API.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| equipResults | Array[Destiny.DestinyEquipItemResult] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyEquipItemResults object
const example = {
  equipResults: [],
};
```

### Python
```python
# Example Destiny.DestinyEquipItemResults object
example = {
    "equipResults": [],
}
```

## Related Entities
- **Destiny.DestinyEquipItemResult**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyEquipItemResults":   {
      "description": "The results of a bulk Equipping operation performed through the Destiny API.",
      "type": "object",
      "properties": {
          "equipResults": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyEquipItemResult"
              }
          }
      }
  }
}
```
