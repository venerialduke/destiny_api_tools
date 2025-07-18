# Tokens.CollectibleDefinitions

## Entity Information
- **Entity Name**: Tokens.CollectibleDefinitions
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for collectibledefinitions operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| CollectibleDefinition | Destiny.Definitions.Collectibles.DestinyCollectibleDefinition |  | No |
| DestinyInventoryItemDefinition | Destiny.Definitions.DestinyInventoryItemDefinition |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.CollectibleDefinitions object
const example = {
  CollectibleDefinition: null,
  DestinyInventoryItemDefinition: null,
};
```

### Python
```python
# Example Tokens.CollectibleDefinitions object
example = {
    "CollectibleDefinition": None,
    "DestinyInventoryItemDefinition": None,
}
```

## Related Entities
- **Destiny.Definitions.Collectibles.DestinyCollectibleDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.CollectibleDefinitions":   {
      "type": "object",
      "properties": {
          "CollectibleDefinition": {
              "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleDefinition"
          },
          "DestinyInventoryItemDefinition": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
          }
      }
  }
}
```
