# Fireteam.FireteamResponse

## Entity Information
- **Entity Name**: Fireteam.FireteamResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for fireteamresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| Summary | Fireteam.FireteamSummary |  | No |
| Members | Array[Fireteam.FireteamMember] |  | No |
| Alternates | Array[Fireteam.FireteamMember] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Fireteam.FireteamResponse object
const example = {
  Summary: null,
  Members: [],
  Alternates: [],
};
```

### Python
```python
# Example Fireteam.FireteamResponse object
example = {
    "Summary": None,
    "Members": [],
    "Alternates": [],
}
```

## Related Entities
- **Fireteam.FireteamMember**: Referenced in this entity
- **Fireteam.FireteamSummary**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Fireteam.FireteamResponse":   {
      "type": "object",
      "properties": {
          "Summary": {
              "$ref": "#/definitions/Fireteam.FireteamSummary"
          },
          "Members": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Fireteam.FireteamMember"
              }
          },
          "Alternates": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Fireteam.FireteamMember"
              }
          }
      }
  }
}
```
