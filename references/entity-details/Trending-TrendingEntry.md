# Trending.TrendingEntry

## Entity Information
- **Entity Name**: Trending.TrendingEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The list entry view for trending items. Returns just enough to show the item on the trending page.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| weight | number (double) | The weighted score of this trending item. | No |
| isFeatured | boolean |  | No |
| identifier | string | We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type. | No |
| entityType | integer (int32) | An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item. | No |
| displayName | string | The localized "display name/article title/'primary localized identifier'" of the entity. | No |
| tagline | string | If the entity has a localized tagline/subtitle/motto/whatever, that is found here. | No |
| image | string |  | No |
| startDate | string (date-time) |  | No |
| endDate | string (date-time) |  | No |
| link | string |  | No |
| webmVideo | string | If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo | No |
| mp4Video | string | If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo | No |
| featureImage | string | If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time. | No |
| items | Array[Trending.TrendingEntry] | If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header. | No |
| creationDate | string (date-time) | If the entry has a date at which it was created, this is that date. | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntry object
const example = {
  weight: 123.45,
  isFeatured: true,
  identifier: "example value",
  entityType: 123,
  displayName: "example value",
  // ... more properties
};
```

### Python
```python
# Example Trending.TrendingEntry object
example = {
    "weight": 123.45,
    "isFeatured": True,
    "identifier": "example value",
    "entityType": 123,
    "displayName": "example value",
    # ... more properties
}
```

## Related Entities
- **Trending.TrendingEntry**: Referenced in this entity
- **Trending.TrendingEntryType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Trending.TrendingEntry":   {
      "description": "The list entry view for trending items. Returns just enough to show the item on the trending page.",
      "type": "object",
      "properties": {
          "weight": {
              "format": "double",
              "description": "The weighted score of this trending item.",
              "type": "number"
          },
          "isFeatured": {
              "type": "boolean"
          },
          "identifier": {
              "description": "We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.",
              "type": "string"
          },
          "entityType": {
              "format": "int32",
              "description": "An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Trending.TrendingEntryType"
              }
          },
          "displayName": {
              "description": "The localized \"display name/article title/'primary localized identifier'\" of the entity.",
              "type": "string"
          },
          "tagline": {
              "description": "If the entity has a localized tagline/subtitle/motto/whatever, that is found here.",
              "type": "string"
          },
          "image": {
              "type": "string"
          },
          "startDate": {
              "format": "date-time",
              "type": "string"
          },
          "endDate": {
              "format": "date-time",
              "type": "string"
          },
          "link": {
              "type": "string"
          },
          "webmVideo": {
              "description": "If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo",
              "type": "string"
          },
          "mp4Video": {
              "description": "If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo",
              "type": "string"
          },
          "featureImage": {
              "description": "If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.",
              "type": "string"
          },
          "items": {
              "description": "If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Trending.TrendingEntry"
              }
          },
          "creationDate": {
              "format": "date-time",
              "description": "If the entry has a date at which it was created, this is that date.",
              "type": "string"
          }
      }
  }
}
```
