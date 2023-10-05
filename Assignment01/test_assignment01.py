from Solution import runner

def test_solution():
    contentSolution = str(runner())
    answerShouldBe = open("/workspaces/copilot-effeciency-study-JStuhrAsferg/Assignment01/airlinehub.ans").read()
    assert contentSolution == answerShouldBe