# Trending.TrendingEntryDestinyActivity

## Entity Information
- **Entity Name**: Trending.TrendingEntryDestinyActivity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing trendingentrydestinyactivity data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) |  | No |
| status | Destiny.Activities.DestinyPublicActivityStatus |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntryDestinyActivity object
const example = {
  activityHash: 123,
  status: null,
};
```

### Python
```python
# Example Trending.TrendingEntryDestinyActivity object
example = {
    "activityHash": 123,
    "status": None,
}
```

## Related Entities
- **Destiny.Activities.DestinyPublicActivityStatus**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Trending.TrendingEntryDestinyActivity":   {
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "type": "integer"
          },
          "status": {
              "$ref": "#/definitions/Destiny.Activities.DestinyPublicActivityStatus"
          }
      }
  }
}
```
