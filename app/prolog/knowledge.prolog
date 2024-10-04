:- dynamic pergunta/3.

% Perguntas para Dominância
pergunta(dominancia, 1, 'Você se considera uma pessoa competitiva?').
pergunta(dominancia, 2, 'Você gosta de tomar decisões rapidamente?').
pergunta(dominancia, 3, 'Você prefere liderar do que ser liderado?').
pergunta(dominancia, 4, 'Você é orientado para resultados?').
pergunta(dominancia, 5, 'Você se sente confortável em assumir riscos?').

% Perguntas para Influência
pergunta(influencia, 1, 'Você gosta de conversar com diferentes tipos de pessoas?').
pergunta(influencia, 2, 'Você prefere trabalhar em grupo do que sozinho?').
pergunta(influencia, 3, 'Você gosta de persuadir os outros?').
pergunta(influencia, 4, 'Você prefere inspirar as pessoas em vez de seguir regras?').
pergunta(influencia, 5, 'Você gosta de ser o centro das atenções?').

% Perguntas para Estabilidade
pergunta(estabilidade, 1, 'Você prefere um ambiente de trabalho previsível?').
pergunta(estabilidade, 2, 'Você evita mudanças rápidas?').
pergunta(estabilidade, 3, 'Você é uma pessoa paciente?').
pergunta(estabilidade, 4, 'Você prefere seguir um ritmo constante no trabalho?').
pergunta(estabilidade, 5, 'Você prefere resolver conflitos de forma pacífica?').

% Perguntas para Conformidade
pergunta(conformidade, 1, 'Você presta atenção aos detalhes?').
pergunta(conformidade, 2, 'Você gosta de seguir regras e procedimentos?').
pergunta(conformidade, 3, 'Você se considera uma pessoa analítica?').
pergunta(conformidade, 4, 'Você é rigoroso ao seguir padrões estabelecidos?').
pergunta(conformidade, 5, 'Você prefere trabalhar com dados e fatos?').

% Função para buscar próxima pergunta
proxima_pergunta(Categoria, Id, Pergunta) :-
    pergunta(Categoria, Id, Pergunta).

% Diagnóstico com base nas respostas
diagnostico(Categoria, Respostas, Diagnostico) :-
    pontuacao(Respostas, Pontuacao),
    interpretar(Categoria, Pontuacao, Diagnostico).

% Cálculo da pontuação
pontuacao(Respostas, Total) :-
    sum_list(Respostas, Total).

% Interpretação do diagnóstico com base na pontuação
interpretar(dominancia, Pontuacao, 'Alta dominância') :- Pontuacao >= 20.
interpretar(dominancia, Pontuacao, 'Dominância moderada') :- Pontuacao >= 10, Pontuacao < 20.
interpretar(dominancia, Pontuacao, 'Baixa dominância') :- Pontuacao < 10.

interpretar(influencia, Pontuacao, 'Alta influência') :- Pontuacao >= 20.
interpretar(influencia, Pontuacao, 'Influência moderada') :- Pontuacao >= 10, Pontuacao < 20.
interpretar(influencia, Pontuacao, 'Baixa influência') :- Pontuacao < 10.

interpretar(estabilidade, Pontuacao, 'Alta estabilidade') :- Pontuacao >= 20.
interpretar(estabilidade, Pontuacao, 'Estabilidade moderada') :- Pontuacao >= 10, Pontuacao < 20.
interpretar(estabilidade, Pontuacao, 'Baixa estabilidade') :- Pontuacao < 10.

interpretar(conformidade, Pontuacao, 'Alta conformidade') :- Pontuacao >= 20.
interpretar(conformidade, Pontuacao, 'Conformidade moderada') :- Pontuacao >= 10, Pontuacao < 20.
interpretar(conformidade, Pontuacao, 'Baixa conformidade') :- Pontuacao < 10.
