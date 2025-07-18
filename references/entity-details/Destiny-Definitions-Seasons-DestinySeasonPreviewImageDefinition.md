# Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines the thumbnail icon, high-res image, and video link for promotional images

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| thumbnailImage | string | A thumbnail icon path to preview seasonal content, probably 480x270. | No |
| highResImage | string | An optional path to a high-resolution image, probably 1920x1080. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition object
const example = {
  thumbnailImage: "example value",
  highResImage: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition object
example = {
    "thumbnailImage": "example value",
    "highResImage": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition":   {
      "description": "Defines the thumbnail icon, high-res image, and video link for promotional images",
      "type": "object",
      "properties": {
          "thumbnailImage": {
              "description": "A thumbnail icon path to preview seasonal content, probably 480x270.",
              "type": "string"
          },
          "highResImage": {
              "description": "An optional path to a high-resolution image, probably 1920x1080.",
              "type": "string"
          }
      }
  }
}
```
