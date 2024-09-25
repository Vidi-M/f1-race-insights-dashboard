import json
import unittest
from unittest.mock import patch, MagicMock

# Assuming the lambda_handler is in a file named `my_lambda.py`
from lambda_.lambda_function import lambda_handler

class TestLambdaHandler(unittest.TestCase):

    @patch('lambda_.lambda_function.fastf1.get_session')  # Mock the fastf1.get_session method
    @patch('lambda_.lambda_function.fastf1.Cache.enable_cache')  # Mock the enable_cache method
    def test_lambda_handler(self, mock_enable_cache, mock_get_session):
        # Create a mock race object with expected results
        mock_race = MagicMock()
        mock_race.results = {
            'Abbreviation': 'MON'  # Example abbreviation for Monza
        }
        # Configure the mock to return the mock race object
        mock_get_session.return_value = mock_race
        
        # Create a dummy event and context
        event = {}
        context = {}

        # Call the lambda_handler
        response = lambda_handler(event, context)

        # Check the status code
        self.assertEqual(response['statusCode'], 200)
        
        # Check the body content
        self.assertEqual(json.loads(response['body']), 'MON')

class TestLambdaIntegration(unittest.TestCase):

    def test_lambda_integration(self):
        # Create a dummy event and context
        event = {}
        context = {}

        # Call the actual lambda_handler function
        response = lambda_handler(event, context)  # This should call the actual API

        # Check if the response is valid
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('body', response)
        body = json.loads(response['body'])

        # Check if the body contains the expected structure (you may need to adjust based on actual results)
        self.assertIsInstance(body, str)  # Ensure the body is a string

# This line allows running the test from the command line
if __name__ == '__main__':
    unittest.main()
