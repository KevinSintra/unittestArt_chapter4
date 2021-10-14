import pytest
from LogAnalyzer import IWebService, LogAnalyzer

def test_Analyze_TooShortFileName_CallWebService():
    fakeService = FakeWebService()
    log = LogAnalyzer(fakeService)
    shortFileName = "abc.txt"
    log.analyze(shortFileName)
    exceptStr = "FileName too short: {name}".format(name=shortFileName)
    assert exceptStr == fakeService.lastError

class FakeWebService(IWebService):
    lastError: str

    def logError(self, message: str) -> None:
        self.lastError = message



