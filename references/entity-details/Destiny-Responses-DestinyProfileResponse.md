# Destiny.Responses.DestinyProfileResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyProfileResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The response for GetDestinyProfile, with components for character and item-level data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| responseMintedTimestamp | string (date-time) | Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness. | No |
| secondaryComponentsMintedTimestamp | string (date-time) | Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:
 PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory
 All other component types may use the primary timestamp property. | No |
| vendorReceipts | object | Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say...
COMPONENT TYPE: VendorReceipts | No |
| profileInventory | object | The profile-level inventory of the Destiny Profile.
COMPONENT TYPE: ProfileInventories | No |
| profileCurrencies | object | The profile-level currencies owned by the Destiny Profile.
COMPONENT TYPE: ProfileCurrencies | No |
| profile | object | The basic information about the Destiny Profile (formerly "Account").
COMPONENT TYPE: Profiles | No |
| platformSilver | object | Silver quantities for any platform on which this Profile plays destiny.
 COMPONENT TYPE: PlatformSilver | No |
| profileKiosks | object | Items available from Kiosks that are available Profile-wide (i.e. across all characters)
This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.
COMPONENT TYPE: Kiosks | No |
| profilePlugSets | object | When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped.
This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.
COMPONENT TYPE: ItemSockets | No |
| profileProgression | object | When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data.
COMPONENT TYPE: ProfileProgression | No |
| profilePresentationNodes | object | COMPONENT TYPE: PresentationNodes | No |
| profileRecords | object | COMPONENT TYPE: Records | No |
| profileCollectibles | object | COMPONENT TYPE: Collectibles | No |
| profileTransitoryData | object | COMPONENT TYPE: Transitory | No |
| metrics | object | COMPONENT TYPE: Metrics | No |
| profileStringVariables | object | COMPONENT TYPE: StringVariables | No |
| profileCommendations | object | COMPONENT TYPE: SocialCommendations | No |
| characters | object | Basic information about each character, keyed by the CharacterId.
COMPONENT TYPE: Characters | No |
| characterInventories | object | The character-level non-equipped inventory items, keyed by the Character's Id.
COMPONENT TYPE: CharacterInventories | No |
| characterLoadouts | object | The character loadouts, keyed by the Character's Id.
COMPONENT TYPE: CharacterLoadouts | No |
| characterProgressions | object | Character-level progression data, keyed by the Character's Id.
COMPONENT TYPE: CharacterProgressions | No |
| characterRenderData | object | Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id.
COMPONENT TYPE: CharacterRenderData | No |
| characterActivities | object | Character activity data - the activities available to this character and its status, keyed by the Character's Id.
COMPONENT TYPE: CharacterActivities | No |
| characterEquipment | object | The character's equipped items, keyed by the Character's Id.
COMPONENT TYPE: CharacterEquipment | No |
| characterKiosks | object | Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk.
This component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.
COMPONENT TYPE: Kiosks | No |
| characterPlugSets | object | When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped.
This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.
COMPONENT TYPE: ItemSockets | No |
| characterUninstancedItemComponents | object | Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface?
Let's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise.
At some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character.
Up to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus "itemComponents" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside.
Unfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character.
To give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory.
I'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay | No |
| characterPresentationNodes | object | COMPONENT TYPE: PresentationNodes | No |
| characterRecords | object | COMPONENT TYPE: Records | No |
| characterCollectibles | object | COMPONENT TYPE: Collectibles | No |
| characterStringVariables | object | COMPONENT TYPE: StringVariables | No |
| characterCraftables | object | COMPONENT TYPE: Craftables | No |
| itemComponents | object | Information about instanced items across all returned characters, keyed by the item's instance ID.
COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.] | No |
| characterCurrencyLookups | object | A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
COMPONENT TYPE: CurrencyLookups | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyProfileResponse object
const example = {
  responseMintedTimestamp: "example value",
  secondaryComponentsMintedTimestamp: "example value",
  vendorReceipts: null,
  profileInventory: null,
  profileCurrencies: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Responses.DestinyProfileResponse object
example = {
    "responseMintedTimestamp": "example value",
    "secondaryComponentsMintedTimestamp": "example value",
    "vendorReceipts": None,
    "profileInventory": None,
    "profileCurrencies": None,
    # ... more properties
}
```

## Related Entities
- **DestinyBaseItemComponentSetOfuint32**: Referenced in this entity
- **DestinyItemComponentSetOfint64**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCharacterComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCraftablesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyInventoryComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyKiosksComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyInventoryComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyKiosksComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyMetricsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyPlatformSilverComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyPlugSetsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyPresentationNodesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyProfileCollectiblesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyProfileComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyProfileProgressionComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyProfileRecordsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyProfileTransitoryComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinySocialCommendationsComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyStringVariablesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyVendorReceiptsComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyProfileResponse":   {
      "description": "The response for GetDestinyProfile, with components for character and item-level data.",
      "type": "object",
      "properties": {
          "responseMintedTimestamp": {
              "format": "date-time",
              "description": "Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness.",
              "type": "string"
          },
          "secondaryComponentsMintedTimestamp": {
              "format": "date-time",
              "description": "Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:\r\n PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory\r\n All other component types may use the primary timestamp property.",
              "type": "string"
          },
          "vendorReceipts": {
              "description": "Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say...\r\nCOMPONENT TYPE: VendorReceipts",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyVendorReceiptsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "VendorReceipts"
          },
          "profileInventory": {
              "description": "The profile-level inventory of the Destiny Profile.\r\nCOMPONENT TYPE: ProfileInventories",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyInventoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ProfileInventories"
          },
          "profileCurrencies": {
              "description": "The profile-level currencies owned by the Destiny Profile.\r\nCOMPONENT TYPE: ProfileCurrencies",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyInventoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ProfileCurrencies"
          },
          "profile": {
              "description": "The basic information about the Destiny Profile (formerly \"Account\").\r\nCOMPONENT TYPE: Profiles",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyProfileComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Profiles"
          },
          "platformSilver": {
              "description": "Silver quantities for any platform on which this Profile plays destiny.\r\n COMPONENT TYPE: PlatformSilver",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyPlatformSilverComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "PlatformSilver"
          },
          "profileKiosks": {
              "description": "Items available from Kiosks that are available Profile-wide (i.e. across all characters)\r\nThis component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.\r\nCOMPONENT TYPE: Kiosks",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyKiosksComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Kiosks"
          },
          "profilePlugSets": {
              "description": "When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped.\r\nThis comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.\r\nCOMPONENT TYPE: ItemSockets",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyPlugSetsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemSockets"
          },
          "profileProgression": {
              "description": "When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data.\r\nCOMPONENT TYPE: ProfileProgression",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyProfileProgressionComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ProfileProgression"
          },
          "profilePresentationNodes": {
              "description": "COMPONENT TYPE: PresentationNodes",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyPresentationNodesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "PresentationNodes"
          },
          "profileRecords": {
              "description": "COMPONENT TYPE: Records",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyProfileRecordsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Records"
          },
          "profileCollectibles": {
              "description": "COMPONENT TYPE: Collectibles",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyProfileCollectiblesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Collectibles"
          },
          "profileTransitoryData": {
              "description": "COMPONENT TYPE: Transitory",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyProfileTransitoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Transitory"
          },
          "metrics": {
              "description": "COMPONENT TYPE: Metrics",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyMetricsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Metrics"
          },
          "profileStringVariables": {
              "description": "COMPONENT TYPE: StringVariables",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyStringVariablesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "StringVariables"
          },
          "profileCommendations": {
              "description": "COMPONENT TYPE: SocialCommendations",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinySocialCommendationsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "SocialCommendations"
          },
          "characters": {
              "description": "Basic information about each character, keyed by the CharacterId.\r\nCOMPONENT TYPE: Characters",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCharacterComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Characters"
          },
          "characterInventories": {
              "description": "The character-level non-equipped inventory items, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterInventories",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyInventoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterInventories"
          },
          "characterLoadouts": {
              "description": "The character loadouts, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterLoadouts",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterLoadouts"
          },
          "characterProgressions": {
              "description": "Character-level progression data, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterProgressions",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterProgressions"
          },
          "characterRenderData": {
              "description": "Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterRenderData",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterRenderData"
          },
          "characterActivities": {
              "description": "Character activity data - the activities available to this character and its status, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterActivities",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterActivities"
          },
          "characterEquipment": {
              "description": "The character's equipped items, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterEquipment",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyInventoryComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CharacterEquipment"
          },
          "characterKiosks": {
              "description": "Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk.\r\nThis component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.\r\nCOMPONENT TYPE: Kiosks",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyKiosksComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Kiosks"
          },
          "characterPlugSets": {
              "description": "When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped.\r\nThis comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.\r\nCOMPONENT TYPE: ItemSockets",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "ItemSockets"
          },
          "characterUninstancedItemComponents": {
              "description": "Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface?\r\nLet's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise.\r\nAt some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character.\r\nUp to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus \"itemComponents\" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside.\r\nUnfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character.\r\nTo give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory.\r\nI'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/DestinyBaseItemComponentSetOfuint32"
              }
          },
          "characterPresentationNodes": {
              "description": "COMPONENT TYPE: PresentationNodes",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "PresentationNodes"
          },
          "characterRecords": {
              "description": "COMPONENT TYPE: Records",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Records"
          },
          "characterCollectibles": {
              "description": "COMPONENT TYPE: Collectibles",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Collectibles"
          },
          "characterStringVariables": {
              "description": "COMPONENT TYPE: StringVariables",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "StringVariables"
          },
          "characterCraftables": {
              "description": "COMPONENT TYPE: Craftables",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCraftablesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Craftables"
          },
          "itemComponents": {
              "description": "Information about instanced items across all returned characters, keyed by the item's instance ID.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DestinyItemComponentSetOfint64"
                  }
              ]
          },
          "characterCurrencyLookups": {
              "description": "A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.\r\nCOMPONENT TYPE: CurrencyLookups",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CurrencyLookups"
          }
      }
  }
}
```
