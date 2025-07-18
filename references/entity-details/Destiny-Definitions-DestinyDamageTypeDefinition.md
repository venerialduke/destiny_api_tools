# Destiny.Definitions.DestinyDamageTypeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyDamageTypeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
All damage types that are possible in the game are defined here, along with localized info and icons as needed.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | The description of the damage type, icon etc... | No |
| transparentIconPath | string | A variant of the icon that is transparent and colorless. | No |
| showIcon | boolean | If TRUE, the game shows this damage type's icon. Otherwise, it doesn't. Whether you show it or not is up to you. | No |
| enumValue | integer (int32) | We have an enumeration for damage types for quick reference. This is the current definition's damage type enum value. | No |
| color | object | A color associated with the damage type. The displayProperties icon is tinted with a color close to this. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyDamageTypeDefinition object
const example = {
  displayProperties: null,
  transparentIconPath: "example value",
  showIcon: true,
  enumValue: 123,
  color: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyDamageTypeDefinition object
example = {
    "displayProperties": None,
    "transparentIconPath": "example value",
    "showIcon": True,
    "enumValue": 123,
    "color": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.DamageType**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyDamageTypeDefinition":   {
      "description": "All damage types that are possible in the game are defined here, along with localized info and icons as needed.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "The description of the damage type, icon etc...",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "transparentIconPath": {
              "description": "A variant of the icon that is transparent and colorless.",
              "type": "string"
          },
          "showIcon": {
              "description": "If TRUE, the game shows this damage type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.",
              "type": "boolean"
          },
          "enumValue": {
              "format": "int32",
              "description": "We have an enumeration for damage types for quick reference. This is the current definition's damage type enum value.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DamageType"
              }
          },
          "color": {
              "description": "A color associated with the damage type. The displayProperties icon is tinted with a color close to this.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Misc.DestinyColor"
                  }
              ]
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "DamageTypes"
  }
}
```
