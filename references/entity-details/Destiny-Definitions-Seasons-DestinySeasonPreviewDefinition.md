# Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines the promotional text, images, and links to preview this season.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| description | string | A localized description of the season. | No |
| linkPath | string | A relative path to learn more about the season. Web browsers should be automatically redirected to the user's Bungie.net locale. For example: "/SeasonOfTheChosen" will redirect to "/7/en/Seasons/SeasonOfTheChosen" for English users. | No |
| videoLink | string | An optional link to a localized video, probably YouTube. | No |
| images | Array[Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition] | A list of images to preview the seasonal content. Should have at least three to show. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition object
const example = {
  description: "example value",
  linkPath: "example value",
  videoLink: "example value",
  images: [],
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition object
example = {
    "description": "example value",
    "linkPath": "example value",
    "videoLink": "example value",
    "images": [],
}
```

## Related Entities
- **Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition":   {
      "description": "Defines the promotional text, images, and links to preview this season.",
      "type": "object",
      "properties": {
          "description": {
              "description": "A localized description of the season.",
              "type": "string"
          },
          "linkPath": {
              "description": "A relative path to learn more about the season. Web browsers should be automatically redirected to the user's Bungie.net locale. For example: \"/SeasonOfTheChosen\" will redirect to \"/7/en/Seasons/SeasonOfTheChosen\" for English users.",
              "type": "string"
          },
          "videoLink": {
              "description": "An optional link to a localized video, probably YouTube.",
              "type": "string"
          },
          "images": {
              "description": "A list of images to preview the seasonal content. Should have at least three to show.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPreviewImageDefinition"
              }
          }
      }
  }
}
```
