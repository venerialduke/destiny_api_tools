# Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutconstantsdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| whiteIconImagePath | string | This is the same icon as the one in the display properties, offered here as well with a more descriptive name. | No |
| blackIconImagePath | string | This is a color-inverted version of the whiteIconImagePath. | No |
| loadoutCountPerCharacter | integer (int32) | The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks. | No |
| loadoutPreviewFilterOutSocketCategoryHashes | Array[integer] | A list of the socket category hashes to be filtered out of loadout item preview displays. | No |
| loadoutPreviewFilterOutSocketTypeHashes | Array[integer] | A list of the socket type hashes to be filtered out of loadout item preview displays. | No |
| loadoutNameHashes | Array[integer] | A list of the loadout name hashes in index order, for convenience. | No |
| loadoutIconHashes | Array[integer] | A list of the loadout icon hashes in index order, for convenience. | No |
| loadoutColorHashes | Array[integer] | A list of the loadout color hashes in index order, for convenience. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition object
const example = {
  displayProperties: null,
  whiteIconImagePath: "example value",
  blackIconImagePath: "example value",
  loadoutCountPerCharacter: 123,
  loadoutPreviewFilterOutSocketCategoryHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition object
example = {
    "displayProperties": None,
    "whiteIconImagePath": "example value",
    "blackIconImagePath": "example value",
    "loadoutCountPerCharacter": 123,
    "loadoutPreviewFilterOutSocketCategoryHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutColorDefinition**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutIconDefinition**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketCategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "whiteIconImagePath": {
              "description": "This is the same icon as the one in the display properties, offered here as well with a more descriptive name.",
              "type": "string"
          },
          "blackIconImagePath": {
              "description": "This is a color-inverted version of the whiteIconImagePath.",
              "type": "string"
          },
          "loadoutCountPerCharacter": {
              "format": "int32",
              "description": "The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks.",
              "type": "integer"
          },
          "loadoutPreviewFilterOutSocketCategoryHashes": {
              "description": "A list of the socket category hashes to be filtered out of loadout item preview displays.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketCategoryDefinition"
              }
          },
          "loadoutPreviewFilterOutSocketTypeHashes": {
              "description": "A list of the socket type hashes to be filtered out of loadout item preview displays.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          },
          "loadoutNameHashes": {
              "description": "A list of the loadout name hashes in index order, for convenience.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutNameDefinition"
              }
          },
          "loadoutIconHashes": {
              "description": "A list of the loadout icon hashes in index order, for convenience.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutIconDefinition"
              }
          },
          "loadoutColorHashes": {
              "description": "A list of the loadout color hashes in index order, for convenience.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutColorDefinition"
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
      "x-mobile-manifest-name": "LoadoutConstants"
  }
}
```
