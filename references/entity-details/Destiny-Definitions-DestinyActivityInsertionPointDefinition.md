# Destiny.Definitions.DestinyActivityInsertionPointDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityInsertionPointDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A point of entry into an activity, gated by an unlock flag and with some more-or-less useless (for our purposes) phase information. I'm including it in case we end up being able to bolt more useful information onto it in the future.
UPDATE: Turns out this information isn't actually useless, and is in fact actually useful for people. Who would have thought? We still don't have localized info for it, but at least this will help people when they're looking at phase indexes in stats data, or when they want to know what phases have been completed on a weekly achievement.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| phaseHash | integer (uint32) | A unique hash value representing the phase. This can be useful for, for example, comparing how different instances of Raids have phases in different orders! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityInsertionPointDefinition object
const example = {
  phaseHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityInsertionPointDefinition object
example = {
    "phaseHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityInsertionPointDefinition":   {
      "description": "A point of entry into an activity, gated by an unlock flag and with some more-or-less useless (for our purposes) phase information. I'm including it in case we end up being able to bolt more useful information onto it in the future.\r\nUPDATE: Turns out this information isn't actually useless, and is in fact actually useful for people. Who would have thought? We still don't have localized info for it, but at least this will help people when they're looking at phase indexes in stats data, or when they want to know what phases have been completed on a weekly achievement.",
      "type": "object",
      "properties": {
          "phaseHash": {
              "format": "uint32",
              "description": "A unique hash value representing the phase. This can be useful for, for example, comparing how different instances of Raids have phases in different orders!",
              "type": "integer"
          }
      }
  }
}
```
