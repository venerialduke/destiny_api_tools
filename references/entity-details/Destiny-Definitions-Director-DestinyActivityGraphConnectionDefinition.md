# Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Nodes on a graph can be visually connected: this appears to be the information about which nodes to link. It appears to lack more detailed information, such as the path for that linking.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| sourceNodeHash | integer (uint32) |  | No |
| destNodeHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition object
const example = {
  sourceNodeHash: 123,
  destNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition object
example = {
    "sourceNodeHash": 123,
    "destNodeHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition":   {
      "description": "Nodes on a graph can be visually connected: this appears to be the information about which nodes to link. It appears to lack more detailed information, such as the path for that linking.",
      "type": "object",
      "properties": {
          "sourceNodeHash": {
              "format": "uint32",
              "type": "integer"
          },
          "destNodeHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
