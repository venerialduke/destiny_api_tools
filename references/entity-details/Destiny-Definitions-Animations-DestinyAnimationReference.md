# Destiny.Definitions.Animations.DestinyAnimationReference

## Entity Information
- **Entity Name**: Destiny.Definitions.Animations.DestinyAnimationReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyanimationreference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| animName | string |  | No |
| animIdentifier | string |  | No |
| path | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Animations.DestinyAnimationReference object
const example = {
  animName: "example value",
  animIdentifier: "example value",
  path: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Animations.DestinyAnimationReference object
example = {
    "animName": "example value",
    "animIdentifier": "example value",
    "path": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Animations.DestinyAnimationReference":   {
      "type": "object",
      "properties": {
          "animName": {
              "type": "string"
          },
          "animIdentifier": {
              "type": "string"
          },
          "path": {
              "type": "string"
          }
      }
  }
}
```
