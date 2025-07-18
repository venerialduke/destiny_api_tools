# Destiny.Definitions.DestinyItemActionBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemActionBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If an item can have an action performed on it (like "Dismantle"), it will be defined here if you care.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| verbName | string | Localized text for the verb of the action being performed. | No |
| verbDescription | string | Localized text describing the action being performed. | No |
| isPositive | boolean | The content has this property, however it's not entirely clear how it is used. | No |
| overlayScreenName | string | If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen's data itself. | No |
| overlayIcon | string | The icon associated with the overlay screen for the action, if any. | No |
| requiredCooldownSeconds | integer (int32) | The number of seconds to delay before allowing this action to be performed again. | No |
| requiredItems | Array[Destiny.Definitions.DestinyItemActionRequiredItemDefinition] | If the action requires other items to exist or be destroyed, this is the list of those items and requirements. | No |
| progressionRewards | Array[Destiny.Definitions.DestinyProgressionRewardDefinition] | If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action. | No |
| actionTypeLabel | string | The internal identifier for the action. | No |
| requiredLocation | string | Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property. | No |
| requiredCooldownHash | integer (uint32) | The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns. | No |
| deleteOnAction | boolean | If true, the item is deleted when the action completes. | No |
| consumeEntireStack | boolean | If true, the entire stack is deleted when the action completes. | No |
| useOnAcquire | boolean | If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemActionBlockDefinition object
const example = {
  verbName: "example value",
  verbDescription: "example value",
  isPositive: true,
  overlayScreenName: "example value",
  overlayIcon: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemActionBlockDefinition object
example = {
    "verbName": "example value",
    "verbDescription": "example value",
    "isPositive": True,
    "overlayScreenName": "example value",
    "overlayIcon": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyItemActionRequiredItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionRewardDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemActionBlockDefinition":   {
      "description": "If an item can have an action performed on it (like \"Dismantle\"), it will be defined here if you care.",
      "type": "object",
      "properties": {
          "verbName": {
              "description": "Localized text for the verb of the action being performed.",
              "type": "string"
          },
          "verbDescription": {
              "description": "Localized text describing the action being performed.",
              "type": "string"
          },
          "isPositive": {
              "description": "The content has this property, however it's not entirely clear how it is used.",
              "type": "boolean"
          },
          "overlayScreenName": {
              "description": "If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen's data itself.",
              "type": "string"
          },
          "overlayIcon": {
              "description": "The icon associated with the overlay screen for the action, if any.",
              "type": "string"
          },
          "requiredCooldownSeconds": {
              "format": "int32",
              "description": "The number of seconds to delay before allowing this action to be performed again.",
              "type": "integer"
          },
          "requiredItems": {
              "description": "If the action requires other items to exist or be destroyed, this is the list of those items and requirements.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemActionRequiredItemDefinition"
              }
          },
          "progressionRewards": {
              "description": "If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionRewardDefinition"
              }
          },
          "actionTypeLabel": {
              "description": "The internal identifier for the action.",
              "type": "string"
          },
          "requiredLocation": {
              "description": "Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property.",
              "type": "string"
          },
          "requiredCooldownHash": {
              "format": "uint32",
              "description": "The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns.",
              "type": "integer"
          },
          "deleteOnAction": {
              "description": "If true, the item is deleted when the action completes.",
              "type": "boolean"
          },
          "consumeEntireStack": {
              "description": "If true, the entire stack is deleted when the action completes.",
              "type": "boolean"
          },
          "useOnAcquire": {
              "description": "If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items.",
              "type": "boolean"
          }
      }
  }
}
```
