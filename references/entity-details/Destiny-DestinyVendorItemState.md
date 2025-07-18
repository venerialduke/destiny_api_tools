# Destiny.DestinyVendorItemState

## Entity Information
- **Entity Name**: Destiny.DestinyVendorItemState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The possible states of Destiny Profile Records. IMPORTANT: Any given item can theoretically have many of these states simultaneously: as a result, this was altered to be a flags enumeration/bitmask for v3.2.0.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | There are no augments on the item. |
| 1 | Incomplete | Deprecated forever (probably). There was a time when Records were going to be implemented through Vendors, and this field was relevant. Now they're implemented through Presentation Nodes, and this field doesn't matter anymore. |
| 2 | RewardAvailable | Deprecated forever (probably). See the description of the "Incomplete" value for the juicy scoop. |
| 4 | Complete | Deprecated forever (probably). See the description of the "Incomplete" value for the juicy scoop. |
| 8 | New | This item is considered to be "newly available", and should have some UI showing how shiny it is. |
| 16 | Featured | This item is being "featured", and should be shiny in a different way from items that are merely new. |
| 32 | Ending | This item is only available for a limited time, and that time is approaching. |
| 64 | OnSale | This item is "on sale". Get it while it's hot. |
| 128 | Owned | This item is already owned. |
| 256 | WideView | This item should be shown with a "wide view" instead of normal icon view. |
| 512 | NexusAttention | This indicates that you should show some kind of attention-requesting indicator on the item, in a similar manner to items in the nexus that have such notifications. |
| 1024 | SetDiscount | This indicates that the item has some sort of a 'set' discount. |
| 2048 | PriceDrop | This indicates that the item has a price drop. |
| 4096 | DailyOffer | This indicates that the item is a daily offer. |
| 8192 | Charity | This indicates that the item is for charity. |
| 16384 | SeasonalRewardExpiration | This indicates that the item has a seasonal reward expiration. |
| 32768 | BestDeal | This indicates that the sale item is the best deal among different choices. |
| 65536 | Popular | This indicates that the sale item is popular. |
| 131072 | Free | This indicates that the sale item is free. |
| 262144 | Locked | This indicates that the sale item is locked. |
| 524288 | Paracausal | This indicates that the sale item is paracausal. |
| 1048576 | Cryptarch |  |
| 2097152 | ArtifactPerkOwned |  |
| 4194304 | Savings |  |
| 8388608 | Ineligible |  |
| 16777216 | ArtifactPerkBoosted |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyVendorItemState enumeration values
const DestinyVendorItemState = {
  None: 0,
  Incomplete: 1,
  RewardAvailable: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyVendorItemState.None;
```

### Python
```python
# Destiny.DestinyVendorItemState enumeration values
class DestinyVendorItemState:
    NONE = 0
    INCOMPLETE = 1
    REWARDAVAILABLE = 2
    # ... more values

# Using the enumeration
value = DestinyVendorItemState.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyVendorItemState":   {
      "format": "int32",
      "description": "The possible states of Destiny Profile Records. IMPORTANT: Any given item can theoretically have many of these states simultaneously: as a result, this was altered to be a flags enumeration/bitmask for v3.2.0.",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128",
          "256",
          "512",
          "1024",
          "2048",
          "4096",
          "8192",
          "16384",
          "32768",
          "65536",
          "131072",
          "262144",
          "524288",
          "1048576",
          "2097152",
          "4194304",
          "8388608",
          "16777216"
      ],
      "type": "integer"
  }
}
```
