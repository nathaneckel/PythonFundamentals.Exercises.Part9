import json
import os
import unittest

from json_helper import read_json, read_json_files_and_print_contents

#example of test errors I'm getting:
#FileNotFoundError: [Errno 2] No such file or directory: 'data/He-Man_Figures/He-Man.json'
#I am confused; that IS actually the path to the file.
#Have several other labs to catch up on so I'm doing that.
class TestFunctions(unittest.TestCase):

    def test_read_json(self):
        # Create a temporary JSON file with known data
        temp_json_file = 'temp.json'
        json_data = {'key': 'value'}
        with open(temp_json_file, 'w') as f:
            json.dump(json_data, f)

        # Test read_json function
        result = read_json(temp_json_file)
        self.assertEqual(result, json_data)

        # Clean up temporary file
        os.remove(temp_json_file)

    def test_read_json_files_and_print_contents(self):
        # Create a temporary directory with known JSON files
        temp_dir = 'temp_dir'
        os.makedirs(temp_dir)
        json_data = {'key': 'value'}
        with open(os.path.join(temp_dir, 'file1.json'), 'w') as f:
            json.dump(json_data, f)
        with open(os.path.join(temp_dir, 'file2.json'), 'w') as f:
            json.dump(json_data, f)

        # Redirect stdout to capture print statements
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # Test read_json_files_and_print_contents function
        read_json_files_and_print_contents(temp_dir)

        # Get printed contents
        printed_contents = sys.stdout.getvalue()

        # Assert that printed contents match expected
        expected_contents = str(json_data) + '\n' * 2
        self.assertEqual(printed_contents, expected_contents)

        # Clean up temporary directory
        os.remove(os.path.join(temp_dir, 'file1.json'))
        os.remove(os.path.join(temp_dir, 'file2.json'))
        os.rmdir(temp_dir)

    # Add similar tests for write_pickle and load_pickle functions

if __name__ == '__main__':
    unittest.main()
