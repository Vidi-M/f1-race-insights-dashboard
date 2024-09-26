import json
import fastf1

#Simple code to check if it is working
def lambda_handler(event, context):
    # Enable caching (store in /tmp directory, which Lambda provides for temporary storage)
    # fastf1.Cache.enable_cache("/tmp")
    
    # Load race data (e.g., 2021 Bahrain GP)
    race = fastf1.get_session(2024, 'Monza', 'R')
    race.load()

    # Extract the abbreviation
    abbreviation = race.results['Abbreviation']
    
    # Check the type and handle accordingly
    if isinstance(abbreviation, str):
        abbreviation_value = abbreviation  # Directly use the string
    else:
        abbreviation_value = abbreviation.values[0]  # Get the first value if it's a Series
    
    # Return the order of driver numbers as a JSON response
    response = {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Successfully processed the request!',
            'data': {abbreviation_value}  # You can add the actual response data here
        }),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # Allow all origins for CORS
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',  # Allow the necessary methods
            'Access-Control-Allow-Headers': 'Content-Type'  # Allow Content-Type header
        }
    }

    return response