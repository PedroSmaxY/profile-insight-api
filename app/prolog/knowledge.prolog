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

% Função para calcular a pontuação
calcular_pontuacao([P1, P2, P3, P4, P5], Total) :-
    Total is P1 + P2 + P3 + P4 + P5.
