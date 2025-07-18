# DestinyBaseItemComponentSetOfuint32

## Entity Information
- **Entity Name**: DestinyBaseItemComponentSetOfuint32
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinybaseitemcomponentsetofuint32 data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectives | DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent |  | No |
| perks | DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent |  | No |

## Usage Examples

### JavaScript
```javascript
// Example DestinyBaseItemComponentSetOfuint32 object
const example = {
  objectives: null,
  perks: null,
};
```

### Python
```python
# Example DestinyBaseItemComponentSetOfuint32 object
example = {
    "objectives": None,
    "perks": None,
}
```

## Related Entities
- **DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DestinyBaseItemComponentSetOfuint32":   {
      "type": "object",
      "properties": {
          "objectives": {
              "x-destiny-component-type-dependency": "ItemObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent"
          },
          "perks": {
              "x-destiny-component-type-dependency": "ItemPerks",
              "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent"
          }
      }
  }
}
```
