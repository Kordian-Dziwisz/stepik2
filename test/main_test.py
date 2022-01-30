import main


def test_mainFunction():
    assert main.mainFunction(3) == '***'
    assert main.mainFunction(1) == '*'
    assert main.mainFunction(0) == ''
    assert main.mainFunction(-4) == False
