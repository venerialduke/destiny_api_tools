# Destiny.Definitions.DestinyItemSourceBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSourceBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Data about an item's "sources": ways that the item can be obtained.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| sourceHashes | Array[integer] | The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition). | No |
| sources | Array[Destiny.Definitions.Sources.DestinyItemSourceDefinition] | A collection of details about the stats that were computed for the ways we found that the item could be spawned. | No |
| exclusive | integer (int32) | If we found that this item is exclusive to a specific platform, this will be set to the BungieMembershipType enumeration that matches that platform. | No |
| vendorSources | Array[Destiny.Definitions.DestinyItemVendorSourceReference] | A denormalized reference back to vendors that potentially sell this item. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSourceBlockDefinition object
const example = {
  sourceHashes: [],
  sources: [],
  exclusive: 123,
  vendorSources: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSourceBlockDefinition object
example = {
    "sourceHashes": [],
    "sources": [],
    "exclusive": 123,
    "vendorSources": [],
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Definitions.DestinyItemVendorSourceReference**: Referenced in this entity
- **Destiny.Definitions.DestinyRewardSourceDefinition**: Referenced in this entity
- **Destiny.Definitions.Sources.DestinyItemSourceDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSourceBlockDefinition":   {
      "description": "Data about an item's \"sources\": ways that the item can be obtained.",
      "type": "object",
      "properties": {
          "sourceHashes": {
              "description": "The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition).",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyRewardSourceDefinition"
              }
          },
          "sources": {
              "description": "A collection of details about the stats that were computed for the ways we found that the item could be spawned.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Sources.DestinyItemSourceDefinition"
              }
          },
          "exclusive": {
              "format": "int32",
              "description": "If we found that this item is exclusive to a specific platform, this will be set to the BungieMembershipType enumeration that matches that platform.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "vendorSources": {
              "description": "A denormalized reference back to vendors that potentially sell this item.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemVendorSourceReference"
              }
          }
      }
  }
}
```
