# Destiny.Definitions.DestinyVendorGroupDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorGroupDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
BNet attempts to group vendors into similar collections. These groups aren't technically game canonical, but they are helpful for filtering vendors or showing them organized into a clean view on a webpage or app.
These definitions represent the groups we've built. Unlike in Destiny 1, a Vendors' group may change dynamically as the game state changes: thus, you will want to check DestinyVendorComponent responses to find a vendor's currently active Group (if you care).
Using this will let you group your vendors in your UI in a similar manner to how we will do grouping in the Companion.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| order | integer (int32) | The recommended order in which to render the groups, Ascending order. | No |
| categoryName | string | For now, a group just has a name. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorGroupDefinition object
const example = {
  order: 123,
  categoryName: "example value",
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorGroupDefinition object
example = {
    "order": 123,
    "categoryName": "example value",
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorGroupDefinition":   {
      "description": "BNet attempts to group vendors into similar collections. These groups aren't technically game canonical, but they are helpful for filtering vendors or showing them organized into a clean view on a webpage or app.\r\nThese definitions represent the groups we've built. Unlike in Destiny 1, a Vendors' group may change dynamically as the game state changes: thus, you will want to check DestinyVendorComponent responses to find a vendor's currently active Group (if you care).\r\nUsing this will let you group your vendors in your UI in a similar manner to how we will do grouping in the Companion.",
      "type": "object",
      "properties": {
          "order": {
              "format": "int32",
              "description": "The recommended order in which to render the groups, Ascending order.",
              "type": "integer"
          },
          "categoryName": {
              "description": "For now, a group just has a name.",
              "type": "string"
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "VendorGroups"
  }
}
```
