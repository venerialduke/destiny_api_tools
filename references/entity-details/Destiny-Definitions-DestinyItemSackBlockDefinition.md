# Destiny.Definitions.DestinyItemSackBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSackBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Some items are "sacks" - they can be "opened" to produce other items. This is information related to its sack status, mostly UI strings. Engrams are an example of items that are considered to be "Sacks".

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| detailAction | string | A description of what will happen when you open the sack. As far as I can tell, this is blank currently. Unknown whether it will eventually be populated with useful info. | No |
| openAction | string | The localized name of the action being performed when you open the sack. | No |
| selectItemCount | integer (int32) |  | No |
| vendorSackType | string |  | No |
| openOnAcquire | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSackBlockDefinition object
const example = {
  detailAction: "example value",
  openAction: "example value",
  selectItemCount: 123,
  vendorSackType: "example value",
  openOnAcquire: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSackBlockDefinition object
example = {
    "detailAction": "example value",
    "openAction": "example value",
    "selectItemCount": 123,
    "vendorSackType": "example value",
    "openOnAcquire": True,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSackBlockDefinition":   {
      "description": "Some items are \"sacks\" - they can be \"opened\" to produce other items. This is information related to its sack status, mostly UI strings. Engrams are an example of items that are considered to be \"Sacks\".",
      "type": "object",
      "properties": {
          "detailAction": {
              "description": "A description of what will happen when you open the sack. As far as I can tell, this is blank currently. Unknown whether it will eventually be populated with useful info.",
              "type": "string"
          },
          "openAction": {
              "description": "The localized name of the action being performed when you open the sack.",
              "type": "string"
          },
          "selectItemCount": {
              "format": "int32",
              "type": "integer"
          },
          "vendorSackType": {
              "type": "string"
          },
          "openOnAcquire": {
              "type": "boolean"
          }
      }
  }
}
```
