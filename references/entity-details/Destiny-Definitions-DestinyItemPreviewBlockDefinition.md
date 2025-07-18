# Destiny.Definitions.DestinyItemPreviewBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemPreviewBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Items like Sacks or Boxes can have items that it shows in-game when you view details that represent the items you can obtain if you use or acquire the item.
This defines those categories, and gives some insights into that data's source.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| screenStyle | string | A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there's no guarantees of a fixed, known number of these - so fall back to something reasonable if you don't recognize it. | No |
| previewVendorHash | integer (uint32) | If the preview data is derived from a fake "Preview" Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor. | No |
| artifactHash | integer (uint32) | If this item should show you Artifact information when you preview it, this is the hash identifier of the DestinyArtifactDefinition for the artifact whose data should be shown. | No |
| previewActionString | string | If the preview has an associated action (like "Open"), this will be the localized string for that action. | No |
| derivedItemCategories | Array[Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition] | This is a list of the items being previewed, categorized in the same way as they are in the preview UI. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemPreviewBlockDefinition object
const example = {
  screenStyle: "example value",
  previewVendorHash: 123,
  artifactHash: 123,
  previewActionString: "example value",
  derivedItemCategories: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemPreviewBlockDefinition object
example = {
    "screenStyle": "example value",
    "previewVendorHash": 123,
    "artifactHash": 123,
    "previewActionString": "example value",
    "derivedItemCategories": [],
}
```

## Related Entities
- **Destiny.Definitions.Artifacts.DestinyArtifactDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemPreviewBlockDefinition":   {
      "description": "Items like Sacks or Boxes can have items that it shows in-game when you view details that represent the items you can obtain if you use or acquire the item.\r\nThis defines those categories, and gives some insights into that data's source.",
      "type": "object",
      "properties": {
          "screenStyle": {
              "description": "A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there's no guarantees of a fixed, known number of these - so fall back to something reasonable if you don't recognize it.",
              "type": "string"
          },
          "previewVendorHash": {
              "format": "uint32",
              "description": "If the preview data is derived from a fake \"Preview\" Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "artifactHash": {
              "format": "uint32",
              "description": "If this item should show you Artifact information when you preview it, this is the hash identifier of the DestinyArtifactDefinition for the artifact whose data should be shown.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Artifacts.DestinyArtifactDefinition"
              }
          },
          "previewActionString": {
              "description": "If the preview has an associated action (like \"Open\"), this will be the localized string for that action.",
              "type": "string"
          },
          "derivedItemCategories": {
              "description": "This is a list of the items being previewed, categorized in the same way as they are in the preview UI.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition"
              }
          }
      }
  }
}
```
