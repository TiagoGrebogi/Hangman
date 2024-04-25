def dica(palavra):

    dicas_frutas = {
        "morango": "Uma fruta vermelha, pequena e doce",
        "abacaxi": "Uma fruta tropical grande com uma casca espinhosa e polpa amarela",
        "manga": "Fruta tropical suculenta, com polpa doce e cores vibrantes, como laranja ou amarelo",
        "limao": "Fruto cítrico amargo, comum em culinária e bebidas, conhecido por sua casca verde ou amarela e polpa ácida",
        "uva": "Pequenas frutas suculentas, geralmente em cachos, com variedades em verde, vermelho, roxo ou preto, apreciadas por seu sabor doce e uso em vinhos e sucos",
        "kiwi": "Fruta pequena, com casca peluda marrom e polpa verde, repleta de pequenas sementes pretas, conhecida por seu sabor doce e ligeiramente ácido"
    }
    
    dicas_paises = {
        "brasil": "País tropical, conhecido pela sua vasta diversidade cultural, praias deslumbrantes e pela Floresta Amazônica, a maior do mundo",
        "franca": "País europeu famoso por sua rica história, arte, culinária sofisticada e ícones como a Torre Eiffel e o Louvre",
        "japao": "Nação insular asiática, reconhecida por sua tecnologia avançada, cultura tradicional, como o chá cerimonial, e pela hospitalidade do povo japonês",
        "australia": "País insular localizado no Hemisfério Sul, conhecido por suas vastas paisagens naturais, vida selvagem única e praias paradisíacas",
        "mexico": "Nação da América Latina, famosa por sua rica cultura, incluindo a antiga civilização asteca, praias deslumbrantes e culinária picante",
        "canada": "País norte-americano conhecido por suas paisagens deslumbrantes, como as Montanhas Rochosas e as Cataratas do Niágara, e por sua qualidade de vida elevada"
    }
    
    dicas_profissao = {
        "medico": "Profissional da saúde responsável por diagnosticar, tratar e prevenir doenças em pacientes, com formação em medicina e especialidades diversas",
        "professor": "Educador dedicado ao ensino e à orientação de alunos em diferentes níveis de educação, compartilhando conhecimento e estimulando o desenvolvimento intelectual",
        "bombeiro": "Servidor público treinado para combater incêndios, realizar resgates em situações de emergência e prestar assistência médica de primeiros socorros",
        "policial": "Agente encarregado de manter a ordem pública, prevenir crimes e fazer cumprir a lei, protegendo a comunidade e investigando atividades criminosas",
        "cozinheiro": "Profissional especializado na preparação de alimentos, utilizando técnicas culinárias para criar pratos saborosos e atraentes em diversos estilos de cozinha",
        "jardineiro": "Trabalhador responsável pelo cuidado e manutenção de jardins e áreas verdes, realizando plantio, poda, irrigação e outras atividades para garantir a saúde das plantas e a beleza do ambiente"
    }

    dicas_carros = {
        "lamborghini": "Um carro esportivo de luxo e alta velocidade.",
        "maserati": "Outro carro de luxo conhecido por seu design elegante e desempenho poderoso.",
        "bugatti": "Marca conhecida por produzir alguns dos veículos mais rápidos e exclusivos do mundo",
        "mclaren": "Fabricante britânica de carros esportivos de alto desempenho, famosa por sua engenharia inovadora e design aerodinâmico",
        "pagani": "Marca italiana de carros superesportivos artesanais, reconhecida por seu design exótico",
        "koenigsegg": "Montadora sueca de carros esportivos de alto desempenho, conhecida por seus veículos de produção limitada"
    }
    
    dicas_objetos = {
        "luminaria": "",
        "binoculo": "",
        "telescopio": "",
        "xicara": "",
        "trena": "",
        "ventilador": ""
    }

    dicas_filmes = {
        "matrix": "",
        "titanic": "",
        "avatar": "",
        "transformers": "",
        "interstellar": "",
        "shrek": ""
    }
    
    if palavra in dicas_frutas:
        return dicas_frutas[palavra]
    elif palavra in dicas_paises:
        return dicas_paises[palavra]
    elif palavra in dicas_profissao:
        return dicas_profissao[palavra]
    
    
    elif palavra in dicas_carros:
        return dicas_carros[palavra]
    elif palavra in dicas_objetos:
        return dicas_objetos[palavra]
    elif palavra in dicas_filmes:
        return dicas_filmes[palavra]

    return "Desculpe, não há dica disponível para esta palavra."

