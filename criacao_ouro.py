from visitor import visitor

class criacao_ouro(visitor):

    def vist_crianca(self,crianca):
        crianca.set_subscription(crianca.get_subscription() *0.75)

    def vist_adulto(self,adulto):
        adulto.set_subscription(adulto.get_subscription()* 0.90)


    def vist_velho(self,velho):
        velho.set_subscription(velho.get_subscription() *0.50)

    def vist_pessoas(self,pessoas):
        for pessoa in pessoas:
            pessoa.accept(self)