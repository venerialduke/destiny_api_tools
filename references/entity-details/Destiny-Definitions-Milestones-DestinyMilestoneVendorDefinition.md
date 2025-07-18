# Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If the Milestone or a component has vendors whose inventories could/should be displayed that are relevant to it, this will return the vendor in question. 
It also contains information we need to determine whether that vendor is actually relevant at the moment, given the user's current state.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | The hash of the vendor whose wares should be shown as associated with the Milestone. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition object
const example = {
  vendorHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition object
example = {
    "vendorHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneVendorDefinition":   {
      "description": "If the Milestone or a component has vendors whose inventories could/should be displayed that are relevant to it, this will return the vendor in question. \r\nIt also contains information we need to determine whether that vendor is actually relevant at the moment, given the user's current state.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "The hash of the vendor whose wares should be shown as associated with the Milestone.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          }
      }
  }
}
```
