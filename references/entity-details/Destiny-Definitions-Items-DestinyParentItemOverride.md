# Destiny.Definitions.Items.DestinyParentItemOverride

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyParentItemOverride
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyparentitemoverride data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| additionalEquipRequirementsDisplayStrings | Array[string] |  | No |
| pipIcon | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyParentItemOverride object
const example = {
  additionalEquipRequirementsDisplayStrings: [],
  pipIcon: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyParentItemOverride object
example = {
    "additionalEquipRequirementsDisplayStrings": [],
    "pipIcon": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyParentItemOverride":   {
      "type": "object",
      "properties": {
          "additionalEquipRequirementsDisplayStrings": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "pipIcon": {
              "type": "string"
          }
      }
  }
}
```
