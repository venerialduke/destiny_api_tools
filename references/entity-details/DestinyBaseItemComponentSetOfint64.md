# DestinyBaseItemComponentSetOfint64

## Entity Information
- **Entity Name**: DestinyBaseItemComponentSetOfint64
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinybaseitemcomponentsetofint64 data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectives | DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent |  | No |
| perks | DictionaryComponentResponseOfint64AndDestinyItemPerksComponent |  | No |

## Usage Examples

### JavaScript
```javascript
// Example DestinyBaseItemComponentSetOfint64 object
const example = {
  objectives: null,
  perks: null,
};
```

### Python
```python
# Example DestinyBaseItemComponentSetOfint64 object
example = {
    "objectives": None,
    "perks": None,
}
```

## Related Entities
- **DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyItemPerksComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DestinyBaseItemComponentSetOfint64":   {
      "type": "object",
      "properties": {
          "objectives": {
              "x-destiny-component-type-dependency": "ItemObjectives",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent"
          },
          "perks": {
              "x-destiny-component-type-dependency": "ItemPerks",
              "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyItemPerksComponent"
          }
      }
  }
}
```
