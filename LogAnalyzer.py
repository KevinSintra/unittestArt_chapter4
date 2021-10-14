import abc

"""
情境1: 紀錄 LOG 時若失敗, 需通知 web 服務. (commit 1)

情境2: 功能新增 => 將 web service 互動使用 tyr catch 包住, 若互動失敗需要發信. (commit 2)
    # 如何替換掉 web 服務?
    # 如何模擬來自 web 服務引發的例外?
    # 如何驗證發信過程是否正確?
"""


class IWebService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def logError(self, message: str) -> None:
        pass


class IEmailService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sendEmail(self, to: str, subject: str, body: str) -> None:
        pass


class LogAnalyzer:

    def __init__(self, webService: IWebService, mailService: IEmailService = None) -> None:
        self.__webService__ = webService
        self.__emailService__ = mailService
        pass

    def analyze(self, fileName: str) -> None:
        try:
            if(len(fileName) < 8):
                self.__webService__.logError(
                    "FileName too short: {name}".format(name=fileName))
        except Exception as e:
            self.__emailService__.sendEmail(
                "someone@somewhere.com", "cant't log", e)
