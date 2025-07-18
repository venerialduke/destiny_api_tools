# Destiny.Definitions.DestinyVendorInteractionReplyDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorInteractionReplyDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
When the interaction is replied to, Reward sites will fire and items potentially selected based on whether the given unlock expression is TRUE.
You can potentially choose one from multiple replies when replying to an interaction: this is how you get either/or rewards from vendors.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemRewardsSelection | integer (int32) | The rewards granted upon responding to the vendor. | No |
| reply | string | The localized text for the reply. | No |
| replyType | integer (int32) | An enum indicating the type of reply being made. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorInteractionReplyDefinition object
const example = {
  itemRewardsSelection: 123,
  reply: "example value",
  replyType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorInteractionReplyDefinition object
example = {
    "itemRewardsSelection": 123,
    "reply": "example value",
    "replyType": 123,
}
```

## Related Entities
- **Destiny.DestinyVendorInteractionRewardSelection**: Referenced in this entity
- **Destiny.DestinyVendorReplyType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorInteractionReplyDefinition":   {
      "description": "When the interaction is replied to, Reward sites will fire and items potentially selected based on whether the given unlock expression is TRUE.\r\nYou can potentially choose one from multiple replies when replying to an interaction: this is how you get either/or rewards from vendors.",
      "type": "object",
      "properties": {
          "itemRewardsSelection": {
              "format": "int32",
              "description": "The rewards granted upon responding to the vendor.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyVendorInteractionRewardSelection"
              }
          },
          "reply": {
              "description": "The localized text for the reply.",
              "type": "string"
          },
          "replyType": {
              "format": "int32",
              "description": "An enum indicating the type of reply being made.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyVendorReplyType"
              }
          }
      }
  }
}
```
