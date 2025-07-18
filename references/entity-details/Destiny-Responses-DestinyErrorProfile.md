# Destiny.Responses.DestinyErrorProfile

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyErrorProfile
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If a Destiny Profile can't be returned, but we're pretty certain it's a valid Destiny account, this will contain as much info as we can get about the profile for your use.
Assume that the most you'll get is the Error Code, the Membership Type and the Membership ID.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| errorCode | integer (int32) | The error that we encountered. You should be able to look up localized text to show to the user for these failures. | No |
| infoCard | object | Basic info about the account that failed. Don't expect anything other than membership ID, Membership Type, and displayName to be populated. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyErrorProfile object
const example = {
  errorCode: 123,
  infoCard: null,
};
```

### Python
```python
# Example Destiny.Responses.DestinyErrorProfile object
example = {
    "errorCode": 123,
    "infoCard": None,
}
```

## Related Entities
- **Exceptions.PlatformErrorCodes**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyErrorProfile":   {
      "description": "If a Destiny Profile can't be returned, but we're pretty certain it's a valid Destiny account, this will contain as much info as we can get about the profile for your use.\r\nAssume that the most you'll get is the Error Code, the Membership Type and the Membership ID.",
      "type": "object",
      "properties": {
          "errorCode": {
              "format": "int32",
              "description": "The error that we encountered. You should be able to look up localized text to show to the user for these failures.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Exceptions.PlatformErrorCodes"
              }
          },
          "infoCard": {
              "description": "Basic info about the account that failed. Don't expect anything other than membership ID, Membership Type, and displayName to be populated.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/User.UserInfoCard"
                  }
              ]
          }
      }
  }
}
```
