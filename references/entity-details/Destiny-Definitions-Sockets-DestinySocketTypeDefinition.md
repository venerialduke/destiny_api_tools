# Destiny.Definitions.Sockets.DestinySocketTypeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Sockets.DestinySocketTypeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
All Sockets have a "Type": a set of common properties that determine when the socket allows Plugs to be inserted, what Categories of Plugs can be inserted, and whether the socket is even visible at all given the current game/character/account state.
See DestinyInventoryItemDefinition for more information about Socketed items and Plugs.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful. | No |
| insertAction | object | Defines what happens when a plug is inserted into sockets of this type. | No |
| plugWhitelist | Array[Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition] | A list of Plug "Categories" that are allowed to be plugged into sockets of this type.
These should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.
If the plug's category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted. | No |
| socketCategoryHash | integer (uint32) |  | No |
| visibility | integer (int32) | Sometimes a socket isn't visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled. | No |
| alwaysRandomizeSockets | boolean |  | No |
| isPreviewEnabled | boolean |  | No |
| hideDuplicateReusablePlugs | boolean |  | No |
| overridesUiAppearance | boolean | This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item's icon and nameplate. | No |
| avoidDuplicatesOnInitialization | boolean |  | No |
| currencyScalars | Array[Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry] |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sockets.DestinySocketTypeDefinition object
const example = {
  displayProperties: null,
  insertAction: null,
  plugWhitelist: [],
  socketCategoryHash: 123,
  visibility: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Sockets.DestinySocketTypeDefinition object
example = {
    "displayProperties": None,
    "insertAction": None,
    "plugWhitelist": [],
    "socketCategoryHash": 123,
    "visibility": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketCategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry**: Referenced in this entity
- **Destiny.DestinySocketVisibility**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Sockets.DestinySocketTypeDefinition":   {
      "description": "All Sockets have a \"Type\": a set of common properties that determine when the socket allows Plugs to be inserted, what Categories of Plugs can be inserted, and whether the socket is even visible at all given the current game/character/account state.\r\nSee DestinyInventoryItemDefinition for more information about Socketed items and Plugs.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "insertAction": {
              "description": "Defines what happens when a plug is inserted into sockets of this type.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition"
                  }
              ]
          },
          "plugWhitelist": {
              "description": "A list of Plug \"Categories\" that are allowed to be plugged into sockets of this type.\r\nThese should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.\r\nIf the plug's category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition"
              }
          },
          "socketCategoryHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketCategoryDefinition"
              }
          },
          "visibility": {
              "format": "int32",
              "description": "Sometimes a socket isn't visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinySocketVisibility"
              }
          },
          "alwaysRandomizeSockets": {
              "type": "boolean"
          },
          "isPreviewEnabled": {
              "type": "boolean"
          },
          "hideDuplicateReusablePlugs": {
              "type": "boolean"
          },
          "overridesUiAppearance": {
              "description": "This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item's icon and nameplate.",
              "type": "boolean"
          },
          "avoidDuplicatesOnInitialization": {
              "type": "boolean"
          },
          "currencyScalars": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeScalarMaterialRequirementEntry"
              }
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "SocketTypes"
  }
}
```
