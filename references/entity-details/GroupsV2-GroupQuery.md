# GroupsV2.GroupQuery

## Entity Information
- **Entity Name**: GroupsV2.GroupQuery
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes".
If you are querying for a group, you can pass any of the properties below.
If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values):
- groupMemberCountFilter - localeFilter - tagText
If you pass these, you will get a useless InvalidParameters error.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| groupType | integer (int32) |  | No |
| creationDate | integer (int32) |  | No |
| sortBy | integer (int32) |  | No |
| groupMemberCountFilter | integer (int32) |  | No |
| localeFilter | string |  | No |
| tagText | string |  | No |
| itemsPerPage | integer (int32) |  | No |
| currentPage | integer (int32) |  | No |
| requestContinuationToken | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupQuery object
const example = {
  name: "example value",
  groupType: 123,
  creationDate: 123,
  sortBy: 123,
  groupMemberCountFilter: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupQuery object
example = {
    "name": "example value",
    "groupType": 123,
    "creationDate": 123,
    "sortBy": 123,
    "groupMemberCountFilter": 123,
    # ... more properties
}
```

## Related Entities
- **GroupsV2.GroupDateRange**: Referenced in this entity
- **GroupsV2.GroupSortBy**: Referenced in this entity
- **GroupsV2.GroupType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupQuery":   {
      "description": "NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible \"modes\".\r\nIf you are querying for a group, you can pass any of the properties below.\r\nIf you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values):\r\n- groupMemberCountFilter - localeFilter - tagText\r\nIf you pass these, you will get a useless InvalidParameters error.",
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "groupType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupType"
              }
          },
          "creationDate": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupDateRange"
              }
          },
          "sortBy": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupSortBy"
              }
          },
          "groupMemberCountFilter": {
              "format": "int32",
              "enum": [
                  "0",
                  "1",
                  "2",
                  "3"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "All"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "OneToTen"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "ElevenToOneHundred"
                  },
                  {
                      "numericValue": "3",
                      "identifier": "GreaterThanOneHundred"
                  }
              ]
          },
          "localeFilter": {
              "type": "string"
          },
          "tagText": {
              "type": "string"
          },
          "itemsPerPage": {
              "format": "int32",
              "type": "integer"
          },
          "currentPage": {
              "format": "int32",
              "type": "integer"
          },
          "requestContinuationToken": {
              "type": "string"
          }
      }
  }
}
```
