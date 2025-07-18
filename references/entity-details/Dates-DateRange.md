# Dates.DateRange

## Entity Information
- **Entity Name**: Dates.DateRange
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for daterange operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| start | string (date-time) |  | No |
| end | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Dates.DateRange object
const example = {
  start: "example value",
  end: "example value",
};
```

### Python
```python
# Example Dates.DateRange object
example = {
    "start": "example value",
    "end": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Dates.DateRange":   {
      "type": "object",
      "properties": {
          "start": {
              "format": "date-time",
              "type": "string"
          },
          "end": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
