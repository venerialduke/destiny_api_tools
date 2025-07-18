# FireteamFinder.DestinyFireteamFinderRespondToApplicationResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderRespondToApplicationResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderrespondtoapplicationresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| applicationId | integer (int64) |  | No |
| applicationRevision | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderRespondToApplicationResponse object
const example = {
  applicationId: 123,
  applicationRevision: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderRespondToApplicationResponse object
example = {
    "applicationId": 123,
    "applicationRevision": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderRespondToApplicationResponse":   {
      "type": "object",
      "properties": {
          "applicationId": {
              "format": "int64",
              "type": "integer"
          },
          "applicationRevision": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
