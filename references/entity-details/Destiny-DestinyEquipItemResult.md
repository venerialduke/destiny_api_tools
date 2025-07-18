# Destiny.DestinyEquipItemResult

## Entity Information
- **Entity Name**: Destiny.DestinyEquipItemResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The results of an Equipping operation performed through the Destiny API.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemInstanceId | integer (int64) | The instance ID of the item in question (all items that can be equipped must, but definition, be Instanced and thus have an Instance ID that you can use to refer to them) | No |
| equipStatus | integer (int32) | A PlatformErrorCodes enum indicating whether it succeeded, and if it failed why. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyEquipItemResult object
const example = {
  itemInstanceId: 123,
  equipStatus: 123,
};
```

### Python
```python
# Example Destiny.DestinyEquipItemResult object
example = {
    "itemInstanceId": 123,
    "equipStatus": 123,
}
```

## Related Entities
- **Exceptions.PlatformErrorCodes**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyEquipItemResult":   {
      "description": "The results of an Equipping operation performed through the Destiny API.",
      "type": "object",
      "properties": {
          "itemInstanceId": {
              "format": "int64",
              "description": "The instance ID of the item in question (all items that can be equipped must, but definition, be Instanced and thus have an Instance ID that you can use to refer to them)",
              "type": "integer"
          },
          "equipStatus": {
              "format": "int32",
              "description": "A PlatformErrorCodes enum indicating whether it succeeded, and if it failed why.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Exceptions.PlatformErrorCodes"
              }
          }
      }
  }
}
```
