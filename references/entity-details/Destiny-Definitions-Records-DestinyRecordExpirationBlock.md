# Destiny.Definitions.Records.DestinyRecordExpirationBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordExpirationBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If this record has an expiration after which it cannot be earned, this is some information about that expiration.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| hasExpiration | boolean |  | No |
| description | string |  | No |
| icon | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.DestinyRecordExpirationBlock object
const example = {
  hasExpiration: true,
  description: "example value",
  icon: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordExpirationBlock object
example = {
    "hasExpiration": True,
    "description": "example value",
    "icon": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordExpirationBlock":   {
      "description": "If this record has an expiration after which it cannot be earned, this is some information about that expiration.",
      "type": "object",
      "properties": {
          "hasExpiration": {
              "type": "boolean"
          },
          "description": {
              "type": "string"
          },
          "icon": {
              "type": "string"
          }
      }
  }
}
```
