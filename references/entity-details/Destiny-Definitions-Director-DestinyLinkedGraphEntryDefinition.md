# Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinylinkedgraphentrydefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityGraphHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition object
const example = {
  activityGraphHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition object
example = {
    "activityGraphHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition":   {
      "type": "object",
      "properties": {
          "activityGraphHash": {
              "format": "uint32",
              "type": "integer"
          }
      }
  }
}
```
