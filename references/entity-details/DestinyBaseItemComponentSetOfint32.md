# DestinyBaseItemComponentSetOfint32

## Entity Information
- **Entity Name**: DestinyBaseItemComponentSetOfint32
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinybaseitemcomponentsetofint32 data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectives | DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent |  | No |
| perks | DictionaryComponentResponseOfint32AndDestinyItemPerksComponent |  | No |

## Usage Examples

### JavaScript
```javascript
// Example DestinyBaseItemComponentSetOfint32 object
const example = {
  objectives: null,
  perks: null,
};
```

### Python
```python
# Example DestinyBaseItemComponentSetOfint32 object
example = {
    "objectives": None,
    "perks": None,
}
```

## Related Entities
- **DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyItemPerksComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DestinyBaseItemComponentSetOfint32":   {
      "type": "object",
      "properties": {
          "objectives": {
              "x-destiny-component-type-dependency": "ItemObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent"
          },
          "perks": {
              "x-destiny-component-type-dependency": "ItemPerks",
              "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyItemPerksComponent"
          }
      }
  }
}
```
