# Content.Models.ContentTypeProperty

## Entity Information
- **Entity Name**: Content.Models.ContentTypeProperty
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contenttypeproperty operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| rootPropertyName | string |  | No |
| readableName | string |  | No |
| value | string |  | No |
| propertyDescription | string |  | No |
| localizable | boolean |  | No |
| fallback | boolean |  | No |
| enabled | boolean |  | No |
| order | integer (int32) |  | No |
| visible | boolean |  | No |
| isTitle | boolean |  | No |
| required | boolean |  | No |
| maxLength | integer (int32) |  | No |
| maxByteLength | integer (int32) |  | No |
| maxFileSize | integer (int32) |  | No |
| regexp | string |  | No |
| validateAs | string |  | No |
| rssAttribute | string |  | No |
| visibleDependency | string |  | No |
| visibleOn | string |  | No |
| datatype | integer (int32) |  | No |
| attributes | object |  | No |
| childProperties | Array[Content.Models.ContentTypeProperty] |  | No |
| contentTypeAllowed | string |  | No |
| bindToProperty | string |  | No |
| boundRegex | string |  | No |
| representationSelection | object |  | No |
| defaultValues | Array[Content.Models.ContentTypeDefaultValue] |  | No |
| isExternalAllowed | boolean |  | No |
| propertySection | string |  | No |
| weight | integer (int32) |  | No |
| entitytype | string |  | No |
| isCombo | boolean |  | No |
| suppressProperty | boolean |  | No |
| legalContentTypes | Array[string] |  | No |
| representationValidationString | string |  | No |
| minWidth | integer (int32) |  | No |
| maxWidth | integer (int32) |  | No |
| minHeight | integer (int32) |  | No |
| maxHeight | integer (int32) |  | No |
| isVideo | boolean |  | No |
| isImage | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.ContentTypeProperty object
const example = {
  name: "example value",
  rootPropertyName: "example value",
  readableName: "example value",
  value: "example value",
  propertyDescription: "example value",
  // ... more properties
};
```

### Python
```python
# Example Content.Models.ContentTypeProperty object
example = {
    "name": "example value",
    "rootPropertyName": "example value",
    "readableName": "example value",
    "value": "example value",
    "propertyDescription": "example value",
    # ... more properties
}
```

## Related Entities
- **Content.Models.ContentPropertyDataTypeEnum**: Referenced in this entity
- **Content.Models.ContentTypeDefaultValue**: Referenced in this entity
- **Content.Models.ContentTypeProperty**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.ContentTypeProperty":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "rootPropertyName": {
              "type": "string"
          },
          "readableName": {
              "type": "string"
          },
          "value": {
              "type": "string"
          },
          "propertyDescription": {
              "type": "string"
          },
          "localizable": {
              "type": "boolean"
          },
          "fallback": {
              "type": "boolean"
          },
          "enabled": {
              "type": "boolean"
          },
          "order": {
              "format": "int32",
              "type": "integer"
          },
          "visible": {
              "type": "boolean"
          },
          "isTitle": {
              "type": "boolean"
          },
          "required": {
              "type": "boolean"
          },
          "maxLength": {
              "format": "int32",
              "type": "integer"
          },
          "maxByteLength": {
              "format": "int32",
              "type": "integer"
          },
          "maxFileSize": {
              "format": "int32",
              "type": "integer"
          },
          "regexp": {
              "type": "string"
          },
          "validateAs": {
              "type": "string"
          },
          "rssAttribute": {
              "type": "string"
          },
          "visibleDependency": {
              "type": "string"
          },
          "visibleOn": {
              "type": "string"
          },
          "datatype": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Content.Models.ContentPropertyDataTypeEnum"
              }
          },
          "attributes": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "childProperties": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.ContentTypeProperty"
              }
          },
          "contentTypeAllowed": {
              "type": "string"
          },
          "bindToProperty": {
              "type": "string"
          },
          "boundRegex": {
              "type": "string"
          },
          "representationSelection": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "defaultValues": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.ContentTypeDefaultValue"
              }
          },
          "isExternalAllowed": {
              "type": "boolean"
          },
          "propertySection": {
              "type": "string"
          },
          "weight": {
              "format": "int32",
              "type": "integer"
          },
          "entitytype": {
              "type": "string"
          },
          "isCombo": {
              "type": "boolean"
          },
          "suppressProperty": {
              "type": "boolean"
          },
          "legalContentTypes": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "representationValidationString": {
              "type": "string"
          },
          "minWidth": {
              "format": "int32",
              "type": "integer"
          },
          "maxWidth": {
              "format": "int32",
              "type": "integer"
          },
          "minHeight": {
              "format": "int32",
              "type": "integer"
          },
          "maxHeight": {
              "format": "int32",
              "type": "integer"
          },
          "isVideo": {
              "type": "boolean"
          },
          "isImage": {
              "type": "boolean"
          }
      }
  }
}
```
