# Destiny.Character.DestinyCharacterPeerView

## Entity Information
- **Entity Name**: Destiny.Character.DestinyCharacterPeerView
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A minimal view of a character's equipped items, for the purpose of rendering a summary screen or showing the character in 3D.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| equipment | Array[Destiny.Character.DestinyItemPeerView] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Character.DestinyCharacterPeerView object
const example = {
  equipment: [],
};
```

### Python
```python
# Example Destiny.Character.DestinyCharacterPeerView object
example = {
    "equipment": [],
}
```

## Related Entities
- **Destiny.Character.DestinyItemPeerView**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Character.DestinyCharacterPeerView":   {
      "description": "A minimal view of a character's equipped items, for the purpose of rendering a summary screen or showing the character in 3D.",
      "type": "object",
      "properties": {
          "equipment": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Character.DestinyItemPeerView"
              }
          }
      }
  }
}
```
