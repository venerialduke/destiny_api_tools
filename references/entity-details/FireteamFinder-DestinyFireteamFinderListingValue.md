# FireteamFinder.DestinyFireteamFinderListingValue

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderListingValue
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlistingvalue data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| valueType | integer (uint32) |  | No |
| values | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderListingValue object
const example = {
  valueType: 123,
  values: [],
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderListingValue object
example = {
    "valueType": 123,
    "values": [],
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderListingValue":   {
      "type": "object",
      "properties": {
          "valueType": {
              "format": "uint32",
              "type": "integer"
          },
          "values": {
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
