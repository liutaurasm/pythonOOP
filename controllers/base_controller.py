from abc import ABC, abstractmethod


class BaseController(ABC):

    path = "/"

    @abstractmethod
    def GET(http):
        pass

    @abstractmethod
    def POST(http):
        pass
