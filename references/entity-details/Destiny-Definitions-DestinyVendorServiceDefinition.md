# Destiny.Definitions.DestinyVendorServiceDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorServiceDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
When a vendor provides services, this is the localized name of those services.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string | The localized name of a service provided. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorServiceDefinition object
const example = {
  name: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorServiceDefinition object
example = {
    "name": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorServiceDefinition":   {
      "description": "When a vendor provides services, this is the localized name of those services.",
      "type": "object",
      "properties": {
          "name": {
              "description": "The localized name of a service provided.",
              "type": "string"
          }
      }
  }
}
```
