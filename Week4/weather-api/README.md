# Weather API - Lambda + API Gateway

## What This Does

A serverless REST API that returns weather data for any city.

## How to Use

Call the API with a city name:

https://your-api-endpoint/weather?city=Lagos


## Example Response

```json
{
  "city": "Lagos",
  "country": "NG",
  "temperature": 28.5,
  "feels_like": 31.2,
  "humidity": 75,
  "description": "scattered clouds",
  "wind_speed": 5.2
}
