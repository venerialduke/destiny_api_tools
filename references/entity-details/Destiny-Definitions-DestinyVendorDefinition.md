# Destiny.Definitions.DestinyVendorDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
These are the definitions for Vendors.
In Destiny, a Vendor can be a lot of things - some things that you wouldn't expect, and some things that you don't even see directly in the game. Vendors are the Dolly Levi of the Destiny universe.
- Traditional Vendors as you see in game: people who you come up to and who give you quests, rewards, or who you can buy things from.
- Kiosks/Collections, which are really just Vendors that don't charge currency (or charge some pittance of a currency) and whose gating for purchases revolves more around your character's state.
- Previews for rewards or the contents of sacks. These are implemented as Vendors, where you can't actually purchase from them but the items that they have for sale and the categories of sale items reflect the rewards or contents of the sack. This is so that the game could reuse the existing Vendor display UI for rewards and save a bunch of wheel reinvention.
- Item Transfer capabilities, like the Vault and Postmaster. Vendors can have "acceptedItem" buckets that determine the source and destination buckets for transfers. When you interact with such a vendor, these buckets are what gets shown in the UI instead of any items that the Vendor would have for sale. Yep, the Vault is a vendor.
It is pretty much guaranteed that they'll be used for even more features in the future. They have come to be seen more as generic categorized containers for items than "vendors" in a traditional sense, for better or worse.
Where possible and time allows, we'll attempt to split those out into their own more digestible derived "Definitions": but often time does not allow that, as you can see from the above ways that vendors are used which we never split off from Vendor Definitions externally.
Since Vendors are so many things to so many parts of the game, the definition is understandably complex. You will want to combine this data with live Vendor information from the API when it is available.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition |  | No |
| vendorProgressionType | integer (int32) | The type of reward progression that this vendor has. Default - The original rank progression from token redemption. Ritual - Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Battlegrounds (War Table). | No |
| buyString | string | If the vendor has a custom localized string describing the "buy" action, that is returned here. | No |
| sellString | string | Ditto for selling. Not that you can sell items to a vendor anymore. Will it come back? Who knows. The string's still there. | No |
| displayItemHash | integer (uint32) | If the vendor has an item that should be displayed as the "featured" item, this is the hash identifier for that DestinyVendorItemDefinition.
Apparently this is usually a related currency, like a reputation token. But it need not be restricted to that. | No |
| inhibitBuying | boolean | If this is true, you aren't allowed to buy whatever the vendor is selling. | No |
| inhibitSelling | boolean | If this is true, you're not allowed to sell whatever the vendor is buying. | No |
| factionHash | integer (uint32) | If the Vendor has a faction, this hash will be valid and point to a DestinyFactionDefinition.
The game UI and BNet often mine the faction definition for additional elements and details to place on the screen, such as the faction's Progression status (aka "Reputation"). | No |
| resetIntervalMinutes | integer (int32) | A number used for calculating the frequency of a vendor's inventory resetting/refreshing.
Don't worry about calculating this - we do it on the server side and send you the next refresh date with the live data. | No |
| resetOffsetMinutes | integer (int32) | Again, used for reset/refreshing of inventory. Don't worry too much about it. Unless you want to. | No |
| failureStrings | Array[string] | If an item can't be purchased from the vendor, there may be many "custom"/game state specific reasons why not.
This is a list of localized strings with messages for those custom failures. The live BNet data will return a failureIndexes property for items that can't be purchased: using those values to index into this array, you can show the user the appropriate failure message for the item that can't be bought. | No |
| unlockRanges | Array[Dates.DateRange] | If we were able to predict the dates when this Vendor will be visible/available, this will be the list of those date ranges. Sadly, we're not able to predict this very frequently, so this will often be useless data. | No |
| vendorIdentifier | string | The internal identifier for the Vendor. A holdover from the old days of Vendors, but we don't have time to refactor it away. | No |
| vendorPortrait | string | A portrait of the Vendor's smiling mug. Or frothing tentacles. | No |
| vendorBanner | string | If the vendor has a custom banner image, that can be found here. | No |
| enabled | boolean | If a vendor is not enabled, we won't even save the vendor's definition, and we won't return any items or info about them. It's as if they don't exist. | No |
| visible | boolean | If a vendor is not visible, we still have and will give vendor definition info, but we won't use them for things like Advisors or UI. | No |
| vendorSubcategoryIdentifier | string | The identifier of the VendorCategoryDefinition for this vendor's subcategory. | No |
| consolidateCategories | boolean | If TRUE, consolidate categories that only differ by trivial properties (such as having minor differences in name) | No |
| actions | Array[Destiny.Definitions.DestinyVendorActionDefinition] | Describes "actions" that can be performed on a vendor. Currently, none of these exist. But theoretically a Vendor could let you interact with it by performing actions. We'll see what these end up looking like if they ever get used. | No |
| categories | Array[Destiny.Definitions.DestinyVendorCategoryEntryDefinition] | These are the headers for sections of items that the vendor is selling. When you see items organized by category in the header, it is these categories that it is showing.
Well, technically not *exactly* these. On BNet, it doesn't make sense to have categories be "paged" as we do in Destiny, so we run some heuristics to attempt to aggregate pages of categories together. 
These are the categories post-concatenation, if the vendor had concatenation applied. If you want the pre-aggregated category data, use originalCategories. | No |
| originalCategories | Array[Destiny.Definitions.DestinyVendorCategoryEntryDefinition] | See the categories property for a description of categories and why originalCategories exists. | No |
| displayCategories | Array[Destiny.Definitions.DestinyDisplayCategoryDefinition] | Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI. 
The "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two. | No |
| interactions | Array[Destiny.Definitions.DestinyVendorInteractionDefinition] | In addition to selling items, vendors can have "interactions": UI where you "talk" with the vendor and they offer you a reward, some item, or merely acknowledge via dialog that you did something cool. | No |
| inventoryFlyouts | Array[Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition] | If the vendor shows you items from your own inventory - such as the Vault vendor does - this data describes the UI around showing those inventory buckets and which ones get shown. | No |
| itemList | Array[Destiny.Definitions.DestinyVendorItemDefinition] | If the vendor sells items (or merely has a list of items to show like the "Sack" vendors do), this is the list of those items that the vendor can sell. From this list, only a subset will be available from the vendor at any given time, selected randomly and reset on the vendor's refresh interval.
Note that a vendor can sell the same item multiple ways: for instance, nothing stops a vendor from selling you some specific weapon but using two different currencies, or the same weapon at multiple "item levels". | No |
| services | Array[Destiny.Definitions.DestinyVendorServiceDefinition] | BNet doesn't use this data yet, but it appears to be an optional list of flavor text about services that the Vendor can provide. | No |
| acceptedItems | Array[Destiny.Definitions.DestinyVendorAcceptedItemDefinition] | If the Vendor is actually a vehicle for the transferring of items (like the Vault and Postmaster vendors), this defines the list of source->destination buckets for transferring. | No |
| returnWithVendorRequest | boolean | As many of you know, Vendor data has historically been pretty brutal on the BNet servers. In an effort to reduce this workload, only Vendors with this flag set will be returned on Vendor requests. This allows us to filter out Vendors that don't dynamic data that's particularly useful: things like "Preview/Sack" vendors, for example, that you can usually suss out the details for using just the definitions themselves. | No |
| locations | Array[Destiny.Definitions.Vendors.DestinyVendorLocationDefinition] | A vendor can be at different places in the world depending on the game/character/account state. This is the list of possible locations for the vendor, along with conditions we use to determine which one is currently active. | No |
| groups | Array[Destiny.Definitions.DestinyVendorGroupReference] | A vendor can be a part of 0 or 1 "groups" at a time: a group being a collection of Vendors related by either location or function/purpose. It's used for our our Companion Vendor UI. Only one of these can be active for a Vendor at a time. | No |
| ignoreSaleItemHashes | Array[integer] | Some items don't make sense to return in the API, for example because they represent an action to be performed rather than an item being sold. I'd rather we not do this, but at least in the short term this is a workable workaround. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorDefinition object
const example = {
  displayProperties: null,
  vendorProgressionType: 123,
  buyString: "example value",
  sellString: "example value",
  displayItemHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorDefinition object
example = {
    "displayProperties": None,
    "vendorProgressionType": 123,
    "buyString": "example value",
    "sellString": "example value",
    "displayItemHash": 123,
    # ... more properties
}
```

## Related Entities
- **Dates.DateRange**: Referenced in this entity
- **Destiny.Definitions.DestinyDisplayCategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyFactionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorAcceptedItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorActionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorCategoryEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorGroupReference**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorInteractionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorServiceDefinition**: Referenced in this entity
- **Destiny.Definitions.Vendors.DestinyVendorLocationDefinition**: Referenced in this entity
- **Destiny.DestinyVendorProgressionType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorDefinition":   {
      "description": "These are the definitions for Vendors.\r\nIn Destiny, a Vendor can be a lot of things - some things that you wouldn't expect, and some things that you don't even see directly in the game. Vendors are the Dolly Levi of the Destiny universe.\r\n- Traditional Vendors as you see in game: people who you come up to and who give you quests, rewards, or who you can buy things from.\r\n- Kiosks/Collections, which are really just Vendors that don't charge currency (or charge some pittance of a currency) and whose gating for purchases revolves more around your character's state.\r\n- Previews for rewards or the contents of sacks. These are implemented as Vendors, where you can't actually purchase from them but the items that they have for sale and the categories of sale items reflect the rewards or contents of the sack. This is so that the game could reuse the existing Vendor display UI for rewards and save a bunch of wheel reinvention.\r\n- Item Transfer capabilities, like the Vault and Postmaster. Vendors can have \"acceptedItem\" buckets that determine the source and destination buckets for transfers. When you interact with such a vendor, these buckets are what gets shown in the UI instead of any items that the Vendor would have for sale. Yep, the Vault is a vendor.\r\nIt is pretty much guaranteed that they'll be used for even more features in the future. They have come to be seen more as generic categorized containers for items than \"vendors\" in a traditional sense, for better or worse.\r\nWhere possible and time allows, we'll attempt to split those out into their own more digestible derived \"Definitions\": but often time does not allow that, as you can see from the above ways that vendors are used which we never split off from Vendor Definitions externally.\r\nSince Vendors are so many things to so many parts of the game, the definition is understandably complex. You will want to combine this data with live Vendor information from the API when it is available.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition"
          },
          "vendorProgressionType": {
              "format": "int32",
              "description": "The type of reward progression that this vendor has. Default - The original rank progression from token redemption. Ritual - Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Battlegrounds (War Table).",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyVendorProgressionType"
              }
          },
          "buyString": {
              "description": "If the vendor has a custom localized string describing the \"buy\" action, that is returned here.",
              "type": "string"
          },
          "sellString": {
              "description": "Ditto for selling. Not that you can sell items to a vendor anymore. Will it come back? Who knows. The string's still there.",
              "type": "string"
          },
          "displayItemHash": {
              "format": "uint32",
              "description": "If the vendor has an item that should be displayed as the \"featured\" item, this is the hash identifier for that DestinyVendorItemDefinition.\r\nApparently this is usually a related currency, like a reputation token. But it need not be restricted to that.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "inhibitBuying": {
              "description": "If this is true, you aren't allowed to buy whatever the vendor is selling.",
              "type": "boolean"
          },
          "inhibitSelling": {
              "description": "If this is true, you're not allowed to sell whatever the vendor is buying.",
              "type": "boolean"
          },
          "factionHash": {
              "format": "uint32",
              "description": "If the Vendor has a faction, this hash will be valid and point to a DestinyFactionDefinition.\r\nThe game UI and BNet often mine the faction definition for additional elements and details to place on the screen, such as the faction's Progression status (aka \"Reputation\").",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyFactionDefinition"
              }
          },
          "resetIntervalMinutes": {
              "format": "int32",
              "description": "A number used for calculating the frequency of a vendor's inventory resetting/refreshing.\r\nDon't worry about calculating this - we do it on the server side and send you the next refresh date with the live data.",
              "type": "integer"
          },
          "resetOffsetMinutes": {
              "format": "int32",
              "description": "Again, used for reset/refreshing of inventory. Don't worry too much about it. Unless you want to.",
              "type": "integer"
          },
          "failureStrings": {
              "description": "If an item can't be purchased from the vendor, there may be many \"custom\"/game state specific reasons why not.\r\nThis is a list of localized strings with messages for those custom failures. The live BNet data will return a failureIndexes property for items that can't be purchased: using those values to index into this array, you can show the user the appropriate failure message for the item that can't be bought.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "unlockRanges": {
              "description": "If we were able to predict the dates when this Vendor will be visible/available, this will be the list of those date ranges. Sadly, we're not able to predict this very frequently, so this will often be useless data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Dates.DateRange"
              }
          },
          "vendorIdentifier": {
              "description": "The internal identifier for the Vendor. A holdover from the old days of Vendors, but we don't have time to refactor it away.",
              "type": "string"
          },
          "vendorPortrait": {
              "description": "A portrait of the Vendor's smiling mug. Or frothing tentacles.",
              "type": "string"
          },
          "vendorBanner": {
              "description": "If the vendor has a custom banner image, that can be found here.",
              "type": "string"
          },
          "enabled": {
              "description": "If a vendor is not enabled, we won't even save the vendor's definition, and we won't return any items or info about them. It's as if they don't exist.",
              "type": "boolean"
          },
          "visible": {
              "description": "If a vendor is not visible, we still have and will give vendor definition info, but we won't use them for things like Advisors or UI.",
              "type": "boolean"
          },
          "vendorSubcategoryIdentifier": {
              "description": "The identifier of the VendorCategoryDefinition for this vendor's subcategory.",
              "type": "string"
          },
          "consolidateCategories": {
              "description": "If TRUE, consolidate categories that only differ by trivial properties (such as having minor differences in name)",
              "type": "boolean"
          },
          "actions": {
              "description": "Describes \"actions\" that can be performed on a vendor. Currently, none of these exist. But theoretically a Vendor could let you interact with it by performing actions. We'll see what these end up looking like if they ever get used.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorActionDefinition"
              }
          },
          "categories": {
              "description": "These are the headers for sections of items that the vendor is selling. When you see items organized by category in the header, it is these categories that it is showing.\r\nWell, technically not *exactly* these. On BNet, it doesn't make sense to have categories be \"paged\" as we do in Destiny, so we run some heuristics to attempt to aggregate pages of categories together. \r\nThese are the categories post-concatenation, if the vendor had concatenation applied. If you want the pre-aggregated category data, use originalCategories.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorCategoryEntryDefinition"
              }
          },
          "originalCategories": {
              "description": "See the categories property for a description of categories and why originalCategories exists.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorCategoryEntryDefinition"
              }
          },
          "displayCategories": {
              "description": "Display Categories are different from \"categories\" in that these are specifically for visual grouping and display of categories in Vendor UI. \r\nThe \"categories\" structure is for validation of the contained items, and can be categorized entirely separately from \"Display Categories\", there need be and often will be no meaningful relationship between the two.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDisplayCategoryDefinition"
              }
          },
          "interactions": {
              "description": "In addition to selling items, vendors can have \"interactions\": UI where you \"talk\" with the vendor and they offer you a reward, some item, or merely acknowledge via dialog that you did something cool.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorInteractionDefinition"
              }
          },
          "inventoryFlyouts": {
              "description": "If the vendor shows you items from your own inventory - such as the Vault vendor does - this data describes the UI around showing those inventory buckets and which ones get shown.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorInventoryFlyoutDefinition"
              }
          },
          "itemList": {
              "description": "If the vendor sells items (or merely has a list of items to show like the \"Sack\" vendors do), this is the list of those items that the vendor can sell. From this list, only a subset will be available from the vendor at any given time, selected randomly and reset on the vendor's refresh interval.\r\nNote that a vendor can sell the same item multiple ways: for instance, nothing stops a vendor from selling you some specific weapon but using two different currencies, or the same weapon at multiple \"item levels\".",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorItemDefinition"
              }
          },
          "services": {
              "description": "BNet doesn't use this data yet, but it appears to be an optional list of flavor text about services that the Vendor can provide.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorServiceDefinition"
              }
          },
          "acceptedItems": {
              "description": "If the Vendor is actually a vehicle for the transferring of items (like the Vault and Postmaster vendors), this defines the list of source->destination buckets for transferring.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorAcceptedItemDefinition"
              }
          },
          "returnWithVendorRequest": {
              "description": "As many of you know, Vendor data has historically been pretty brutal on the BNet servers. In an effort to reduce this workload, only Vendors with this flag set will be returned on Vendor requests. This allows us to filter out Vendors that don't dynamic data that's particularly useful: things like \"Preview/Sack\" vendors, for example, that you can usually suss out the details for using just the definitions themselves.",
              "type": "boolean"
          },
          "locations": {
              "description": "A vendor can be at different places in the world depending on the game/character/account state. This is the list of possible locations for the vendor, along with conditions we use to determine which one is currently active.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Vendors.DestinyVendorLocationDefinition"
              }
          },
          "groups": {
              "description": "A vendor can be a part of 0 or 1 \"groups\" at a time: a group being a collection of Vendors related by either location or function/purpose. It's used for our our Companion Vendor UI. Only one of these can be active for a Vendor at a time.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorGroupReference"
              }
          },
          "ignoreSaleItemHashes": {
              "description": "Some items don't make sense to return in the API, for example because they represent an action to be performed rather than an item being sold. I'd rather we not do this, but at least in the short term this is a workable workaround.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
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
      "x-mobile-manifest-name": "Vendors"
  }
}
```
