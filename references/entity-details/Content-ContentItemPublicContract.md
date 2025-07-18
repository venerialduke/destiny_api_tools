# Content.ContentItemPublicContract

## Entity Information
- **Entity Name**: Content.ContentItemPublicContract
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contentitempubliccontract operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| contentId | integer (int64) |  | No |
| cType | string |  | No |
| cmsPath | string |  | No |
| creationDate | string (date-time) |  | No |
| modifyDate | string (date-time) |  | No |
| allowComments | boolean |  | No |
| hasAgeGate | boolean |  | No |
| minimumAge | integer (int32) |  | No |
| ratingImagePath | string |  | No |
| author | User.GeneralUser |  | No |
| autoEnglishPropertyFallback | boolean |  | No |
| properties | object | Firehose content is really a collection of metadata and "properties", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.
As Cole Porter would have crooned, "Anything Goes" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized. | No |
| representations | Array[Content.ContentRepresentation] |  | No |
| tags | Array[string] | NOTE: Tags will always be lower case. | No |
| commentSummary | Content.CommentSummary |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.ContentItemPublicContract object
const example = {
  contentId: 123,
  cType: "example value",
  cmsPath: "example value",
  creationDate: "example value",
  modifyDate: "example value",
  // ... more properties
};
```

### Python
```python
# Example Content.ContentItemPublicContract object
example = {
    "contentId": 123,
    "cType": "example value",
    "cmsPath": "example value",
    "creationDate": "example value",
    "modifyDate": "example value",
    # ... more properties
}
```

## Related Entities
- **Content.CommentSummary**: Referenced in this entity
- **Content.ContentRepresentation**: Referenced in this entity
- **User.GeneralUser**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.ContentItemPublicContract":   {
      "type": "object",
      "properties": {
          "contentId": {
              "format": "int64",
              "type": "integer"
          },
          "cType": {
              "type": "string"
          },
          "cmsPath": {
              "type": "string"
          },
          "creationDate": {
              "format": "date-time",
              "type": "string"
          },
          "modifyDate": {
              "format": "date-time",
              "type": "string"
          },
          "allowComments": {
              "type": "boolean"
          },
          "hasAgeGate": {
              "type": "boolean"
          },
          "minimumAge": {
              "format": "int32",
              "type": "integer"
          },
          "ratingImagePath": {
              "type": "string"
          },
          "author": {
              "$ref": "#/definitions/User.GeneralUser"
          },
          "autoEnglishPropertyFallback": {
              "type": "boolean"
          },
          "properties": {
              "description": "Firehose content is really a collection of metadata and \"properties\", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.\r\nAs Cole Porter would have crooned, \"Anything Goes\" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized.",
              "type": "object",
              "additionalProperties": {
                  "type": "object"
              }
          },
          "representations": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.ContentRepresentation"
              }
          },
          "tags": {
              "description": "NOTE: Tags will always be lower case.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "commentSummary": {
              "$ref": "#/definitions/Content.CommentSummary"
          }
      }
  }
}
```
