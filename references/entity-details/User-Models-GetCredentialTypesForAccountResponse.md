# User.Models.GetCredentialTypesForAccountResponse

## Entity Information
- **Entity Name**: User.Models.GetCredentialTypesForAccountResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for getcredentialtypesforaccountresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| credentialType | integer (byte) |  | No |
| credentialDisplayName | string |  | No |
| isPublic | boolean |  | No |
| credentialAsString | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.Models.GetCredentialTypesForAccountResponse object
const example = {
  credentialType: 123,
  credentialDisplayName: "example value",
  isPublic: true,
  credentialAsString: "example value",
};
```

### Python
```python
# Example User.Models.GetCredentialTypesForAccountResponse object
example = {
    "credentialType": 123,
    "credentialDisplayName": "example value",
    "isPublic": True,
    "credentialAsString": "example value",
}
```

## Related Entities
- **BungieCredentialType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.Models.GetCredentialTypesForAccountResponse":   {
      "type": "object",
      "properties": {
          "credentialType": {
              "format": "byte",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieCredentialType"
              }
          },
          "credentialDisplayName": {
              "type": "string"
          },
          "isPublic": {
              "type": "boolean"
          },
          "credentialAsString": {
              "type": "string"
          }
      }
  }
}
```
