import pytest
from FileHandler import parse_input
import uuid
class TestClass:
    def test_empty_file(self):
        """ Non existing files should raise error """
        
        with pytest.raises(FileNotFoundError):
            parse_input(str(uuid.uuid4()))
    def test_wrong_formated_file(self):
        """ Wrong formatted files should raise error """
        
        with pytest.raises(ValueError):
            parse_input("test_inputs/missing_color.json")
        
        with pytest.raises(ValueError):
            parse_input("test_inputs/missing_stations.json")

        with pytest.raises(ValueError):
            parse_input("test_inputs/missing_connected_stations.json")
    def test_correct_input(self):
        """ Files with good format should return the json """
        
        assert type(parse_input("test_inputs/example_input.json")) is dict

