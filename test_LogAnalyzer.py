import pytest
from LogAnalyzer import IEmailService, IWebService, LogAnalyzer


class FakeWebService(IWebService):
    lastError: str

    def logError(self, message: str) -> None:
        self.lastError = message


def test_Analyze_TooShortFileName_CallWebService():
    fakeService = FakeWebService()
    log = LogAnalyzer(fakeService)
    shortFileName = "abc.txt"
    log.analyze(shortFileName)
    exceptStr = "FileName too short: {name}".format(name=shortFileName)
    assert exceptStr == fakeService.lastError


class FakeWebService2(IWebService):
    toThrow: Exception = None

    def logError(self, message: str) -> None:
        if(self.toThrow != None):
            raise self.toThrow
        else:
            pass


class FakeEmailService(IEmailService):
    def __init__(self) -> None:
        self.to = ""
        self.subject = ""
        self.body = ""
        pass

    def sendEmail(self, to: str, subject: str, body: str) -> None:
        self.to = to
        self.subject = subject
        self.body = body
        pass


def test_Analyzer_WebServiceThrows_SendEmail():
    webService = FakeWebService2()  # 因不驗證, 所以是 虛設常式
    e = Exception("fake exception")
    webService.toThrow = e
    mailService = FakeEmailService()  # 因需驗證, 所以是 模擬物件
    log = LogAnalyzer(webService, mailService)
    fileName = "abc.txt"
    log.analyze(fileName)
    assert "someone@somewhere.com" == mailService.to
    assert "cant't log" == mailService.subject
    assert e == mailService.body
