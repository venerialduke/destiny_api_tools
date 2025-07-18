# Destiny.Definitions.Seasons.DestinySeasonPassReference

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinySeasonPassReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines the hash, unlock flag and start time of season passes

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| seasonPassHash | integer (uint32) | The Season Pass Hash | No |
| seasonPassStartDate | string (date-time) | The Season Pass Start Date | No |
| seasonPassEndDate | string (date-time) | The Season Pass End Date | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinySeasonPassReference object
const example = {
  seasonPassHash: 123,
  seasonPassStartDate: "example value",
  seasonPassEndDate: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinySeasonPassReference object
example = {
    "seasonPassHash": 123,
    "seasonPassStartDate": "example value",
    "seasonPassEndDate": "example value",
}
```

## Related Entities
- **Destiny.Definitions.Seasons.DestinySeasonPassDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinySeasonPassReference":   {
      "description": "Defines the hash, unlock flag and start time of season passes",
      "type": "object",
      "properties": {
          "seasonPassHash": {
              "format": "uint32",
              "description": "The Season Pass Hash",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPassDefinition"
              }
          },
          "seasonPassStartDate": {
              "format": "date-time",
              "description": "The Season Pass Start Date",
              "type": "string"
          },
          "seasonPassEndDate": {
              "format": "date-time",
              "description": "The Season Pass End Date",
              "type": "string"
          }
      }
  }
}
```
