# Destiny.Definitions.DestinyTalentNodeCategory

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeCategory
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
An artificial construct provided by Bungie.Net, where we attempt to group talent nodes by functionality.
This is a single set of references to Talent Nodes that share a common trait or purpose.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| identifier | string | Mostly just for debug purposes, but if you find it useful you can have it. This is BNet's manually created identifier for this category. | No |
| isLoreDriven | boolean | If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations. | No |
| displayProperties | object | Will contain at least the "name", which will be the title of the category. We will likely not have description and an icon yet, but I'm going to keep my options open. | No |
| nodeHashes | Array[integer] | The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyTalentNodeCategory object
const example = {
  identifier: "example value",
  isLoreDriven: true,
  displayProperties: null,
  nodeHashes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyTalentNodeCategory object
example = {
    "identifier": "example value",
    "isLoreDriven": True,
    "displayProperties": None,
    "nodeHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeCategory":   {
      "description": "An artificial construct provided by Bungie.Net, where we attempt to group talent nodes by functionality.\r\nThis is a single set of references to Talent Nodes that share a common trait or purpose.",
      "type": "object",
      "properties": {
          "identifier": {
              "description": "Mostly just for debug purposes, but if you find it useful you can have it. This is BNet's manually created identifier for this category.",
              "type": "string"
          },
          "isLoreDriven": {
              "description": "If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations.",
              "type": "boolean"
          },
          "displayProperties": {
              "description": "Will contain at least the \"name\", which will be the title of the category. We will likely not have description and an icon yet, but I'm going to keep my options open.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "nodeHashes": {
              "description": "The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          }
      }
  }
}
```
