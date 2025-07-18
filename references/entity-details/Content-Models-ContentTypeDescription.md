# Content.Models.ContentTypeDescription

## Entity Information
- **Entity Name**: Content.Models.ContentTypeDescription
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contenttypedescription operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| cType | string |  | No |
| name | string |  | No |
| contentDescription | string |  | No |
| previewImage | string |  | No |
| priority | integer (int32) |  | No |
| reminder | string |  | No |
| properties | Array[Content.Models.ContentTypeProperty] |  | No |
| tagMetadata | Array[Content.Models.TagMetadataDefinition] |  | No |
| tagMetadataItems | object |  | No |
| usageExamples | Array[string] |  | No |
| showInContentEditor | boolean |  | No |
| typeOf | string |  | No |
| bindIdentifierToProperty | string |  | No |
| boundRegex | string |  | No |
| forceIdentifierBinding | boolean |  | No |
| allowComments | boolean |  | No |
| autoEnglishPropertyFallback | boolean |  | No |
| bulkUploadable | boolean |  | No |
| previews | Array[Content.Models.ContentPreview] |  | No |
| suppressCmsPath | boolean |  | No |
| propertySections | Array[Content.Models.ContentTypePropertySection] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.ContentTypeDescription object
const example = {
  cType: "example value",
  name: "example value",
  contentDescription: "example value",
  previewImage: "example value",
  priority: 123,
  // ... more properties
};
```

### Python
```python
# Example Content.Models.ContentTypeDescription object
example = {
    "cType": "example value",
    "name": "example value",
    "contentDescription": "example value",
    "previewImage": "example value",
    "priority": 123,
    # ... more properties
}
```

## Related Entities
- **Content.Models.ContentPreview**: Referenced in this entity
- **Content.Models.ContentTypeProperty**: Referenced in this entity
- **Content.Models.ContentTypePropertySection**: Referenced in this entity
- **Content.Models.TagMetadataDefinition**: Referenced in this entity
- **Content.Models.TagMetadataItem**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.ContentTypeDescription":   {
      "type": "object",
      "properties": {
          "cType": {
              "type": "string"
          },
          "name": {
              "type": "string"
          },
          "contentDescription": {
              "type": "string"
          },
          "previewImage": {
              "type": "string"
          },
          "priority": {
              "format": "int32",
              "type": "integer"
          },
          "reminder": {
              "type": "string"
          },
          "properties": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.ContentTypeProperty"
              }
          },
          "tagMetadata": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.TagMetadataDefinition"
              }
          },
          "tagMetadataItems": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Content.Models.TagMetadataItem"
              }
          },
          "usageExamples": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "showInContentEditor": {
              "type": "boolean"
          },
          "typeOf": {
              "type": "string"
          },
          "bindIdentifierToProperty": {
              "type": "string"
          },
          "boundRegex": {
              "type": "string"
          },
          "forceIdentifierBinding": {
              "type": "boolean"
          },
          "allowComments": {
              "type": "boolean"
          },
          "autoEnglishPropertyFallback": {
              "type": "boolean"
          },
          "bulkUploadable": {
              "type": "boolean"
          },
          "previews": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.ContentPreview"
              }
          },
          "suppressCmsPath": {
              "type": "boolean"
          },
          "propertySections": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.ContentTypePropertySection"
              }
          }
      }
  }
}
```
