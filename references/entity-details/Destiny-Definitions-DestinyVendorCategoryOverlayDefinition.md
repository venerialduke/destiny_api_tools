# Destiny.Definitions.DestinyVendorCategoryOverlayDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorCategoryOverlayDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The details of an overlay prompt to show to a user. They are all fairly self-explanatory localized strings that can be shown.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| choiceDescription | string |  | No |
| description | string |  | No |
| icon | string |  | No |
| title | string |  | No |
| currencyItemHash | integer (uint32) | If this overlay has a currency item that it features, this is said featured item. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorCategoryOverlayDefinition object
const example = {
  choiceDescription: "example value",
  description: "example value",
  icon: "example value",
  title: "example value",
  currencyItemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorCategoryOverlayDefinition object
example = {
    "choiceDescription": "example value",
    "description": "example value",
    "icon": "example value",
    "title": "example value",
    "currencyItemHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorCategoryOverlayDefinition":   {
      "description": "The details of an overlay prompt to show to a user. They are all fairly self-explanatory localized strings that can be shown.",
      "type": "object",
      "properties": {
          "choiceDescription": {
              "type": "string"
          },
          "description": {
              "type": "string"
          },
          "icon": {
              "type": "string"
          },
          "title": {
              "type": "string"
          },
          "currencyItemHash": {
              "format": "uint32",
              "description": "If this overlay has a currency item that it features, this is said featured item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
