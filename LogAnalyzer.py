import abc

"""
情境: 紀錄 LOG 時若失敗, 需通知 web 服務.
"""


class IWebService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def logError(self, message: str) -> None:
        pass


class LogAnalyzer:
    __webService__: IWebService

    def __init__(self, webService: IWebService) -> None:
        self.__webService__ = webService
        pass

    def analyze(self, fileName: str) -> None:
        if(len(fileName) < 8):
            self.__webService__.logError("FileName too short: {name}".format(name=fileName))
