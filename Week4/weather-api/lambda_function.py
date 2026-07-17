import json
import urllib.request
import os

def lambda_handler(event, context):
    print("Full event:", json.dumps(event))
    
    city = None
    
    # Try multiple ways to get city
    if event.get('queryStringParameters'):
        city = event['queryStringParameters'].get('city')
    
    if not city and event.get('multiValueQueryStringParameters'):
        params = event['multiValueQueryStringParameters'].get('city', [])
        if params:
            city = params[0]
    
    if not city:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'City required', 'received': event})
        }
    
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        
        result = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(result)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }