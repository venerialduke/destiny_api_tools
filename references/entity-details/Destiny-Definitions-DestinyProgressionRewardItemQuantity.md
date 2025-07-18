# Destiny.Definitions.DestinyProgressionRewardItemQuantity

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyProgressionRewardItemQuantity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyprogressionrewarditemquantity data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rewardItemIndex | integer (int32) |  | No |
| rewardedAtProgressionLevel | integer (int32) |  | No |
| acquisitionBehavior | integer (int32) |  | No |
| uiDisplayStyle | string |  | No |
| claimUnlockDisplayStrings | Array[string] |  | No |
| socketOverrides | Array[Destiny.Definitions.DestinyProgressionSocketPlugOverride] |  | No |
| itemHash | integer (uint32) | The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition. | No |
| itemInstanceId | integer (int64) | If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null. | No |
| quantity | integer (int32) | The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used. | No |
| hasConditionalVisibility | boolean | Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyProgressionRewardItemQuantity object
const example = {
  rewardItemIndex: 123,
  rewardedAtProgressionLevel: 123,
  acquisitionBehavior: 123,
  uiDisplayStyle: "example value",
  claimUnlockDisplayStrings: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyProgressionRewardItemQuantity object
example = {
    "rewardItemIndex": 123,
    "rewardedAtProgressionLevel": 123,
    "acquisitionBehavior": 123,
    "uiDisplayStyle": "example value",
    "claimUnlockDisplayStrings": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionSocketPlugOverride**: Referenced in this entity
- **Destiny.DestinyProgressionRewardItemAcquisitionBehavior**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyProgressionRewardItemQuantity":   {
      "type": "object",
      "properties": {
          "rewardItemIndex": {
              "format": "int32",
              "type": "integer"
          },
          "rewardedAtProgressionLevel": {
              "format": "int32",
              "type": "integer"
          },
          "acquisitionBehavior": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyProgressionRewardItemAcquisitionBehavior"
              }
          },
          "uiDisplayStyle": {
              "type": "string"
          },
          "claimUnlockDisplayStrings": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "socketOverrides": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionSocketPlugOverride"
              }
          },
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "itemInstanceId": {
              "format": "int64",
              "description": "If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.",
              "type": "integer"
          },
          "quantity": {
              "format": "int32",
              "description": "The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.",
              "type": "integer"
          },
          "hasConditionalVisibility": {
              "description": "Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.",
              "type": "boolean"
          }
      }
  }
}
```
