# FireteamFinder.DestinyFireteamFinderApplication

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderApplication
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderapplication data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| applicationId | integer (int64) |  | No |
| revision | integer (int32) |  | No |
| state | integer (int32) |  | No |
| submitterId | FireteamFinder.DestinyFireteamFinderPlayerId |  | No |
| referralToken | integer (int64) |  | No |
| applicantSet | FireteamFinder.DestinyFireteamFinderApplicantSet |  | No |
| applicationType | integer (int32) |  | No |
| listingId | integer (int64) |  | No |
| createdDateTime | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderApplication object
const example = {
  applicationId: 123,
  revision: 123,
  state: 123,
  submitterId: null,
  referralToken: 123,
  // ... more properties
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderApplication object
example = {
    "applicationId": 123,
    "revision": 123,
    "state": 123,
    "submitterId": None,
    "referralToken": 123,
    # ... more properties
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderApplicantSet**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderApplicationState**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderApplicationType**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderPlayerId**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderApplication":   {
      "type": "object",
      "properties": {
          "applicationId": {
              "format": "int64",
              "type": "integer"
          },
          "revision": {
              "format": "int32",
              "type": "integer"
          },
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderApplicationState"
              }
          },
          "submitterId": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderPlayerId"
          },
          "referralToken": {
              "format": "int64",
              "type": "integer"
          },
          "applicantSet": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderApplicantSet"
          },
          "applicationType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderApplicationType"
              }
          },
          "listingId": {
              "format": "int64",
              "type": "integer"
          },
          "createdDateTime": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
