import  abc

class visitor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def vist_crianca(self,crianca):pass

    @abc.abstractmethod
    def vist_adulto(self,adulto):pass

    @abc.abstractmethod
    def vist_velho(self,velho):pass

    @abc.abstractmethod
    def vist_pessoas(self,pessoas):pass