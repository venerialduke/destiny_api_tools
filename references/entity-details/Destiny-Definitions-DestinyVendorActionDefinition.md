# Destiny.Definitions.DestinyVendorActionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorActionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If a vendor can ever end up performing actions, these are the properties that will be related to those actions. I'm not going to bother documenting this yet, as it is unused and unclear if it will ever be used... but in case it is ever populated and someone finds it useful, it is defined here.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| description | string |  | No |
| executeSeconds | integer (int32) |  | No |
| icon | string |  | No |
| name | string |  | No |
| verb | string |  | No |
| isPositive | boolean |  | No |
| actionId | string |  | No |
| actionHash | integer (uint32) |  | No |
| autoPerformAction | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorActionDefinition object
const example = {
  description: "example value",
  executeSeconds: 123,
  icon: "example value",
  name: "example value",
  verb: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorActionDefinition object
example = {
    "description": "example value",
    "executeSeconds": 123,
    "icon": "example value",
    "name": "example value",
    "verb": "example value",
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorActionDefinition":   {
      "description": "If a vendor can ever end up performing actions, these are the properties that will be related to those actions. I'm not going to bother documenting this yet, as it is unused and unclear if it will ever be used... but in case it is ever populated and someone finds it useful, it is defined here.",
      "type": "object",
      "properties": {
          "description": {
              "type": "string"
          },
          "executeSeconds": {
              "format": "int32",
              "type": "integer"
          },
          "icon": {
              "type": "string"
          },
          "name": {
              "type": "string"
          },
          "verb": {
              "type": "string"
          },
          "isPositive": {
              "type": "boolean"
          },
          "actionId": {
              "type": "string"
          },
          "actionHash": {
              "format": "uint32",
              "type": "integer"
          },
          "autoPerformAction": {
              "type": "boolean"
          }
      }
  }
}
```
