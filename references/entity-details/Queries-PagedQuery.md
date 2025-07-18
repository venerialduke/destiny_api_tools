# Queries.PagedQuery

## Entity Information
- **Entity Name**: Queries.PagedQuery
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for pagedquery operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemsPerPage | integer (int32) |  | No |
| currentPage | integer (int32) |  | No |
| requestContinuationToken | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Queries.PagedQuery object
const example = {
  itemsPerPage: 123,
  currentPage: 123,
  requestContinuationToken: "example value",
};
```

### Python
```python
# Example Queries.PagedQuery object
example = {
    "itemsPerPage": 123,
    "currentPage": 123,
    "requestContinuationToken": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Queries.PagedQuery":   {
      "type": "object",
      "properties": {
          "itemsPerPage": {
              "format": "int32",
              "type": "integer"
          },
          "currentPage": {
              "format": "int32",
              "type": "integer"
          },
          "requestContinuationToken": {
              "type": "string"
          }
      }
  }
}
```
