from visitor import visitor

class criacao(visitor):

    def vist_crianca(self,crianca):
        crianca.set_subscription(crianca.get_subscription() *0.85)

    def vist_adulto(self,adulto):pass


    def vist_velho(self,velho):
        velho.set_subscription(velho.get_subscription() *0.75)

    def vist_pessoas(self,pessoas):
        for pessoa in pessoas:
            pessoa.accept(self)