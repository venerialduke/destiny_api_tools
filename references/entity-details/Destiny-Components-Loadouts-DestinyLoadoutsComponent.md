# Destiny.Components.Loadouts.DestinyLoadoutsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Loadouts.DestinyLoadoutsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| loadouts | Array[Destiny.Components.Loadouts.DestinyLoadoutComponent] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Loadouts.DestinyLoadoutsComponent object
const example = {
  loadouts: [],
};
```

### Python
```python
# Example Destiny.Components.Loadouts.DestinyLoadoutsComponent object
example = {
    "loadouts": [],
}
```

## Related Entities
- **Destiny.Components.Loadouts.DestinyLoadoutComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Loadouts.DestinyLoadoutsComponent":   {
      "type": "object",
      "properties": {
          "loadouts": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Loadouts.DestinyLoadoutComponent"
              }
          }
      },
      "x-destiny-component-type-dependency": "CharacterLoadouts"
  }
}
```
