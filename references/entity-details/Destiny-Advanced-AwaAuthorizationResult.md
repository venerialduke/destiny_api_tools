# Destiny.Advanced.AwaAuthorizationResult

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaAuthorizationResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing awaauthorizationresult data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| userSelection | integer (int32) | Indication of how the user responded to the request. If the value is "Approved" the actionToken will contain the token that can be presented when performing the advanced write action. | No |
| responseReason | integer (int32) |  | No |
| developerNote | string | Message to the app developer to help understand the response. | No |
| actionToken | string | Credential used to prove the user authorized an advanced write action. | No |
| maximumNumberOfUses | integer (int32) | This token may be used to perform the requested action this number of times, at a maximum. If this value is 0, then there is no limit. | No |
| validUntil | string (date-time) | Time, UTC, when token expires. | No |
| type | integer (int32) | Advanced Write Action Type from the permission request. | No |
| membershipType | integer (int32) | MembershipType from the permission request. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Advanced.AwaAuthorizationResult object
const example = {
  userSelection: 123,
  responseReason: 123,
  developerNote: "example value",
  actionToken: "example value",
  maximumNumberOfUses: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Advanced.AwaAuthorizationResult object
example = {
    "userSelection": 123,
    "responseReason": 123,
    "developerNote": "example value",
    "actionToken": "example value",
    "maximumNumberOfUses": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Advanced.AwaResponseReason**: Referenced in this entity
- **Destiny.Advanced.AwaType**: Referenced in this entity
- **Destiny.Advanced.AwaUserSelection**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaAuthorizationResult":   {
      "type": "object",
      "properties": {
          "userSelection": {
              "format": "int32",
              "description": "Indication of how the user responded to the request. If the value is \"Approved\" the actionToken will contain the token that can be presented when performing the advanced write action.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Advanced.AwaUserSelection"
              }
          },
          "responseReason": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Advanced.AwaResponseReason"
              }
          },
          "developerNote": {
              "description": "Message to the app developer to help understand the response.",
              "type": "string"
          },
          "actionToken": {
              "description": "Credential used to prove the user authorized an advanced write action.",
              "type": "string"
          },
          "maximumNumberOfUses": {
              "format": "int32",
              "description": "This token may be used to perform the requested action this number of times, at a maximum. If this value is 0, then there is no limit.",
              "type": "integer"
          },
          "validUntil": {
              "format": "date-time",
              "description": "Time, UTC, when token expires.",
              "type": "string"
          },
          "type": {
              "format": "int32",
              "description": "Advanced Write Action Type from the permission request.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Advanced.AwaType"
              }
          },
          "membershipType": {
              "format": "int32",
              "description": "MembershipType from the permission request.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          }
      }
  }
}
```
