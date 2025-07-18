# Applications.Series

## Entity Information
- **Entity Name**: Applications.Series
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a series of data points with associated target information, typically used for time-series data in API usage statistics.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| datapoints | Array[Applications.Datapoint] | Collection of samples with time and value. | No |
| target | string | Target to which to datapoints apply. | No |

## Usage Examples

### JavaScript
```javascript
// Example series data
const series = {
  target: "GetProfile",
  datapoints: [
    {
      time: "2023-12-01T00:00:00Z",
      count: 150.0
    },
    {
      time: "2023-12-01T01:00:00Z",
      count: 200.0
    },
    {
      time: "2023-12-01T02:00:00Z",
      count: 175.0
    }
  ]
};

// Process series data
console.log(`Target: ${series.target}`);
console.log(`Data points: ${series.datapoints.length}`);

// Calculate total count
const totalCount = series.datapoints.reduce((sum, dp) => sum + dp.count, 0);
console.log(`Total count: ${totalCount}`);

// Find peak usage time
const peakDatapoint = series.datapoints.reduce((max, dp) => 
  dp.count > max.count ? dp : max
);
console.log(`Peak usage at ${peakDatapoint.time}: ${peakDatapoint.count}`);
```

### Python
```python
# Example series data
series = {
    "target": "GetProfile",
    "datapoints": [
        {
            "time": "2023-12-01T00:00:00Z",
            "count": 150.0
        },
        {
            "time": "2023-12-01T01:00:00Z", 
            "count": 200.0
        },
        {
            "time": "2023-12-01T02:00:00Z",
            "count": 175.0
        }
    ]
}

# Process series data
print(f"Target: {series['target']}")
print(f"Data points: {len(series['datapoints'])}")

# Calculate total count
total_count = sum(dp["count"] for dp in series["datapoints"])
print(f"Total count: {total_count}")

# Find peak usage time
peak_datapoint = max(series["datapoints"], key=lambda dp: dp["count"])
print(f"Peak usage at {peak_datapoint['time']}: {peak_datapoint['count']}")
```

## Related Entities
- **Applications.Datapoint**: Individual data points within the series
- **Applications.ApiUsage**: Uses Series objects for API call and throttled request tracking
- **Applications.Application**: Indirectly related through usage statistics

## Notes
- Used as a container for time-series data in API usage statistics
- The target property typically identifies the API endpoint or operation being measured
- Datapoints are usually ordered chronologically
- Common targets include endpoint names like "GetProfile", "GetCharacter", etc.
- Used for both successful API calls and throttled requests tracking

## JSON Schema
```json
{
  "Applications.Series": {
    "type": "object",
    "properties": {
      "datapoints": {
        "description": "Collection of samples with time and value.",
        "type": "array",
        "items": {
          "$ref": "#/definitions/Applications.Datapoint"
        }
      },
      "target": {
        "description": "Target to which to datapoints apply.",
        "type": "string"
      }
    }
  }
}
```