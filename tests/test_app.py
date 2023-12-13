import json
import unittest
import sys
import app

sys.path.insert(0, '../webixHomeAssignment')


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """"" Setup method to create a test client"""
        self.app = app.app.test_client()
        self.app.testing = True

    def test_valid_word(self):
        """Test case for a valid word"""
        response = self.app.post('/calculate_embedding', data=dict(word='dog'))

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertIn('word', response_data)
        self.assertIn('vector', response_data)
        self.assertIn('message', response_data)

        self.assertEqual(response_data['word'], 'dog')

        self.assertIsInstance(response_data['vector'], list)

        self.assertEqual(response_data['message'], "Vector representation of the word successfully retrieved.")

    def test_invalid_word(self):
        """Test case for an invalid word (not in model vocabulary)"""
        response = self.app.post('/calculate_embedding', data=dict(word='notaword'))

        self.assertEqual(response.status_code, 400)

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertIn('error', response_data)

        self.assertEqual(response_data['error'], "The word 'notaword' does not have an associated vector.")

    def test_more_than_one_word(self):
        """Test case for more than one word (not supported)"""
        response = self.app.post('/calculate_embedding', data=dict(word='not a word'))

        self.assertEqual(response.status_code, 400)

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertIn('error', response_data)

        self.assertEqual(response_data['error'], "Please enter only one word.")


if __name__ == '__main__':
    unittest.main()
