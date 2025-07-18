# Destiny.Components.Collectibles.DestinyCollectibleComponent

## Entity Information
- **Entity Name**: Destiny.Components.Collectibles.DestinyCollectibleComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycollectiblecomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| state | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Collectibles.DestinyCollectibleComponent object
const example = {
  state: 123,
};
```

### Python
```python
# Example Destiny.Components.Collectibles.DestinyCollectibleComponent object
example = {
    "state": 123,
}
```

## Related Entities
- **Destiny.DestinyCollectibleState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Collectibles.DestinyCollectibleComponent":   {
      "type": "object",
      "properties": {
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyCollectibleState"
              }
          }
      }
  }
}
```
