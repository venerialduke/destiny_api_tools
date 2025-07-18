# FireteamFinder.DestinyFireteamFinderApplicantSet

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderApplicantSet
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderapplicantset data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| applicants | Array[FireteamFinder.DestinyFireteamFinderApplicant] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderApplicantSet object
const example = {
  applicants: [],
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderApplicantSet object
example = {
    "applicants": [],
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderApplicant**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderApplicantSet":   {
      "type": "object",
      "properties": {
          "applicants": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderApplicant"
              }
          }
      }
  }
}
```
