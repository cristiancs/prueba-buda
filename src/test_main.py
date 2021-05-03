import pytest
import main
class TestMain:

    def test_basic_case_returns_correct_response_with_red_train(self):
        """ PDF Example returns correct answer for red"""
        testClass = main.Main(["", "test_inputs/example_input.json","A","F", "red"])

        assert testClass.run() == "A->B->C->H->F"

    def test_basic_case_returns_correct_response_with_green_train(self):
        """ PDF Example returns correct answer for green"""
        testClass = main.Main(["", "test_inputs/example_input.json","A","F", "green"])

        response = testClass.run()
        assert  response== "A->B->C->D->E->F" or response ==   "A->B->C->G->I->F"
    
    def test_basic_case_returns_correct_response_with_empty_train(self):
        """ PDF Example returns correct answer for no color"""
        testClass = main.Main(["", "test_inputs/example_input.json","A","F"])
        response = testClass.run()
        assert  response== "A->B->C->D->E->F"

    def test_a_to_g_reed_should_return_empty(self):
        testClass = main.Main(["", "test_inputs/example_input.json","A","G","red"])
        response = testClass.run()
        assert  response == "No Routes"

    def test_unconnected_nodes_should_return_no_routes(self):
        testClass = main.Main(["", "test_inputs/example_input.json","A","Z","red"])
        response = testClass.run()
        assert  response == "No Routes"

    def test_invalid_color_should_return_exception(self):
        with pytest.raises(ValueError):
            testClass = main.Main(["", "test_inputs/example_input.json","A","Z","redz"])