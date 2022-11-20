import abc

class visibilidade(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def accept(self,visitor):pass
