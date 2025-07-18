# Destiny.Definitions.DestinyEntitySearchResult

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyEntitySearchResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| suggestedWords | Array[string] | A list of suggested words that might make for better search results, based on the text searched for. | No |
| results | object | The items found that are matches/near matches for the searched-for term, sorted by something vaguely resembling "relevance". Hopefully this will get better in the future. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyEntitySearchResult object
const example = {
  suggestedWords: [],
  results: null,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyEntitySearchResult object
example = {
    "suggestedWords": [],
    "results": None,
}
```

## Related Entities
- **SearchResultOfDestinyEntitySearchResultItem**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyEntitySearchResult":   {
      "description": "The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.",
      "type": "object",
      "properties": {
          "suggestedWords": {
              "description": "A list of suggested words that might make for better search results, based on the text searched for.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "results": {
              "description": "The items found that are matches/near matches for the searched-for term, sorted by something vaguely resembling \"relevance\". Hopefully this will get better in the future.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SearchResultOfDestinyEntitySearchResultItem"
                  }
              ]
          }
      }
  }
}
```
