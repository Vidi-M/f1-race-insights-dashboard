import json
# import sys
# sys.path.append('./python')  # Adjust the path as necessary

# import fastf1

#Simple code to check if it is working
# def lambda_handler(event, context):
#     # Enable caching (store in /tmp directory, which Lambda provides for temporary storage)
#     # fastf1.Cache.enable_cache("/tmp")
    
#     # Load race data (e.g., 2021 Bahrain GP)
#     race = fastf1.get_session(2024, 'Monza', 'R')
#     race.load()

#     # Extract the abbreviation
#     abbreviation = race.results['Abbreviation']
    
#     # Check the type and handle accordingly
#     if isinstance(abbreviation, str):
#         abbreviation_value = abbreviation  # Directly use the string
#     else:
#         abbreviation_value = abbreviation.values[0]  # Get the first value if it's a Series
    
#     # Return the lap data as a JSON response
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Placeholder Lambda!')  # Now this should be serializable
#     }
    
#     response = {
#         'statusCode': 200,
#         'body': json.dumps(abbreviation_value),
#         'headers': {
#             'Content-Type': 'application/json',
#             'Access-Control-Allow-Origin': '*',  # Allow all origins for CORS
#             'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',  # Allow the necessary methods
#             'Access-Control-Allow-Headers': 'Content-Type'  # Allow Content-Type header
#         }
#     }
#     print("hello")
#     print(abbreviation_value)
#     return response

## Code to check if the api gateway is working
def lambda_handler(event, context):
    # Return the text as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Placeholder Lambda!')  # Now this should be serializable
    }