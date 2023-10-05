from solution import findIndexForString

def test_solution():
    contentSolution = str(findIndexForString())
    answerShouldBe = open("/workspaces/copilot-effeciency-study-JStuhrAsferg/Assignment02/stringmultimatching.ans").read()
    assert contentSolution == answerShouldBe