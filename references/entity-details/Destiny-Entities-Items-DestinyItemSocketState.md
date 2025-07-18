# Destiny.Entities.Items.DestinyItemSocketState

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemSocketState
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The status of a given item's socket. (which plug is inserted, if any: whether it is enabled, what "reusable" plugs can be inserted, etc...)
If I had it to do over, this would probably have a DestinyItemPlug representing the inserted item instead of most of these properties. :shrug:

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugHash | integer (uint32) | The currently active plug, if any.
Note that, because all plugs are statically defined, its effect on stats and perks can be statically determined using the plug item's definition. The stats and perks can be taken at face value on the plug item as the stats and perks it will provide to the user/item. | No |
| isEnabled | boolean | Even if a plug is inserted, it doesn't mean it's enabled.
This flag indicates whether the plug is active and providing its benefits. | No |
| isVisible | boolean | A plug may theoretically provide benefits but not be visible - for instance, some older items use a plug's damage type perk to modify their own damage type. These, though they are not visible, still affect the item. This field indicates that state.
An invisible plug, while it provides benefits if it is Enabled, cannot be directly modified by the user. | No |
| enableFailIndexes | Array[integer] | If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemSocketState object
const example = {
  plugHash: 123,
  isEnabled: true,
  isVisible: true,
  enableFailIndexes: [],
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemSocketState object
example = {
    "plugHash": 123,
    "isEnabled": True,
    "isVisible": True,
    "enableFailIndexes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemSocketState":   {
      "description": "The status of a given item's socket. (which plug is inserted, if any: whether it is enabled, what \"reusable\" plugs can be inserted, etc...)\r\nIf I had it to do over, this would probably have a DestinyItemPlug representing the inserted item instead of most of these properties. :shrug:",
      "type": "object",
      "properties": {
          "plugHash": {
              "format": "uint32",
              "description": "The currently active plug, if any.\r\nNote that, because all plugs are statically defined, its effect on stats and perks can be statically determined using the plug item's definition. The stats and perks can be taken at face value on the plug item as the stats and perks it will provide to the user/item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "isEnabled": {
              "description": "Even if a plug is inserted, it doesn't mean it's enabled.\r\nThis flag indicates whether the plug is active and providing its benefits.",
              "type": "boolean"
          },
          "isVisible": {
              "description": "A plug may theoretically provide benefits but not be visible - for instance, some older items use a plug's damage type perk to modify their own damage type. These, though they are not visible, still affect the item. This field indicates that state.\r\nAn invisible plug, while it provides benefits if it is Enabled, cannot be directly modified by the user.",
              "type": "boolean"
          },
          "enableFailIndexes": {
              "description": "If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
