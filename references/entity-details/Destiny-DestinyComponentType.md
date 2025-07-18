# Destiny.DestinyComponentType

## Entity Information
- **Entity Name**: Destiny.DestinyComponentType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Represents the possible components that can be returned from Destiny "Get" calls such as GetProfile, GetCharacter, GetVendor etc...
When making one of these requests, you will pass one or more of these components as a comma separated list in the "?components=" querystring parameter. For instance, if you want baseline Profile data, Character Data, and character progressions, you would pass "?components=Profiles,Characters,CharacterProgressions" You may use either the numerical or string values.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 100 | Profiles | Profiles is the most basic component, only relevant when calling GetProfile. This returns basic information about the profile, which is almost nothing: a list of characterIds, some information about the last time you logged in, and that most sobering statistic: how long you've played. |
| 101 | VendorReceipts | Only applicable for GetProfile, this will return information about receipts for refundable vendor items. |
| 102 | ProfileInventories | Asking for this will get you the profile-level inventories, such as your Vault buckets (yeah, the Vault is really inventory buckets located on your Profile) |
| 103 | ProfileCurrencies | This will get you a summary of items on your Profile that we consider to be "currencies", such as Glimmer. I mean, if there's Glimmer in Destiny 2. I didn't say there was Glimmer. |
| 104 | ProfileProgression | This will get you any progression-related information that exists on a Profile-wide level, across all characters. |
| 105 | PlatformSilver | This will get you information about the silver that this profile has on every platform on which it plays.
 You may only request this component for the logged in user's Profile, and will not recieve it if you request it for another Profile. |
| 200 | Characters | This will get you summary info about each of the characters in the profile. |
| 201 | CharacterInventories | This will get you information about any non-equipped items on the character or character(s) in question, if you're allowed to see it. You have to either be authenticated as that user, or that user must allow anonymous viewing of their non-equipped items in Bungie.Net settings to actually get results. |
| 202 | CharacterProgressions | This will get you information about the progression (faction, experience, etc... "levels") relevant to each character, if you are the currently authenticated user or the user has elected to allow anonymous viewing of its progression info. |
| 203 | CharacterRenderData | This will get you just enough information to be able to render the character in 3D if you have written a 3D rendering library for Destiny Characters, or "borrowed" ours. It's okay, I won't tell anyone if you're using it. I'm no snitch. (actually, we don't care if you use it - go to town) |
| 204 | CharacterActivities | This will return info about activities that a user can see and gating on it, if you are the currently authenticated user or the user has elected to allow anonymous viewing of its progression info. Note that the data returned by this can be unfortunately problematic and relatively unreliable in some cases. We'll eventually work on making it more consistently reliable. |
| 205 | CharacterEquipment | This will return info about the equipped items on the character(s). Everyone can see this. |
| 206 | CharacterLoadouts | This will return info about the loadouts of the character(s). |
| 300 | ItemInstances | This will return basic info about instanced items - whether they can be equipped, their tracked status, and some info commonly needed in many places (current damage type, primary stat value, etc) |
| 301 | ItemObjectives | Items can have Objectives (DestinyObjectiveDefinition) bound to them. If they do, this will return info for items that have such bound objectives. |
| 302 | ItemPerks | Items can have perks (DestinySandboxPerkDefinition). If they do, this will return info for what perks are active on items. |
| 303 | ItemRenderData | If you just want to render the weapon, this is just enough info to do that rendering. |
| 304 | ItemStats | Items can have stats, like rate of fire. Asking for this component will return requested item's stats if they have stats. |
| 305 | ItemSockets | Items can have sockets, where plugs can be inserted. Asking for this component will return all info relevant to the sockets on items that have them. |
| 306 | ItemTalentGrids | Items can have talent grids, though that matters a lot less frequently than it used to. Asking for this component will return all relevant info about activated Nodes and Steps on this talent grid, like the good ol' days. |
| 307 | ItemCommonData | Items that *aren't* instanced still have important information you need to know: how much of it you have, the itemHash so you can look up their DestinyInventoryItemDefinition, whether they're locked, etc... Both instanced and non-instanced items will have these properties. You will get this automatically with Inventory components - you only need to pass this when calling GetItem on a specific item. |
| 308 | ItemPlugStates | Items that are "Plugs" can be inserted into sockets. This returns statuses about those plugs and why they can/can't be inserted. I hear you giggling, there's nothing funny about inserting plugs. Get your head out of the gutter and pay attention! |
| 309 | ItemPlugObjectives | Sometimes, plugs have objectives on them. This data can get really large, so we split it into its own component. Please, don't grab it unless you need it. |
| 310 | ItemReusablePlugs | Sometimes, designers create thousands of reusable plugs and suddenly your response sizes are almost 3MB, and something has to give.
 Reusable Plugs were split off as their own component, away from ItemSockets, as a result of the Plug changes in Shadowkeep that made plug data infeasibly large for the most common use cases.
 Request this component if and only if you need to know what plugs *could* be inserted into a socket, and need to know it before "drilling" into the details of an item in your application (for instance, if you're doing some sort of interesting sorting or aggregation based on available plugs.
 When you get this, you will also need to combine it with "Plug Sets" data if you want a full picture of all of the available plugs: this component will only return plugs that have state data that is per-item. See Plug Sets for available plugs that have Character, Profile, or no state-specific restrictions. |
| 400 | Vendors | When obtaining vendor information, this will return summary information about the Vendor or Vendors being returned. |
| 401 | VendorCategories | When obtaining vendor information, this will return information about the categories of items provided by the Vendor. |
| 402 | VendorSales | When obtaining vendor information, this will return the information about items being sold by the Vendor. |
| 500 | Kiosks | Asking for this component will return you the account's Kiosk statuses: that is, what items have been filled out/acquired. But only if you are the currently authenticated user or the user has elected to allow anonymous viewing of its progression info. |
| 600 | CurrencyLookups | A "shortcut" component that will give you all of the item hashes/quantities of items that the requested character can use to determine if an action (purchasing, socket insertion) has the required currency. (recall that all currencies are just items, and that some vendor purchases require items that you might not traditionally consider to be a "currency", like plugs/mods!) |
| 700 | PresentationNodes | Returns summary status information about all "Presentation Nodes". See DestinyPresentationNodeDefinition for more details, but the gist is that these are entities used by the game UI to bucket Collectibles and Records into a hierarchy of categories. You may ask for and use this data if you want to perform similar bucketing in your own UI: or you can skip it and roll your own. |
| 800 | Collectibles | Returns summary status information about all "Collectibles". These are records of what items you've discovered while playing Destiny, and some other basic information. For detailed information, you will have to call a separate endpoint devoted to the purpose. |
| 900 | Records | Returns summary status information about all "Records" (also known in the game as "Triumphs". I know, it's confusing because there's also "Moments of Triumph" that will themselves be represented as "Triumphs.") |
| 1000 | Transitory | Returns information that Bungie considers to be "Transitory": data that may change too frequently or come from a non-authoritative source such that we don't consider the data to be fully trustworthy, but that might prove useful for some limited use cases. We can provide no guarantee of timeliness nor consistency for this data: buyer beware with the Transitory component. |
| 1100 | Metrics | Returns summary status information about all "Metrics" (also known in the game as "Stat Trackers"). |
| 1200 | StringVariables | Returns a mapping of localized string variable hashes to values, on a per-account or per-character basis. |
| 1300 | Craftables | Returns summary status information about all "Craftables" aka crafting recipe items. |
| 1400 | SocialCommendations | Returns score values for all commendations and commendation nodes. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyComponentType enumeration values
const DestinyComponentType = {
  None: 0,
  Profiles: 100,
  VendorReceipts: 101,
  // ... more values
};

// Using the enumeration
const value = DestinyComponentType.None;
```

### Python
```python
# Destiny.DestinyComponentType enumeration values
class DestinyComponentType:
    NONE = 0
    PROFILES = 100
    VENDORRECEIPTS = 101
    # ... more values

# Using the enumeration
value = DestinyComponentType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyComponentType":   {
      "format": "int32",
      "description": "Represents the possible components that can be returned from Destiny \"Get\" calls such as GetProfile, GetCharacter, GetVendor etc...\r\nWhen making one of these requests, you will pass one or more of these components as a comma separated list in the \"?components=\" querystring parameter. For instance, if you want baseline Profile data, Character Data, and character progressions, you would pass \"?components=Profiles,Characters,CharacterProgressions\" You may use either the numerical or string values.",
      "enum": [
          "0",
          "100",
          "101",
          "102",
          "103",
          "104",
          "105",
          "200",
          "201",
          "202",
          "203",
          "204",
          "205",
          "206",
          "300",
          "301",
          "302",
          "303",
          "304",
          "305",
          "306",
          "307",
          "308",
          "309",
          "310",
          "400",
          "401",
          "402",
          "500",
          "600",
          "700",
          "800",
          "900",
          "1000",
          "1100",
          "1200",
          "1300",
          "1400"
      ],
      "type": "integer"
  }
}
```
