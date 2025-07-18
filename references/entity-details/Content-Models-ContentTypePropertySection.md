# Content.Models.ContentTypePropertySection

## Entity Information
- **Entity Name**: Content.Models.ContentTypePropertySection
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contenttypepropertysection operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| readableName | string |  | No |
| collapsed | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.ContentTypePropertySection object
const example = {
  name: "example value",
  readableName: "example value",
  collapsed: true,
};
```

### Python
```python
# Example Content.Models.ContentTypePropertySection object
example = {
    "name": "example value",
    "readableName": "example value",
    "collapsed": True,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.ContentTypePropertySection":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "readableName": {
              "type": "string"
          },
          "collapsed": {
              "type": "boolean"
          }
      }
  }
}
```
