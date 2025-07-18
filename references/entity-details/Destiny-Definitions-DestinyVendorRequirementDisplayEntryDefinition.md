# Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The localized properties of the requirementsDisplay, allowing information about the requirement or item being featured to be seen.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| icon | string |  | No |
| name | string |  | No |
| source | string |  | No |
| type | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition object
const example = {
  icon: "example value",
  name: "example value",
  source: "example value",
  type: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition object
example = {
    "icon": "example value",
    "name": "example value",
    "source": "example value",
    "type": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition":   {
      "description": "The localized properties of the requirementsDisplay, allowing information about the requirement or item being featured to be seen.",
      "type": "object",
      "properties": {
          "icon": {
              "type": "string"
          },
          "name": {
              "type": "string"
          },
          "source": {
              "type": "string"
          },
          "type": {
              "type": "string"
          }
      }
  }
}
```
