# Destiny.DestinyUnlockStatus

## Entity Information
- **Entity Name**: Destiny.DestinyUnlockStatus
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Indicates the status of an "Unlock Flag" on a Character or Profile.
These are individual bits of state that can be either set or not set, and sometimes provide interesting human-readable information in their related DestinyUnlockDefinition.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| unlockHash | integer (uint32) | The hash identifier for the Unlock Flag. Use to lookup DestinyUnlockDefinition for static data. Not all unlocks have human readable data - in fact, most don't. But when they do, it can be very useful to show. Even if they don't have human readable data, you might be able to infer the meaning of an unlock flag with a bit of experimentation... | No |
| isSet | boolean | Whether the unlock flag is set. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyUnlockStatus object
const example = {
  unlockHash: 123,
  isSet: true,
};
```

### Python
```python
# Example Destiny.DestinyUnlockStatus object
example = {
    "unlockHash": 123,
    "isSet": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyUnlockDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyUnlockStatus":   {
      "description": "Indicates the status of an \"Unlock Flag\" on a Character or Profile.\r\nThese are individual bits of state that can be either set or not set, and sometimes provide interesting human-readable information in their related DestinyUnlockDefinition.",
      "type": "object",
      "properties": {
          "unlockHash": {
              "format": "uint32",
              "description": "The hash identifier for the Unlock Flag. Use to lookup DestinyUnlockDefinition for static data. Not all unlocks have human readable data - in fact, most don't. But when they do, it can be very useful to show. Even if they don't have human readable data, you might be able to infer the meaning of an unlock flag with a bit of experimentation...",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyUnlockDefinition"
              }
          },
          "isSet": {
              "description": "Whether the unlock flag is set.",
              "type": "boolean"
          }
      }
  }
}
```
