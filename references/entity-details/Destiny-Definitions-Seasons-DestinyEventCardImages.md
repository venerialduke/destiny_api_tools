# Destiny.Definitions.Seasons.DestinyEventCardImages

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinyEventCardImages
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyeventcardimages data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| unownedCardSleeveImagePath | string |  | No |
| unownedCardSleeveWrapImagePath | string |  | No |
| cardIncompleteImagePath | string |  | No |
| cardCompleteImagePath | string |  | No |
| cardCompleteWrapImagePath | string |  | No |
| progressIconImagePath | string |  | No |
| themeBackgroundImagePath | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinyEventCardImages object
const example = {
  unownedCardSleeveImagePath: "example value",
  unownedCardSleeveWrapImagePath: "example value",
  cardIncompleteImagePath: "example value",
  cardCompleteImagePath: "example value",
  cardCompleteWrapImagePath: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinyEventCardImages object
example = {
    "unownedCardSleeveImagePath": "example value",
    "unownedCardSleeveWrapImagePath": "example value",
    "cardIncompleteImagePath": "example value",
    "cardCompleteImagePath": "example value",
    "cardCompleteWrapImagePath": "example value",
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinyEventCardImages":   {
      "type": "object",
      "properties": {
          "unownedCardSleeveImagePath": {
              "type": "string"
          },
          "unownedCardSleeveWrapImagePath": {
              "type": "string"
          },
          "cardIncompleteImagePath": {
              "type": "string"
          },
          "cardCompleteImagePath": {
              "type": "string"
          },
          "cardCompleteWrapImagePath": {
              "type": "string"
          },
          "progressIconImagePath": {
              "type": "string"
          },
          "themeBackgroundImagePath": {
              "type": "string"
          }
      }
  }
}
```
