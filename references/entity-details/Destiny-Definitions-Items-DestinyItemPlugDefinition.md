# Destiny.Definitions.Items.DestinyItemPlugDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyItemPlugDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If an item is a Plug, its DestinyInventoryItemDefinition.plug property will be populated with an instance of one of these bad boys.
This gives information about when it can be inserted, what the plug's category is (and thus whether it is compatible with a socket... see DestinySocketTypeDefinition for information about Plug Categories and socket compatibility), whether it is enabled and other Plug info.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| insertionRules | Array[Destiny.Definitions.Items.DestinyPlugRuleDefinition] | The rules around when this plug can be inserted into a socket, aside from the socket's individual restrictions.
The live data DestinyItemPlugComponent.insertFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user. | No |
| plugCategoryIdentifier | string | The string identifier for the plug's category. Use the socket's DestinySocketTypeDefinition.plugWhitelist to determine whether this plug can be inserted into the socket. | No |
| plugCategoryHash | integer (uint32) | The hash for the plugCategoryIdentifier. You can use this instead if you wish: I put both in the definition for debugging purposes. | No |
| onActionRecreateSelf | boolean | If you successfully socket the item, this will determine whether or not you get "refunded" on the plug. | No |
| insertionMaterialRequirementHash | integer (uint32) | If inserting this plug requires materials, this is the hash identifier for looking up the DestinyMaterialRequirementSetDefinition for those requirements. | No |
| previewItemOverrideHash | integer (uint32) | In the game, if you're inspecting a plug item directly, this will be the item shown with the plug attached. Look up the DestinyInventoryItemDefinition for this hash for the item. | No |
| enabledMaterialRequirementHash | integer (uint32) | It's not enough for the plug to be inserted. It has to be enabled as well. For it to be enabled, it may require materials. This is the hash identifier for the DestinyMaterialRequirementSetDefinition for those requirements, if there is one. | No |
| enabledRules | Array[Destiny.Definitions.Items.DestinyPlugRuleDefinition] | The rules around whether the plug, once inserted, is enabled and providing its benefits.
The live data DestinyItemPlugComponent.enableFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user. | No |
| uiPlugLabel | string | Plugs can have arbitrary, UI-defined identifiers that the UI designers use to determine the style applied to plugs. Unfortunately, we have neither a definitive list of these labels nor advance warning of when new labels might be applied or how that relates to how they get rendered. If you want to, you can refer to known labels to change your own styles: but know that new ones can be created arbitrarily, and we have no way of associating the labels with any specific UI style guidance... you'll have to piece that together on your end. Or do what we do, and just show plugs more generically, without specialized styles. | No |
| plugStyle | integer (int32) |  | No |
| plugAvailability | integer (int32) | Indicates the rules about when this plug can be used. See the PlugAvailabilityMode enumeration for more information! | No |
| alternateUiPlugLabel | string | If the plug meets certain state requirements, it may have an alternative label applied to it. This is the alternative label that will be applied in such a situation. | No |
| alternatePlugStyle | integer (int32) | The alternate plug of the plug: only applies when the item is in states that only the server can know about and control, unfortunately. See AlternateUiPlugLabel for the related label info. | No |
| isDummyPlug | boolean | If TRUE, this plug is used for UI display purposes only, and doesn't have any interesting effects of its own. | No |
| parentItemOverride | object | Do you ever get the feeling that a system has become so overburdened by edge cases that it probably should have become some other system entirely? So do I!
In totally unrelated news, Plugs can now override properties of their parent items. This is some of the relevant definition data for those overrides.
If this is populated, it will have the override data to be applied when this plug is applied to an item. | No |
| energyCapacity | object | IF not null, this plug provides Energy capacity to the item in which it is socketed. In Armor 2.0 for example, is implemented in a similar way to Masterworks, where visually it's a single area of the UI being clicked on to "Upgrade" to higher energy levels, but it's actually socketing new plugs. | No |
| energyCost | object | IF not null, this plug has an energy cost. This contains the details of that cost. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyItemPlugDefinition object
const example = {
  insertionRules: [],
  plugCategoryIdentifier: "example value",
  plugCategoryHash: 123,
  onActionRecreateSelf: true,
  insertionMaterialRequirementHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyItemPlugDefinition object
example = {
    "insertionRules": [],
    "plugCategoryIdentifier": "example value",
    "plugCategoryHash": 123,
    "onActionRecreateSelf": True,
    "insertionMaterialRequirementHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyMaterialRequirementSetDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyEnergyCapacityEntry**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyEnergyCostEntry**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyParentItemOverride**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyPlugRuleDefinition**: Referenced in this entity
- **Destiny.PlugAvailabilityMode**: Referenced in this entity
- **Destiny.PlugUiStyles**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyItemPlugDefinition":   {
      "description": "If an item is a Plug, its DestinyInventoryItemDefinition.plug property will be populated with an instance of one of these bad boys.\r\nThis gives information about when it can be inserted, what the plug's category is (and thus whether it is compatible with a socket... see DestinySocketTypeDefinition for information about Plug Categories and socket compatibility), whether it is enabled and other Plug info.",
      "type": "object",
      "properties": {
          "insertionRules": {
              "description": "The rules around when this plug can be inserted into a socket, aside from the socket's individual restrictions.\r\nThe live data DestinyItemPlugComponent.insertFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyPlugRuleDefinition"
              }
          },
          "plugCategoryIdentifier": {
              "description": "The string identifier for the plug's category. Use the socket's DestinySocketTypeDefinition.plugWhitelist to determine whether this plug can be inserted into the socket.",
              "type": "string"
          },
          "plugCategoryHash": {
              "format": "uint32",
              "description": "The hash for the plugCategoryIdentifier. You can use this instead if you wish: I put both in the definition for debugging purposes.",
              "type": "integer"
          },
          "onActionRecreateSelf": {
              "description": "If you successfully socket the item, this will determine whether or not you get \"refunded\" on the plug.",
              "type": "boolean"
          },
          "insertionMaterialRequirementHash": {
              "format": "uint32",
              "description": "If inserting this plug requires materials, this is the hash identifier for looking up the DestinyMaterialRequirementSetDefinition for those requirements.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          },
          "previewItemOverrideHash": {
              "format": "uint32",
              "description": "In the game, if you're inspecting a plug item directly, this will be the item shown with the plug attached. Look up the DestinyInventoryItemDefinition for this hash for the item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "enabledMaterialRequirementHash": {
              "format": "uint32",
              "description": "It's not enough for the plug to be inserted. It has to be enabled as well. For it to be enabled, it may require materials. This is the hash identifier for the DestinyMaterialRequirementSetDefinition for those requirements, if there is one.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          },
          "enabledRules": {
              "description": "The rules around whether the plug, once inserted, is enabled and providing its benefits.\r\nThe live data DestinyItemPlugComponent.enableFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyPlugRuleDefinition"
              }
          },
          "uiPlugLabel": {
              "description": "Plugs can have arbitrary, UI-defined identifiers that the UI designers use to determine the style applied to plugs. Unfortunately, we have neither a definitive list of these labels nor advance warning of when new labels might be applied or how that relates to how they get rendered. If you want to, you can refer to known labels to change your own styles: but know that new ones can be created arbitrarily, and we have no way of associating the labels with any specific UI style guidance... you'll have to piece that together on your end. Or do what we do, and just show plugs more generically, without specialized styles.",
              "type": "string"
          },
          "plugStyle": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.PlugUiStyles"
              }
          },
          "plugAvailability": {
              "format": "int32",
              "description": "Indicates the rules about when this plug can be used. See the PlugAvailabilityMode enumeration for more information!",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.PlugAvailabilityMode"
              }
          },
          "alternateUiPlugLabel": {
              "description": "If the plug meets certain state requirements, it may have an alternative label applied to it. This is the alternative label that will be applied in such a situation.",
              "type": "string"
          },
          "alternatePlugStyle": {
              "format": "int32",
              "description": "The alternate plug of the plug: only applies when the item is in states that only the server can know about and control, unfortunately. See AlternateUiPlugLabel for the related label info.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.PlugUiStyles"
              }
          },
          "isDummyPlug": {
              "description": "If TRUE, this plug is used for UI display purposes only, and doesn't have any interesting effects of its own.",
              "type": "boolean"
          },
          "parentItemOverride": {
              "description": "Do you ever get the feeling that a system has become so overburdened by edge cases that it probably should have become some other system entirely? So do I!\r\nIn totally unrelated news, Plugs can now override properties of their parent items. This is some of the relevant definition data for those overrides.\r\nIf this is populated, it will have the override data to be applied when this plug is applied to an item.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Items.DestinyParentItemOverride"
                  }
              ]
          },
          "energyCapacity": {
              "description": "IF not null, this plug provides Energy capacity to the item in which it is socketed. In Armor 2.0 for example, is implemented in a similar way to Masterworks, where visually it's a single area of the UI being clicked on to \"Upgrade\" to higher energy levels, but it's actually socketing new plugs.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Items.DestinyEnergyCapacityEntry"
                  }
              ]
          },
          "energyCost": {
              "description": "IF not null, this plug has an energy cost. This contains the details of that cost.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Items.DestinyEnergyCostEntry"
                  }
              ]
          }
      }
  }
}
```
