# Links.HyperlinkReference

## Entity Information
- **Entity Name**: Links.HyperlinkReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for hyperlinkreference operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| title | string |  | No |
| url | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Links.HyperlinkReference object
const example = {
  title: "example value",
  url: "example value",
};
```

### Python
```python
# Example Links.HyperlinkReference object
example = {
    "title": "example value",
    "url": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Links.HyperlinkReference":   {
      "type": "object",
      "properties": {
          "title": {
              "type": "string"
          },
          "url": {
              "type": "string"
          }
      }
  }
}
```
