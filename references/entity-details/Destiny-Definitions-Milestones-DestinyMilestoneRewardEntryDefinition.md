# Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition of a specific reward, which may be contained in a category of rewards and that has optional information about how it is obtained.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rewardEntryHash | integer (uint32) | The identifier for this reward entry. Runtime data will refer to reward entries by this hash. Only guaranteed unique within the specific Milestone. | No |
| rewardEntryIdentifier | string | The string identifier, if you care about it. Only guaranteed unique within the specific Milestone. | No |
| items | Array[Destiny.DestinyItemQuantity] | The items you will get as rewards, and how much of it you'll get. | No |
| vendorHash | integer (uint32) | If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in order to redeem the reward. Use this hash to look up the DestinyVendorDefinition. | No |
| displayProperties | object | For us to bother returning this info, we should be able to return some kind of information about why these rewards are grouped together. This is ideally that information. Look at how confident I am that this will always remain true. | No |
| order | integer (int32) | If you want to follow BNet's ordering of these rewards, use this number within a given category to order the rewards. Yeah, I know. I feel dirty too. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition object
const example = {
  rewardEntryHash: 123,
  rewardEntryIdentifier: "example value",
  items: [],
  vendorHash: 123,
  displayProperties: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition object
example = {
    "rewardEntryHash": 123,
    "rewardEntryIdentifier": "example value",
    "items": [],
    "vendorHash": 123,
    "displayProperties": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition":   {
      "description": "The definition of a specific reward, which may be contained in a category of rewards and that has optional information about how it is obtained.",
      "type": "object",
      "properties": {
          "rewardEntryHash": {
              "format": "uint32",
              "description": "The identifier for this reward entry. Runtime data will refer to reward entries by this hash. Only guaranteed unique within the specific Milestone.",
              "type": "integer"
          },
          "rewardEntryIdentifier": {
              "description": "The string identifier, if you care about it. Only guaranteed unique within the specific Milestone.",
              "type": "string"
          },
          "items": {
              "description": "The items you will get as rewards, and how much of it you'll get.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          },
          "vendorHash": {
              "format": "uint32",
              "description": "If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in order to redeem the reward. Use this hash to look up the DestinyVendorDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "displayProperties": {
              "description": "For us to bother returning this info, we should be able to return some kind of information about why these rewards are grouped together. This is ideally that information. Look at how confident I am that this will always remain true.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "order": {
              "format": "int32",
              "description": "If you want to follow BNet's ordering of these rewards, use this number within a given category to order the rewards. Yeah, I know. I feel dirty too.",
              "type": "integer"
          }
      }
  }
}
```
