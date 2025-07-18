# Destiny.Character.DestinyCharacterCustomization

## Entity Information
- **Entity Name**: Destiny.Character.DestinyCharacterCustomization
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Raw data about the customization options chosen for a character's face and appearance.
You can look up the relevant class/race/gender combo in DestinyCharacterCustomizationOptionDefinition for the character, and then look up these values within the CustomizationOptions found to pull some data about their choices. Warning: not all of that data is meaningful. Some data has useful icons. Others have nothing, and are only meant for 3D rendering purposes (which we sadly do not expose yet)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| personality | integer (uint32) |  | No |
| face | integer (uint32) |  | No |
| skinColor | integer (uint32) |  | No |
| lipColor | integer (uint32) |  | No |
| eyeColor | integer (uint32) |  | No |
| hairColors | Array[integer] |  | No |
| featureColors | Array[integer] |  | No |
| decalColor | integer (uint32) |  | No |
| wearHelmet | boolean |  | No |
| hairIndex | integer (int32) |  | No |
| featureIndex | integer (int32) |  | No |
| decalIndex | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Character.DestinyCharacterCustomization object
const example = {
  personality: 123,
  face: 123,
  skinColor: 123,
  lipColor: 123,
  eyeColor: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Character.DestinyCharacterCustomization object
example = {
    "personality": 123,
    "face": 123,
    "skinColor": 123,
    "lipColor": 123,
    "eyeColor": 123,
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Character.DestinyCharacterCustomization":   {
      "description": "Raw data about the customization options chosen for a character's face and appearance.\r\nYou can look up the relevant class/race/gender combo in DestinyCharacterCustomizationOptionDefinition for the character, and then look up these values within the CustomizationOptions found to pull some data about their choices. Warning: not all of that data is meaningful. Some data has useful icons. Others have nothing, and are only meant for 3D rendering purposes (which we sadly do not expose yet)",
      "type": "object",
      "properties": {
          "personality": {
              "format": "uint32",
              "type": "integer"
          },
          "face": {
              "format": "uint32",
              "type": "integer"
          },
          "skinColor": {
              "format": "uint32",
              "type": "integer"
          },
          "lipColor": {
              "format": "uint32",
              "type": "integer"
          },
          "eyeColor": {
              "format": "uint32",
              "type": "integer"
          },
          "hairColors": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "featureColors": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "decalColor": {
              "format": "uint32",
              "type": "integer"
          },
          "wearHelmet": {
              "type": "boolean"
          },
          "hairIndex": {
              "format": "int32",
              "type": "integer"
          },
          "featureIndex": {
              "format": "int32",
              "type": "integer"
          },
          "decalIndex": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
