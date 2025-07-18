# Destiny.Config.DestinyManifest

## Entity Information
- **Entity Name**: Destiny.Config.DestinyManifest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| version | string |  | No |
| mobileAssetContentPath | string |  | No |
| mobileGearAssetDataBases | Array[Destiny.Config.GearAssetDataBaseDefinition] |  | No |
| mobileWorldContentPaths | object |  | No |
| jsonWorldContentPaths | object | This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!) | No |
| jsonWorldComponentContentPaths | object | This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term. | No |
| mobileClanBannerDatabasePath | string |  | No |
| mobileGearCDN | object |  | No |
| iconImagePyramidInfo | Array[Destiny.Config.ImagePyramidEntry] | Information about the "Image Pyramid" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the "original/full size" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Config.DestinyManifest object
const example = {
  version: "example value",
  mobileAssetContentPath: "example value",
  mobileGearAssetDataBases: [],
  mobileWorldContentPaths: null,
  jsonWorldContentPaths: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Config.DestinyManifest object
example = {
    "version": "example value",
    "mobileAssetContentPath": "example value",
    "mobileGearAssetDataBases": [],
    "mobileWorldContentPaths": None,
    "jsonWorldContentPaths": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.Config.GearAssetDataBaseDefinition**: Referenced in this entity
- **Destiny.Config.ImagePyramidEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Config.DestinyManifest":   {
      "description": "DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.",
      "type": "object",
      "properties": {
          "version": {
              "type": "string"
          },
          "mobileAssetContentPath": {
              "type": "string"
          },
          "mobileGearAssetDataBases": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Config.GearAssetDataBaseDefinition"
              }
          },
          "mobileWorldContentPaths": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "jsonWorldContentPaths": {
              "description": "This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!)",
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "jsonWorldComponentContentPaths": {
              "description": "This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term.",
              "type": "object",
              "additionalProperties": {
                  "type": "object",
                  "additionalProperties": {
                      "type": "string"
                  }
              }
          },
          "mobileClanBannerDatabasePath": {
              "type": "string"
          },
          "mobileGearCDN": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "iconImagePyramidInfo": {
              "description": "Information about the \"Image Pyramid\" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the \"original/full size\" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable)",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Config.ImagePyramidEntry"
              }
          }
      }
  }
}
```
