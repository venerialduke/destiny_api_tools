# Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Presentation nodes can be restricted by various requirements. This defines the rules of those requirements, and the message(s) to be shown if these requirements aren't met.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| entitlementUnavailableMessage | string | If this node is not accessible due to Entitlements (for instance, you don't own the required game expansion), this is the message to show. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock object
const example = {
  entitlementUnavailableMessage: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock object
example = {
    "entitlementUnavailableMessage": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock":   {
      "description": "Presentation nodes can be restricted by various requirements. This defines the rules of those requirements, and the message(s) to be shown if these requirements aren't met.",
      "type": "object",
      "properties": {
          "entitlementUnavailableMessage": {
              "description": "If this node is not accessible due to Entitlements (for instance, you don't own the required game expansion), this is the message to show.",
              "type": "string"
          }
      }
  }
}
```
