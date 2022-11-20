from adulto import  adulto
from crianca import  crianca
from velhos import  velho
from criacao import criacao
from criacao_ouro import criacao_ouro

def main ():

    c_1 = crianca()
    c_2 = crianca()

    a_1 = adulto()
    a_2 = adulto()

    v_1 = velho()
    v_2 = velho()

    p_1 = [c_1,a_1,v_1]
    p_2 = [c_2,a_2,v_2]

    cria = criacao()
    cria.vist_pessoas(p_1)

    cria_ouro = criacao_ouro()
    cria_ouro.vist_pessoas(p_2)

    print(f'\n Preço  de assinatura \nCriança: {c_1.get_subscription()}'
          f'\nAdulto: {a_1.get_subscription()}'
          f'\nVelho:  {v_1.get_subscription()} ')

    print(f'\n Preço  de assinatura - OURO - \nCriança: {c_2.get_subscription()}'
          f'\nAdulto: {a_2.get_subscription()}'
          f'\nVelho:  {v_2.get_subscription()} ')

    if __name__ == '__main__':
        main()