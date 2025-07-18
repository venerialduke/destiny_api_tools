# Common.Models.Destiny2CoreSettings

## Entity Information
- **Entity Name**: Common.Models.Destiny2CoreSettings
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destiny2coresettings data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| collectionRootNode | integer (uint32) |  | No |
| badgesRootNode | integer (uint32) |  | No |
| recordsRootNode | integer (uint32) |  | No |
| medalsRootNode | integer (uint32) |  | No |
| metricsRootNode | integer (uint32) |  | No |
| activeTriumphsRootNodeHash | integer (uint32) |  | No |
| activeSealsRootNodeHash | integer (uint32) |  | No |
| legacyTriumphsRootNodeHash | integer (uint32) |  | No |
| legacySealsRootNodeHash | integer (uint32) |  | No |
| medalsRootNodeHash | integer (uint32) |  | No |
| exoticCatalystsRootNodeHash | integer (uint32) |  | No |
| loreRootNodeHash | integer (uint32) |  | No |
| craftingRootNodeHash | integer (uint32) |  | No |
| loadoutConstantsHash | integer (uint32) |  | No |
| guardianRankConstantsHash | integer (uint32) |  | No |
| fireteamFinderConstantsHash | integer (uint32) |  | No |
| inventoryItemConstantsHash | integer (uint32) |  | No |
| featuredItemsListHash | integer (uint32) |  | No |
| armorArchetypePlugSetHash | integer (uint32) |  | No |
| seasonalHubEventCardHash | integer (uint32) |  | No |
| guardianRanksRootNodeHash | integer (uint32) |  | No |
| currentRankProgressionHashes | Array[integer] |  | No |
| insertPlugFreeProtectedPlugItemHashes | Array[integer] |  | No |
| insertPlugFreeBlockedSocketTypeHashes | Array[integer] |  | No |
| enabledFireteamFinderActivityGraphHashes | Array[integer] |  | No |
| undiscoveredCollectibleImage | string |  | No |
| ammoTypeHeavyIcon | string |  | No |
| ammoTypeSpecialIcon | string |  | No |
| ammoTypePrimaryIcon | string |  | No |
| currentSeasonalArtifactHash | integer (uint32) |  | No |
| currentSeasonHash | integer (uint32) |  | No |
| seasonalChallengesPresentationNodeHash | integer (uint32) |  | No |
| futureSeasonHashes | Array[integer] |  | No |
| pastSeasonHashes | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Common.Models.Destiny2CoreSettings object
const example = {
  collectionRootNode: 123,
  badgesRootNode: 123,
  recordsRootNode: 123,
  medalsRootNode: 123,
  metricsRootNode: 123,
  // ... more properties
};
```

### Python
```python
# Example Common.Models.Destiny2CoreSettings object
example = {
    "collectionRootNode": 123,
    "badgesRootNode": 123,
    "recordsRootNode": 123,
    "medalsRootNode": 123,
    "metricsRootNode": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition**: Referenced in this entity
- **Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition**: Referenced in this entity
- **Destiny.Definitions.Inventory.DestinyItemFilterDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyInventoryItemConstantsDefinition**: Referenced in this entity
- **Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinyEventCardDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinyPlugSetDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Common.Models.Destiny2CoreSettings":   {
      "type": "object",
      "properties": {
          "collectionRootNode": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "badgesRootNode": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "recordsRootNode": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "medalsRootNode": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "metricsRootNode": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "activeTriumphsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "activeSealsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "legacyTriumphsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "legacySealsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "medalsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "exoticCatalystsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "loreRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "craftingRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "loadoutConstantsHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Loadouts.DestinyLoadoutConstantsDefinition"
              }
          },
          "guardianRankConstantsHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition"
              }
          },
          "fireteamFinderConstantsHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition"
              }
          },
          "inventoryItemConstantsHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyInventoryItemConstantsDefinition"
              }
          },
          "featuredItemsListHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Inventory.DestinyItemFilterDefinition"
              }
          },
          "armorArchetypePlugSetHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyPlugSetDefinition"
              }
          },
          "seasonalHubEventCardHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinyEventCardDefinition"
              }
          },
          "guardianRanksRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "currentRankProgressionHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "insertPlugFreeProtectedPlugItemHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "insertPlugFreeBlockedSocketTypeHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          },
          "enabledFireteamFinderActivityGraphHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "undiscoveredCollectibleImage": {
              "type": "string"
          },
          "ammoTypeHeavyIcon": {
              "type": "string"
          },
          "ammoTypeSpecialIcon": {
              "type": "string"
          },
          "ammoTypePrimaryIcon": {
              "type": "string"
          },
          "currentSeasonalArtifactHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "currentSeasonHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonDefinition"
              }
          },
          "seasonalChallengesPresentationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "futureSeasonHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonDefinition"
              }
          },
          "pastSeasonHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonDefinition"
              }
          }
      }
  }
}
```
