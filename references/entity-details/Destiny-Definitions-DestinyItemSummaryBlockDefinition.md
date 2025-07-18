# Destiny.Definitions.DestinyItemSummaryBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSummaryBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This appears to be information used when rendering rewards. We don't currently use it on BNet.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| sortPriority | integer (int32) | Apparently when rendering an item in a reward, this should be used as a sort priority. We're not doing it presently. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSummaryBlockDefinition object
const example = {
  sortPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSummaryBlockDefinition object
example = {
    "sortPriority": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSummaryBlockDefinition":   {
      "description": "This appears to be information used when rendering rewards. We don't currently use it on BNet.",
      "type": "object",
      "properties": {
          "sortPriority": {
              "format": "int32",
              "description": "Apparently when rendering an item in a reward, this should be used as a sort priority. We're not doing it presently.",
              "type": "integer"
          }
      }
  }
}
```
