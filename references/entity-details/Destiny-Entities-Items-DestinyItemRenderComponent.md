# Destiny.Entities.Items.DestinyItemRenderComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemRenderComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Many items can be rendered in 3D. When you request this block, you will obtain the custom data needed to render this specific instance of the item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| useCustomDyes | boolean | If you should use custom dyes on this item, it will be indicated here. | No |
| artRegions | object | A dictionary for rendering gear components, with:
key = Art Arrangement Region Index
value = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemRenderComponent object
const example = {
  useCustomDyes: true,
  artRegions: null,
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemRenderComponent object
example = {
    "useCustomDyes": True,
    "artRegions": None,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemRenderComponent":   {
      "description": "Many items can be rendered in 3D. When you request this block, you will obtain the custom data needed to render this specific instance of the item.",
      "type": "object",
      "properties": {
          "useCustomDyes": {
              "description": "If you should use custom dyes on this item, it will be indicated here.",
              "type": "boolean"
          },
          "artRegions": {
              "description": "A dictionary for rendering gear components, with:\r\nkey = Art Arrangement Region Index\r\nvalue = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice.",
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemRenderData"
  }
}
```
