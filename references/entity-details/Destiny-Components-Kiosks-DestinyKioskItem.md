# Destiny.Components.Kiosks.DestinyKioskItem

## Entity Information
- **Entity Name**: Destiny.Components.Kiosks.DestinyKioskItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinykioskitem data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| index | integer (int32) | The index of the item in the related DestinyVendorDefintion's itemList property, representing the sale. | No |
| canAcquire | boolean | If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it. | No |
| failureIndexes | Array[integer] | Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any. | No |
| flavorObjective | object | I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Kiosks.DestinyKioskItem object
const example = {
  index: 123,
  canAcquire: true,
  failureIndexes: [],
  flavorObjective: null,
};
```

### Python
```python
# Example Destiny.Components.Kiosks.DestinyKioskItem object
example = {
    "index": 123,
    "canAcquire": True,
    "failureIndexes": [],
    "flavorObjective": None,
}
```

## Related Entities
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Kiosks.DestinyKioskItem":   {
      "type": "object",
      "properties": {
          "index": {
              "format": "int32",
              "description": "The index of the item in the related DestinyVendorDefintion's itemList property, representing the sale.",
              "type": "integer"
          },
          "canAcquire": {
              "description": "If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it.",
              "type": "boolean"
          },
          "failureIndexes": {
              "description": "Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "flavorObjective": {
              "description": "I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for \"flavor\" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              ]
          }
      }
  }
}
```
