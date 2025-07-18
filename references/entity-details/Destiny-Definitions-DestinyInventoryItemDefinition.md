# Destiny.Definitions.DestinyInventoryItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyInventoryItemDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
So much of what you see in Destiny is actually an Item used in a new and creative way. This is the definition for Items in Destiny, which started off as just entities that could exist in your Inventory but ended up being the backing data for so much more: quests, reward previews, slots, and subclasses.
In practice, you will want to associate this data with "live" item data from a Bungie.Net Platform call: these definitions describe the item in generic, non-instanced terms: but an actual instance of an item can vary widely from these generic definitions.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| tooltipNotifications | Array[Destiny.Definitions.DestinyItemTooltipNotification] | Tooltips that only come up conditionally for the item. Check the live data DestinyItemComponent.tooltipNotificationIndexes property for which of these should be shown at runtime. | No |
| collectibleHash | integer (uint32) | If this item has a collectible related to it, this is the hash identifier of that collectible entry. | No |
| iconWatermark | string | If available, this is the original 'active' release watermark overlay for the icon. If the item has different versions, this can be overridden by the 'display version watermark icon' from the 'quality' block. Alternatively, if there is no watermark for the version, and the item version has a power cap below the current season power cap, this can be overridden by the iconWatermarkShelved property. | No |
| iconWatermarkShelved | string | If available, this is the 'shelved' release watermark overlay for the icon. If the item version has a power cap below the current season power cap, it can be treated as 'shelved', and should be shown with this 'shelved' watermark overlay. | No |
| iconWatermarkFeatured | string | This is the active watermark for the item if it is currently Featured in-game. Clients should use the isFeaturedItem boolean to decide whether or not to show this as opposed to iconWatermark. | No |
| secondaryIcon | string | A secondary icon associated with the item. Currently this is used in very context specific applications, such as Emblem Nameplates. | No |
| secondaryOverlay | string | Pulled from the secondary icon, this is the "secondary background" of the secondary icon. Confusing? Sure, that's why I call it "overlay" here: because as far as it's been used thus far, it has been for an optional overlay image. We'll see if that holds up, but at least for now it explains what this image is a bit better. | No |
| secondarySpecial | string | Pulled from the Secondary Icon, this is the "special" background for the item. For Emblems, this is the background image used on the Details view: but it need not be limited to that for other types of items. | No |
| backgroundColor | object | Sometimes, an item will have a background color. Most notably this occurs with Emblems, who use the Background Color for small character nameplates such as the "friends" view you see in-game. There are almost certainly other items that have background color as well, though I have not bothered to investigate what items have it nor what purposes they serve: use it as you will. | No |
| isFeaturedItem | boolean | Whether or not this item is currently featured in the game, giving it a special watermark | No |
| screenshot | string | If we were able to acquire an in-game screenshot for the item, the path to that screenshot will be returned here. Note that not all items have screenshots: particularly not any non-equippable items. | No |
| itemTypeDisplayName | string | The localized title/name of the item's type. This can be whatever the designers want, and has no guarantee of consistency between items. | No |
| flavorText | string |  | No |
| uiItemDisplayStyle | string | A string identifier that the game's UI uses to determine how the item should be rendered in inventory screens and the like. This could really be anything - at the moment, we don't have the time to really breakdown and maintain all the possible strings this could be, partly because new ones could be added ad hoc. But if you want to use it to dictate your own UI, or look for items with a certain display style, go for it! | No |
| itemTypeAndTierDisplayName | string | It became a common enough pattern in our UI to show Item Type and Tier combined into a single localized string that I'm just going to go ahead and start pre-creating these for items. | No |
| displaySource | string | In theory, it is a localized string telling you about how you can find the item. I really wish this was more consistent. Many times, it has nothing. Sometimes, it's instead a more narrative-forward description of the item. Which is cool, and I wish all properties had that data, but it should really be its own property. | No |
| tooltipStyle | string | An identifier that the game UI uses to determine what type of tooltip to show for the item. These have no corresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differently according to these styles (or ignore it). | No |
| action | object | If the item can be "used", this block will be non-null, and will have data related to the action performed when using the item. (Guess what? 99% of the time, this action is "dismantle". Shocker) | No |
| crafting | object | Recipe items will have relevant crafting information available here. | No |
| inventory | object | If this item can exist in an inventory, this block will be non-null. In practice, every item that currently exists has one of these blocks. But note that it is not necessarily guaranteed. | No |
| setData | object | If this item is a quest, this block will be non-null. In practice, I wish I had called this the Quest block, but at the time it wasn't clear to me whether it would end up being used for purposes other than quests. It will contain data about the steps in the quest, and mechanics we can use for displaying and tracking the quest. | No |
| stats | object | If this item can have stats (such as a weapon, armor, or vehicle), this block will be non-null and populated with the stats found on the item. | No |
| emblemObjectiveHash | integer (uint32) | If the item is an emblem that has a special Objective attached to it - for instance, if the emblem tracks PVP Kills, or what-have-you. This is a bit different from, for example, the Vanguard Kill Tracker mod, which pipes data into the "art channel". When I get some time, I would like to standardize these so you can get at the values they expose without having to care about what they're being used for and how they are wired up, but for now here's the raw data. | No |
| equippingBlock | object | If this item can be equipped, this block will be non-null and will be populated with the conditions under which it can be equipped. | No |
| translationBlock | object | If this item can be rendered, this block will be non-null and will be populated with rendering information. | No |
| preview | object | If this item can be Used or Acquired to gain other items (for instance, how Eververse Boxes can be consumed to get items from the box), this block will be non-null and will give summary information for the items that can be acquired. | No |
| quality | object | If this item can have a level or stats, this block will be non-null and will be populated with default quality (item level, "quality", and infusion) data. See the block for more details, there's often less upfront information in D2 so you'll want to be aware of how you use quality and item level on the definition level now. | No |
| value | object | The conceptual "Value" of an item, if any was defined. See the DestinyItemValueBlockDefinition for more details. | No |
| sourceData | object | If this item has a known source, this block will be non-null and populated with source information. Unfortunately, at this time we are not generating sources: that is some aggressively manual work which we didn't have time for, and I'm hoping to get back to at some point in the future. | No |
| objectives | object | If this item has Objectives (extra tasks that can be accomplished related to the item... most frequently when the item is a Quest Step and the Objectives need to be completed to move on to the next Quest Step), this block will be non-null and the objectives defined herein. | No |
| metrics | object | If this item has available metrics to be shown, this block will be non-null have the appropriate hashes defined. | No |
| plug | object | If this item *is* a Plug, this will be non-null and the info defined herein. See DestinyItemPlugDefinition for more information. | No |
| gearset | object | If this item has related items in a "Gear Set", this will be non-null and the relationships defined herein. | No |
| sack | object | If this item is a "reward sack" that can be opened to provide other items, this will be non-null and the properties of the sack contained herein. | No |
| sockets | object | If this item has any Sockets, this will be non-null and the individual sockets on the item will be defined herein. | No |
| summary | object | Summary data about the item. | No |
| talentGrid | object | If the item has a Talent Grid, this will be non-null and the properties of the grid defined herein. Note that, while many items still have talent grids, the only ones with meaningful Nodes still on them will be Subclass/"Build" items. | No |
| investmentStats | Array[Destiny.Definitions.DestinyItemInvestmentStatDefinition] | If the item has stats, this block will be defined. It has the "raw" investment stats for the item. These investment stats don't take into account the ways that the items can spawn, nor do they take into account any Stat Group transformations. I have retained them for debugging purposes, but I do not know how useful people will find them. | No |
| perks | Array[Destiny.Definitions.DestinyItemPerkEntryDefinition] | If the item has any *intrinsic* Perks (Perks that it will provide regardless of Sockets, Talent Grid, and other transitory state), they will be defined here. | No |
| loreHash | integer (uint32) | If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can use to look up the lore definition. | No |
| summaryItemHash | integer (uint32) | There are times when the game will show you a "summary/vague" version of an item - such as a description of its type represented as a DestinyInventoryItemDefinition - rather than display the item itself.
This happens sometimes when summarizing possible rewards in a tooltip. This is the item displayed instead, if it exists. | No |
| animations | Array[Destiny.Definitions.Animations.DestinyAnimationReference] | If any animations were extracted from game content for this item, these will be the definitions of those animations. | No |
| allowActions | boolean | BNet may forbid the execution of actions on this item via the API. If that is occurring, allowActions will be set to false. | No |
| links | Array[Links.HyperlinkReference] | If we added any help or informational URLs about this item, these will be those links. | No |
| doesPostmasterPullHaveSideEffects | boolean | The boolean will indicate to us (and you!) whether something *could* happen when you transfer this item from the Postmaster that might be considered a "destructive" action.
It is not feasible currently to tell you (or ourelves!) in a consistent way whether this *will* actually cause a destructive action, so we are playing it safe: if it has the potential to do so, we will not allow it to be transferred from the Postmaster by default. You will need to check for this flag before transferring an item from the Postmaster, or else you'll end up receiving an error. | No |
| nonTransferrable | boolean | The intrinsic transferability of an item.
I hate that this boolean is negative - but there's a reason.
Just because an item is intrinsically transferrable doesn't mean that it can be transferred, and we don't want to imply that this is the only source of that transferability. | No |
| itemCategoryHashes | Array[integer] | BNet attempts to make a more formal definition of item "Categories", as defined by DestinyItemCategoryDefinition. This is a list of all Categories that we were able to algorithmically determine that this item is a member of. (for instance, that it's a "Weapon", that it's an "Auto Rifle", etc...)
The algorithm for these is, unfortunately, volatile. If you believe you see a miscategorized item, please let us know on the Bungie API forums. | No |
| specialItemType | integer (int32) | In Destiny 1, we identified some items as having particular categories that we'd like to know about for various internal logic purposes. These are defined in SpecialItemType, and while these days the itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience. | No |
| itemType | integer (int32) | A value indicating the "base" the of the item. This enum is a useful but dramatic oversimplification of what it means for an item to have a "Type". Still, it's handy in many situations.
itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience. | No |
| itemSubType | integer (int32) | A value indicating the "sub-type" of the item. For instance, where an item might have an itemType value "Weapon", this will be something more specific like "Auto Rifle".
itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience. | No |
| classType | integer (int32) | We run a similarly weak-sauce algorithm to try and determine whether an item is restricted to a specific class. If we find it to be restricted in such a way, we set this classType property to match the class' enumeration value so that users can easily identify class restricted items.
If you see a mis-classed item, please inform the developers in the Bungie API forum. | No |
| breakerType | integer (int32) | Some weapons and plugs can have a "Breaker Type": a special ability that works sort of like damage type vulnerabilities. This is (almost?) always set on items by plugs. | No |
| breakerTypeHash | integer (uint32) | Since we also have a breaker type definition, this is the hash for that breaker type for your convenience. Whether you use the enum or hash and look up the definition depends on what's cleanest for your code. | No |
| equippable | boolean | If true, then you will be allowed to equip the item if you pass its other requirements.
This being false means that you cannot equip the item under any circumstances. | No |
| damageTypeHashes | Array[integer] | Theoretically, an item can have many possible damage types. In *practice*, this is not true, but just in case weapons start being made that have multiple (for instance, an item where a socket has reusable plugs for every possible damage type that you can choose from freely), this field will return all of the possible damage types that are available to the weapon by default. | No |
| damageTypes | Array[integer] | This is the list of all damage types that we know ahead of time the item can take on. Unfortunately, this does not preclude the possibility of something funky happening to give the item a damage type that cannot be predicted beforehand: for example, if some designer decides to create arbitrary non-reusable plugs that cause damage type to change.
This damage type prediction will only use the following to determine potential damage types:
- Intrinsic perks
- Talent Node perks
- Known, reusable plugs for sockets | No |
| defaultDamageType | integer (int32) | If the item has a damage type that could be considered to be default, it will be populated here.
For various upsetting reasons, it's surprisingly cumbersome to figure this out. I hope you're happy. | No |
| defaultDamageTypeHash | integer (uint32) | Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition.
I will likely regret leaving in the enumeration versions of these properties, but for now they're very convenient. | No |
| seasonHash | integer (uint32) | If this item is related directly to a Season of Destiny, this is the hash identifier for that season. | No |
| isWrapper | boolean | If true, this is a dummy vendor-wrapped item template. Items purchased from Eververse will be "wrapped" by one of these items so that we can safely provide refund capabilities before the item is "unwrapped". | No |
| traitIds | Array[string] | Traits are metadata tags applied to this item. For example: armor slot, weapon type, foundry, faction, etc. These IDs come from the game and don't map to any content, but should still be useful. | No |
| traitHashes | Array[integer] | These are the corresponding trait definition hashes for the entries in traitIds. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyInventoryItemDefinition object
const example = {
  displayProperties: null,
  tooltipNotifications: [],
  collectibleHash: 123,
  iconWatermark: "example value",
  iconWatermarkShelved: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyInventoryItemDefinition object
example = {
    "displayProperties": None,
    "tooltipNotifications": [],
    "collectibleHash": 123,
    "iconWatermark": "example value",
    "iconWatermarkShelved": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.DamageType**: Referenced in this entity
- **Destiny.Definitions.Animations.DestinyAnimationReference**: Referenced in this entity
- **Destiny.Definitions.BreakerTypes.DestinyBreakerTypeDefinition**: Referenced in this entity
- **Destiny.Definitions.Collectibles.DestinyCollectibleDefinition**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDamageTypeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyEquippingBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemActionBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemCategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemCraftingBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemGearsetBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemInventoryBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemInvestmentStatDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemMetricBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemObjectiveBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemPerkEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemPreviewBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemQualityBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSackBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSetBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSocketBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSourceBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemStatBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSummaryBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemTalentGridBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemTooltipNotification**: Referenced in this entity
- **Destiny.Definitions.DestinyItemTranslationBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemValueBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyItemPlugDefinition**: Referenced in this entity
- **Destiny.Definitions.Lore.DestinyLoreDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonDefinition**: Referenced in this entity
- **Destiny.DestinyBreakerType**: Referenced in this entity
- **Destiny.DestinyClass**: Referenced in this entity
- **Destiny.DestinyItemSubType**: Referenced in this entity
- **Destiny.DestinyItemType**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity
- **Destiny.SpecialItemType**: Referenced in this entity
- **Links.HyperlinkReference**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyInventoryItemDefinition":   {
      "description": "So much of what you see in Destiny is actually an Item used in a new and creative way. This is the definition for Items in Destiny, which started off as just entities that could exist in your Inventory but ended up being the backing data for so much more: quests, reward previews, slots, and subclasses.\r\nIn practice, you will want to associate this data with \"live\" item data from a Bungie.Net Platform call: these definitions describe the item in generic, non-instanced terms: but an actual instance of an item can vary widely from these generic definitions.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "tooltipNotifications": {
              "description": "Tooltips that only come up conditionally for the item. Check the live data DestinyItemComponent.tooltipNotificationIndexes property for which of these should be shown at runtime.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemTooltipNotification"
              }
          },
          "collectibleHash": {
              "format": "uint32",
              "description": "If this item has a collectible related to it, this is the hash identifier of that collectible entry.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleDefinition"
              }
          },
          "iconWatermark": {
              "description": "If available, this is the original 'active' release watermark overlay for the icon. If the item has different versions, this can be overridden by the 'display version watermark icon' from the 'quality' block. Alternatively, if there is no watermark for the version, and the item version has a power cap below the current season power cap, this can be overridden by the iconWatermarkShelved property.",
              "type": "string"
          },
          "iconWatermarkShelved": {
              "description": "If available, this is the 'shelved' release watermark overlay for the icon. If the item version has a power cap below the current season power cap, it can be treated as 'shelved', and should be shown with this 'shelved' watermark overlay.",
              "type": "string"
          },
          "iconWatermarkFeatured": {
              "description": "This is the active watermark for the item if it is currently Featured in-game. Clients should use the isFeaturedItem boolean to decide whether or not to show this as opposed to iconWatermark.",
              "type": "string"
          },
          "secondaryIcon": {
              "description": "A secondary icon associated with the item. Currently this is used in very context specific applications, such as Emblem Nameplates.",
              "type": "string"
          },
          "secondaryOverlay": {
              "description": "Pulled from the secondary icon, this is the \"secondary background\" of the secondary icon. Confusing? Sure, that's why I call it \"overlay\" here: because as far as it's been used thus far, it has been for an optional overlay image. We'll see if that holds up, but at least for now it explains what this image is a bit better.",
              "type": "string"
          },
          "secondarySpecial": {
              "description": "Pulled from the Secondary Icon, this is the \"special\" background for the item. For Emblems, this is the background image used on the Details view: but it need not be limited to that for other types of items.",
              "type": "string"
          },
          "backgroundColor": {
              "description": "Sometimes, an item will have a background color. Most notably this occurs with Emblems, who use the Background Color for small character nameplates such as the \"friends\" view you see in-game. There are almost certainly other items that have background color as well, though I have not bothered to investigate what items have it nor what purposes they serve: use it as you will.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Misc.DestinyColor"
                  }
              ]
          },
          "isFeaturedItem": {
              "description": "Whether or not this item is currently featured in the game, giving it a special watermark",
              "type": "boolean"
          },
          "screenshot": {
              "description": "If we were able to acquire an in-game screenshot for the item, the path to that screenshot will be returned here. Note that not all items have screenshots: particularly not any non-equippable items.",
              "type": "string"
          },
          "itemTypeDisplayName": {
              "description": "The localized title/name of the item's type. This can be whatever the designers want, and has no guarantee of consistency between items.",
              "type": "string"
          },
          "flavorText": {
              "type": "string"
          },
          "uiItemDisplayStyle": {
              "description": "A string identifier that the game's UI uses to determine how the item should be rendered in inventory screens and the like. This could really be anything - at the moment, we don't have the time to really breakdown and maintain all the possible strings this could be, partly because new ones could be added ad hoc. But if you want to use it to dictate your own UI, or look for items with a certain display style, go for it!",
              "type": "string"
          },
          "itemTypeAndTierDisplayName": {
              "description": "It became a common enough pattern in our UI to show Item Type and Tier combined into a single localized string that I'm just going to go ahead and start pre-creating these for items.",
              "type": "string"
          },
          "displaySource": {
              "description": "In theory, it is a localized string telling you about how you can find the item. I really wish this was more consistent. Many times, it has nothing. Sometimes, it's instead a more narrative-forward description of the item. Which is cool, and I wish all properties had that data, but it should really be its own property.",
              "type": "string"
          },
          "tooltipStyle": {
              "description": "An identifier that the game UI uses to determine what type of tooltip to show for the item. These have no corresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differently according to these styles (or ignore it).",
              "type": "string"
          },
          "action": {
              "description": "If the item can be \"used\", this block will be non-null, and will have data related to the action performed when using the item. (Guess what? 99% of the time, this action is \"dismantle\". Shocker)",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemActionBlockDefinition"
                  }
              ]
          },
          "crafting": {
              "description": "Recipe items will have relevant crafting information available here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemCraftingBlockDefinition"
                  }
              ]
          },
          "inventory": {
              "description": "If this item can exist in an inventory, this block will be non-null. In practice, every item that currently exists has one of these blocks. But note that it is not necessarily guaranteed.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemInventoryBlockDefinition"
                  }
              ]
          },
          "setData": {
              "description": "If this item is a quest, this block will be non-null. In practice, I wish I had called this the Quest block, but at the time it wasn't clear to me whether it would end up being used for purposes other than quests. It will contain data about the steps in the quest, and mechanics we can use for displaying and tracking the quest.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemSetBlockDefinition"
                  }
              ]
          },
          "stats": {
              "description": "If this item can have stats (such as a weapon, armor, or vehicle), this block will be non-null and populated with the stats found on the item.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemStatBlockDefinition"
                  }
              ]
          },
          "emblemObjectiveHash": {
              "format": "uint32",
              "description": "If the item is an emblem that has a special Objective attached to it - for instance, if the emblem tracks PVP Kills, or what-have-you. This is a bit different from, for example, the Vanguard Kill Tracker mod, which pipes data into the \"art channel\". When I get some time, I would like to standardize these so you can get at the values they expose without having to care about what they're being used for and how they are wired up, but for now here's the raw data.",
              "type": "integer"
          },
          "equippingBlock": {
              "description": "If this item can be equipped, this block will be non-null and will be populated with the conditions under which it can be equipped.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyEquippingBlockDefinition"
                  }
              ]
          },
          "translationBlock": {
              "description": "If this item can be rendered, this block will be non-null and will be populated with rendering information.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemTranslationBlockDefinition"
                  }
              ]
          },
          "preview": {
              "description": "If this item can be Used or Acquired to gain other items (for instance, how Eververse Boxes can be consumed to get items from the box), this block will be non-null and will give summary information for the items that can be acquired.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemPreviewBlockDefinition"
                  }
              ]
          },
          "quality": {
              "description": "If this item can have a level or stats, this block will be non-null and will be populated with default quality (item level, \"quality\", and infusion) data. See the block for more details, there's often less upfront information in D2 so you'll want to be aware of how you use quality and item level on the definition level now.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemQualityBlockDefinition"
                  }
              ]
          },
          "value": {
              "description": "The conceptual \"Value\" of an item, if any was defined. See the DestinyItemValueBlockDefinition for more details.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemValueBlockDefinition"
                  }
              ]
          },
          "sourceData": {
              "description": "If this item has a known source, this block will be non-null and populated with source information. Unfortunately, at this time we are not generating sources: that is some aggressively manual work which we didn't have time for, and I'm hoping to get back to at some point in the future.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemSourceBlockDefinition"
                  }
              ]
          },
          "objectives": {
              "description": "If this item has Objectives (extra tasks that can be accomplished related to the item... most frequently when the item is a Quest Step and the Objectives need to be completed to move on to the next Quest Step), this block will be non-null and the objectives defined herein.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemObjectiveBlockDefinition"
                  }
              ]
          },
          "metrics": {
              "description": "If this item has available metrics to be shown, this block will be non-null have the appropriate hashes defined.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemMetricBlockDefinition"
                  }
              ]
          },
          "plug": {
              "description": "If this item *is* a Plug, this will be non-null and the info defined herein. See DestinyItemPlugDefinition for more information.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Items.DestinyItemPlugDefinition"
                  }
              ]
          },
          "gearset": {
              "description": "If this item has related items in a \"Gear Set\", this will be non-null and the relationships defined herein.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemGearsetBlockDefinition"
                  }
              ]
          },
          "sack": {
              "description": "If this item is a \"reward sack\" that can be opened to provide other items, this will be non-null and the properties of the sack contained herein.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemSackBlockDefinition"
                  }
              ]
          },
          "sockets": {
              "description": "If this item has any Sockets, this will be non-null and the individual sockets on the item will be defined herein.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemSocketBlockDefinition"
                  }
              ]
          },
          "summary": {
              "description": "Summary data about the item.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemSummaryBlockDefinition"
                  }
              ]
          },
          "talentGrid": {
              "description": "If the item has a Talent Grid, this will be non-null and the properties of the grid defined herein. Note that, while many items still have talent grids, the only ones with meaningful Nodes still on them will be Subclass/\"Build\" items.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemTalentGridBlockDefinition"
                  }
              ]
          },
          "investmentStats": {
              "description": "If the item has stats, this block will be defined. It has the \"raw\" investment stats for the item. These investment stats don't take into account the ways that the items can spawn, nor do they take into account any Stat Group transformations. I have retained them for debugging purposes, but I do not know how useful people will find them.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemInvestmentStatDefinition"
              }
          },
          "perks": {
              "description": "If the item has any *intrinsic* Perks (Perks that it will provide regardless of Sockets, Talent Grid, and other transitory state), they will be defined here.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemPerkEntryDefinition"
              }
          },
          "loreHash": {
              "format": "uint32",
              "description": "If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can use to look up the lore definition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Lore.DestinyLoreDefinition"
              }
          },
          "summaryItemHash": {
              "format": "uint32",
              "description": "There are times when the game will show you a \"summary/vague\" version of an item - such as a description of its type represented as a DestinyInventoryItemDefinition - rather than display the item itself.\r\nThis happens sometimes when summarizing possible rewards in a tooltip. This is the item displayed instead, if it exists.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "animations": {
              "description": "If any animations were extracted from game content for this item, these will be the definitions of those animations.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Animations.DestinyAnimationReference"
              }
          },
          "allowActions": {
              "description": "BNet may forbid the execution of actions on this item via the API. If that is occurring, allowActions will be set to false.",
              "type": "boolean"
          },
          "links": {
              "description": "If we added any help or informational URLs about this item, these will be those links.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Links.HyperlinkReference"
              }
          },
          "doesPostmasterPullHaveSideEffects": {
              "description": "The boolean will indicate to us (and you!) whether something *could* happen when you transfer this item from the Postmaster that might be considered a \"destructive\" action.\r\nIt is not feasible currently to tell you (or ourelves!) in a consistent way whether this *will* actually cause a destructive action, so we are playing it safe: if it has the potential to do so, we will not allow it to be transferred from the Postmaster by default. You will need to check for this flag before transferring an item from the Postmaster, or else you'll end up receiving an error.",
              "type": "boolean"
          },
          "nonTransferrable": {
              "description": "The intrinsic transferability of an item.\r\nI hate that this boolean is negative - but there's a reason.\r\nJust because an item is intrinsically transferrable doesn't mean that it can be transferred, and we don't want to imply that this is the only source of that transferability.",
              "type": "boolean"
          },
          "itemCategoryHashes": {
              "description": "BNet attempts to make a more formal definition of item \"Categories\", as defined by DestinyItemCategoryDefinition. This is a list of all Categories that we were able to algorithmically determine that this item is a member of. (for instance, that it's a \"Weapon\", that it's an \"Auto Rifle\", etc...)\r\nThe algorithm for these is, unfortunately, volatile. If you believe you see a miscategorized item, please let us know on the Bungie API forums.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemCategoryDefinition"
              }
          },
          "specialItemType": {
              "format": "int32",
              "description": "In Destiny 1, we identified some items as having particular categories that we'd like to know about for various internal logic purposes. These are defined in SpecialItemType, and while these days the itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.SpecialItemType"
              }
          },
          "itemType": {
              "format": "int32",
              "description": "A value indicating the \"base\" the of the item. This enum is a useful but dramatic oversimplification of what it means for an item to have a \"Type\". Still, it's handy in many situations.\r\nitemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyItemType"
              }
          },
          "itemSubType": {
              "format": "int32",
              "description": "A value indicating the \"sub-type\" of the item. For instance, where an item might have an itemType value \"Weapon\", this will be something more specific like \"Auto Rifle\".\r\nitemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyItemSubType"
              }
          },
          "classType": {
              "format": "int32",
              "description": "We run a similarly weak-sauce algorithm to try and determine whether an item is restricted to a specific class. If we find it to be restricted in such a way, we set this classType property to match the class' enumeration value so that users can easily identify class restricted items.\r\nIf you see a mis-classed item, please inform the developers in the Bungie API forum.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyClass"
              }
          },
          "breakerType": {
              "format": "int32",
              "description": "Some weapons and plugs can have a \"Breaker Type\": a special ability that works sort of like damage type vulnerabilities. This is (almost?) always set on items by plugs.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyBreakerType"
              }
          },
          "breakerTypeHash": {
              "format": "uint32",
              "description": "Since we also have a breaker type definition, this is the hash for that breaker type for your convenience. Whether you use the enum or hash and look up the definition depends on what's cleanest for your code.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.BreakerTypes.DestinyBreakerTypeDefinition"
              }
          },
          "equippable": {
              "description": "If true, then you will be allowed to equip the item if you pass its other requirements.\r\nThis being false means that you cannot equip the item under any circumstances.",
              "type": "boolean"
          },
          "damageTypeHashes": {
              "description": "Theoretically, an item can have many possible damage types. In *practice*, this is not true, but just in case weapons start being made that have multiple (for instance, an item where a socket has reusable plugs for every possible damage type that you can choose from freely), this field will return all of the possible damage types that are available to the weapon by default.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDamageTypeDefinition"
              }
          },
          "damageTypes": {
              "description": "This is the list of all damage types that we know ahead of time the item can take on. Unfortunately, this does not preclude the possibility of something funky happening to give the item a damage type that cannot be predicted beforehand: for example, if some designer decides to create arbitrary non-reusable plugs that cause damage type to change.\r\nThis damage type prediction will only use the following to determine potential damage types:\r\n- Intrinsic perks\r\n- Talent Node perks\r\n- Known, reusable plugs for sockets",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.DamageType"
                  }
              }
          },
          "defaultDamageType": {
              "format": "int32",
              "description": "If the item has a damage type that could be considered to be default, it will be populated here.\r\nFor various upsetting reasons, it's surprisingly cumbersome to figure this out. I hope you're happy.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DamageType"
              }
          },
          "defaultDamageTypeHash": {
              "format": "uint32",
              "description": "Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition.\r\nI will likely regret leaving in the enumeration versions of these properties, but for now they're very convenient.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDamageTypeDefinition"
              }
          },
          "seasonHash": {
              "format": "uint32",
              "description": "If this item is related directly to a Season of Destiny, this is the hash identifier for that season.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonDefinition"
              }
          },
          "isWrapper": {
              "description": "If true, this is a dummy vendor-wrapped item template. Items purchased from Eververse will be \"wrapped\" by one of these items so that we can safely provide refund capabilities before the item is \"unwrapped\".",
              "type": "boolean"
          },
          "traitIds": {
              "description": "Traits are metadata tags applied to this item. For example: armor slot, weapon type, foundry, faction, etc. These IDs come from the game and don't map to any content, but should still be useful.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "traitHashes": {
              "description": "These are the corresponding trait definition hashes for the entries in traitIds.",
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
      "x-mobile-manifest-name": "Items"
  }
}
```
