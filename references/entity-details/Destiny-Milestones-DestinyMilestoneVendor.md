# Destiny.Milestones.DestinyMilestoneVendor

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneVendor
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If a Milestone has one or more Vendors that are relevant to it, this will contain information about that vendor that you can choose to show.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about. | No |
| previewItemHash | integer (uint32) | If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneVendor object
const example = {
  vendorHash: 123,
  previewItemHash: 123,
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneVendor object
example = {
    "vendorHash": 123,
    "previewItemHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneVendor":   {
      "description": "If a Milestone has one or more Vendors that are relevant to it, this will contain information about that vendor that you can choose to show.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "previewItemHash": {
              "format": "uint32",
              "description": "If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
