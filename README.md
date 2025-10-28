🇬🇧 Projeto de Estudo de Inglês (Iniciante → Avançado)

Arquivo principal: Projeto_Estudo_Ingles.py
Tipo: Aplicação de linha de comando (CLI)
Objetivo: Oferecer uma forma interativa e prática de estudar inglês do nível iniciante ao avançado, com mais de 40 exercícios, treino de vocabulário e rastreamento de progresso.

🧩 Funcionalidades Principais

Mais de 40 exercícios organizados por nível:

🟢 Iniciante: vocabulário básico, verbo to be, cores, pronomes, frases simples.

🟡 Intermediário: present simple, past simple, preposições, phrasal verbs, reading e modal verbs.

🔴 Avançado: voz passiva, conditionals, idioms, collocations e interpretação de textos.

Tipos de exercício: múltipla escolha, tradução, preencher lacunas, reordenação de frases, correspondência (match), conjugação e escrita aberta.

Treinador de vocabulário com palavras básicas (personalizável).

Sistema de progresso automático (salvo em JSON localmente).

Revisão rápida dos últimos exercícios realizados.

Exportação de progresso para arquivo .json.

🧠 Estrutura do Projeto
📁 Projeto_Estudo_Ingles/
│
├── Projeto_Estudo_Ingles.py       # Código principal (CLI)
├── data_english_study/            # Pasta gerada automaticamente
│   ├── progress.json              # Histórico de progresso
│   └── vocab.json                 # Vocabulário básico do usuário
└── README.md                      # Este arquivo

🚀 Como Usar

Certifique-se de ter o Python 3 instalado.
Verifique com:

python --version


Execute o script principal:

python Projeto_Estudo_Ingles.py


Use o menu interativo:

1 → Escolher nível e fazer exercício

2 → Listar exercícios por nível

3 → Treinador de vocabulário

4 → Revisão rápida (últimos 10 exercícios)

5 → Exportar progresso

6 → Sair

Durante um exercício, digite q para voltar ao menu principal.

💾 Armazenamento de Progresso

Os dados do usuário são salvos automaticamente em:

data_english_study/progress.json


Isso inclui:

Últimos exercícios feitos

Pontuação individual por exercício

Histórico com data e hora

🧩 Personalização

Você pode editar ou expandir o vocabulário abrindo o arquivo:

data_english_study/vocab.json


Exemplo de formato:

[
  {"en": "dog", "pt": "cachorro"},
  {"en": "book", "pt": "livro"}
]


Também é possível adicionar novos exercícios diretamente na lista EXERCISES dentro do código, seguindo o padrão existente.

🧭 Estrutura dos Exercícios

Cada exercício possui:

{
  "id": "E01",
  "level": "iniciante",
  "title": "Saudações - escolha múltipla",
  "type": "multiple_choice",
  "data": {
      "question": "What is 'olá' in English?",
      "options": ["goodbye", "hello", "please", "thanks"],
      "answer": "hello"
  }
}


Tipos aceitos:

"multiple_choice"

"translation"

"fill_blank"

"reorder"

"match"

"conjugation"

📦 Requisitos

Este projeto não utiliza bibliotecas externas.
Funciona apenas com módulos padrão do Python (json, os, random, datetime, etc.).

🧑‍💻 Autor

Desenvolvido por: Vitor Procópio
Descrição: Focado em criar ferramentas educacionais em Python para aprendizado interativo e acessível.
