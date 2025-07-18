# GroupsV2.ClanBanner

## Entity Information
- **Entity Name**: GroupsV2.ClanBanner
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for clanbanner operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| decalId | integer (uint32) |  | No |
| decalColorId | integer (uint32) |  | No |
| decalBackgroundColorId | integer (uint32) |  | No |
| gonfalonId | integer (uint32) |  | No |
| gonfalonColorId | integer (uint32) |  | No |
| gonfalonDetailId | integer (uint32) |  | No |
| gonfalonDetailColorId | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.ClanBanner object
const example = {
  decalId: 123,
  decalColorId: 123,
  decalBackgroundColorId: 123,
  gonfalonId: 123,
  gonfalonColorId: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.ClanBanner object
example = {
    "decalId": 123,
    "decalColorId": 123,
    "decalBackgroundColorId": 123,
    "gonfalonId": 123,
    "gonfalonColorId": 123,
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.ClanBanner":   {
      "type": "object",
      "properties": {
          "decalId": {
              "format": "uint32",
              "type": "integer"
          },
          "decalColorId": {
              "format": "uint32",
              "type": "integer"
          },
          "decalBackgroundColorId": {
              "format": "uint32",
              "type": "integer"
          },
          "gonfalonId": {
              "format": "uint32",
              "type": "integer"
          },
          "gonfalonColorId": {
              "format": "uint32",
              "type": "integer"
          },
          "gonfalonDetailId": {
              "format": "uint32",
              "type": "integer"
          },
          "gonfalonDetailColorId": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
