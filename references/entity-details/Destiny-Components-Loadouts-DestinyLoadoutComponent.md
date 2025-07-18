# Destiny.Components.Loadouts.DestinyLoadoutComponent

## Entity Information
- **Entity Name**: Destiny.Components.Loadouts.DestinyLoadoutComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| colorHash | integer (uint32) |  | No |
| iconHash | integer (uint32) |  | No |
| nameHash | integer (uint32) |  | No |
| items | Array[Destiny.Components.Loadouts.DestinyLoadoutItemComponent] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Loadouts.DestinyLoadoutComponent object
const example = {
  colorHash: 123,
  iconHash: 123,
  nameHash: 123,
  items: [],
};
```

### Python
```python
# Example Destiny.Components.Loadouts.DestinyLoadoutComponent object
example = {
    "colorHash": 123,
    "iconHash": 123,
    "nameHash": 123,
    "items": [],
}
```

## Related Entities
- **Destiny.Components.Loadouts.DestinyLoadoutItemComponent**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutColorDefinition**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutIconDefinition**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Loadouts.DestinyLoadoutComponent":   {
      "type": "object",
      "properties": {
          "colorHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutColorDefinition"
              }
          },
          "iconHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutIconDefinition"
              }
          },
          "nameHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition"
              }
          },
          "items": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Loadouts.DestinyLoadoutItemComponent"
              }
          }
      }
  }
}
```
