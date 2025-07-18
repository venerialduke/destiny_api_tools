# Applications.ApiUsage

## Entity Information
- **Entity Name**: Applications.ApiUsage
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Contains usage statistics for API calls made by an application, including both successful API calls and throttled requests during a specified time range.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| apiCalls | Array[Applications.Series] | Counts for on API calls made for the time range. | No |
| throttledRequests | Array[Applications.Series] | Instances of blocked requests or requests that crossed the warn threshold during the time range. | No |

## Usage Examples

### JavaScript
```javascript
// Example API usage response
const apiUsage = {
  apiCalls: [
    {
      target: "GetProfile",
      datapoints: [
        {
          time: "2023-12-01T00:00:00Z",
          count: 150.0
        },
        {
          time: "2023-12-01T01:00:00Z", 
          count: 200.0
        }
      ]
    }
  ],
  throttledRequests: [
    {
      target: "GetProfile",
      datapoints: [
        {
          time: "2023-12-01T00:00:00Z",
          count: 5.0
        }
      ]
    }
  ]
};

// Access API call statistics
console.log(`Total API calls: ${apiUsage.apiCalls[0].datapoints.reduce((sum, dp) => sum + dp.count, 0)}`);
```

### Python
```python
# Example API usage response
api_usage = {
    "apiCalls": [
        {
            "target": "GetProfile",
            "datapoints": [
                {
                    "time": "2023-12-01T00:00:00Z",
                    "count": 150.0
                },
                {
                    "time": "2023-12-01T01:00:00Z",
                    "count": 200.0
                }
            ]
        }
    ],
    "throttledRequests": [
        {
            "target": "GetProfile", 
            "datapoints": [
                {
                    "time": "2023-12-01T00:00:00Z",
                    "count": 5.0
                }
            ]
        }
    ]
}

# Calculate total API calls
total_calls = sum(dp["count"] for series in api_usage["apiCalls"] for dp in series["datapoints"])
print(f"Total API calls: {total_calls}")
```

## Related Entities
- **Applications.Series**: Used for both apiCalls and throttledRequests arrays
- **Applications.Datapoint**: Contains individual time/count data points within each series
- **Applications.Application**: The application this usage data belongs to

## Notes
- Used for monitoring API usage patterns and identifying potential throttling issues
- The apiCalls array contains successful API request counts over time
- The throttledRequests array tracks when requests were blocked or warned due to rate limiting
- Each series can contain multiple datapoints representing different time periods
- Useful for developers to understand their application's API consumption patterns

## JSON Schema
```json
{
  "Applications.ApiUsage": {
    "type": "object",
    "properties": {
      "apiCalls": {
        "description": "Counts for on API calls made for the time range.",
        "type": "array",
        "items": {
          "$ref": "#/definitions/Applications.Series"
        }
      },
      "throttledRequests": {
        "description": "Instances of blocked requests or requests that crossed the warn threshold during the time range.",
        "type": "array",
        "items": {
          "$ref": "#/definitions/Applications.Series"
        }
      }
    }
  }
}
```