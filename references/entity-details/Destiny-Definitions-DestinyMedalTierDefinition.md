# Destiny.Definitions.DestinyMedalTierDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyMedalTierDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
An artificial construct of our own creation, to try and put some order on top of Medals and keep them from being one giant, unmanageable and unsorted blob of stats.
Unfortunately, we haven't had time to do this evaluation yet in Destiny 2, so we're short on Medal Tiers. This will hopefully be updated over time, if Medals continue to exist.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| tierName | string | The name of the tier. | No |
| order | integer (int32) | If you're rendering medals by tier, render them in this order (ascending) | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyMedalTierDefinition object
const example = {
  tierName: "example value",
  order: 123,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyMedalTierDefinition object
example = {
    "tierName": "example value",
    "order": 123,
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
  "Destiny.Definitions.DestinyMedalTierDefinition":   {
      "description": "An artificial construct of our own creation, to try and put some order on top of Medals and keep them from being one giant, unmanageable and unsorted blob of stats.\r\nUnfortunately, we haven't had time to do this evaluation yet in Destiny 2, so we're short on Medal Tiers. This will hopefully be updated over time, if Medals continue to exist.",
      "type": "object",
      "properties": {
          "tierName": {
              "description": "The name of the tier.",
              "type": "string"
          },
          "order": {
              "format": "int32",
              "description": "If you're rendering medals by tier, render them in this order (ascending)",
              "type": "integer"
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
      "x-mobile-manifest-name": "MedalTiers"
  }
}
```
