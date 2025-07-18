# Destiny.Config.GearAssetDataBaseDefinition

## Entity Information
- **Entity Name**: Destiny.Config.GearAssetDataBaseDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing gearassetdatabasedefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| version | integer (int32) |  | No |
| path | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Config.GearAssetDataBaseDefinition object
const example = {
  version: 123,
  path: "example value",
};
```

### Python
```python
# Example Destiny.Config.GearAssetDataBaseDefinition object
example = {
    "version": 123,
    "path": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Config.GearAssetDataBaseDefinition":   {
      "type": "object",
      "properties": {
          "version": {
              "format": "int32",
              "type": "integer"
          },
          "path": {
              "type": "string"
          }
      }
  }
}
```
