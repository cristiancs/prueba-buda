import pytest
from BFSService import BFSService
from FileHandlerService import parse_input


class TestBFService:

    def test_basic_case_returns_correct_response_with_red_train(self):
        """ PDF Example returns correct answer for red"""
        input_data = parse_input("test_inputs/example_input.json")
        testClass = BFSService(input_data, "red")
        response = testClass.getRoute("A","F")
        assert  response == ["A","B","C","H","F"]

    def test_basic_case_returns_correct_response_with_green_train(self):
        """ PDF Example returns correct answer for green"""
        input_data = parse_input("test_inputs/example_input.json")
        testClass = BFSService(input_data, "green")
        response = testClass.getRoute("A","F")
        assert  response == ["A","B","C","D","E","F"] or testClass.getRoute("A","F") == ["A","B","C","G","I","F"]
    
    def test_basic_case_returns_correct_response_with_empty_train(self):
        """ PDF Example returns correct answer for no color"""
        input_data = parse_input("test_inputs/example_input.json")
        testClass = BFSService(input_data, "")
        response = testClass.getRoute("A","F")
        assert  response == ["A","B","C","D","E","F"]
    
    def test_a_to_a_should_return_only_a(self):
        """ PDF Example returns correct answer for no color"""
        input_data = parse_input("test_inputs/example_input.json")
        testClass = BFSService(input_data, "")
        response = testClass.getRoute("A","A")
        assert  response == ["A"]
        
    def test_a_to_g_reed_should_return_empty(self):
        input_data = parse_input("test_inputs/example_input.json")
        testClass = BFSService(input_data, "red")
        response = testClass.getRoute("A","G")
        assert  response == []

    def test_unconnected_nodes_should_return_no_routes(self):
        input_data = parse_input("test_inputs/example_input.json")
        testClass = BFSService(input_data, "red")
        response = testClass.getRoute("A","Z")
        assert  response == []