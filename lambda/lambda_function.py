import json
import fastf1

#Simple code to check if it is working
def lambda_handler(event, context):
    # Enable caching (store in /tmp directory, which Lambda provides for temporary storage)
    fastf1.Cache.enable_cache("/tmp")
    
    # Load race data (e.g., 2021 Bahrain GP)
    race = fastf1.get_session(2024, 'Monza', 'R')
    race.load()

    

    # Return the lap data as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps(race.results['Abbreviation'])
    }