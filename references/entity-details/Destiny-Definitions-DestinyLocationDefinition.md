# Destiny.Definitions.DestinyLocationDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyLocationDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
A "Location" is a sort of shortcut for referring to a specific combination of Activity, Destination, Place, and even Bubble or NavPoint within a space.
Most of this data isn't intrinsically useful to us, but Objectives refer to locations, and through that we can at least infer the Activity, Destination, and Place being referred to by the Objective.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorHash | integer (uint32) | If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition. | No |
| locationReleases | Array[Destiny.Definitions.DestinyLocationReleaseDefinition] | A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyLocationDefinition object
const example = {
  vendorHash: 123,
  locationReleases: [],
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyLocationDefinition object
example = {
    "vendorHash": 123,
    "locationReleases": [],
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyLocationReleaseDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyLocationDefinition":   {
      "description": "A \"Location\" is a sort of shortcut for referring to a specific combination of Activity, Destination, Place, and even Bubble or NavPoint within a space.\r\nMost of this data isn't intrinsically useful to us, but Objectives refer to locations, and through that we can at least infer the Activity, Destination, and Place being referred to by the Objective.",
      "type": "object",
      "properties": {
          "vendorHash": {
              "format": "uint32",
              "description": "If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "locationReleases": {
              "description": "A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyLocationReleaseDefinition"
              }
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
      "x-mobile-manifest-name": "Locations"
  }
}
```
