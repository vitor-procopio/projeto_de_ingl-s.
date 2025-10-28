Projeto de Estudo de Inglês
Um aplicativo CLI (Command Line Interface) interativo para aprendizado de inglês, com mais de 40 exercícios organizados por níveis de dificuldade.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📋 Descrição
Este projeto oferece uma plataforma completa para estudo de inglês, desde o nível iniciante até o avançado, através de exercícios interativos no terminal. O sistema inclui rastreamento de progresso, treinador de vocabulário e organização por níveis de dificuldade.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

✨ Características
+40 exercícios divididos em 3 níveis: iniciante, intermediário e avançado

Múltiplos tipos de exercícios: múltipla escolha, preenchimento, tradução, ordenação, correspondência e conjugação

Sistema de progresso com histórico de acertos

Treinador de vocabulário personalizável

Interface em português para facilitar o uso

Arquivo único - fácil de executar e distribuir


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Como Usar
Pré-requisitos
Python 3.6 ou superior

Execução
bash
python Projeto_Estudo_Ingles.py
Funcionalidades Principais
Menu Principal: Acesso a todas as funcionalidades

Exercícios por Nível: Escolha entre iniciante, intermediário ou avançado

Treinador de Vocabulário: Pratique com palavras básicas (expansível)

Revisão Rápida: Veja seu progresso nos últimos exercícios

Exportação de Progresso: Salve seus dados em arquivo JSON


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📁 Estrutura do Projeto
text
Projeto_Estudo_Ingles.py
├── Configurações e utilitários
├── Base de dados de exercícios (45+)
├── Sistema de execução de exercícios
├── Treinador de vocabulário
├── Sistema de progresso
└── Menu principal interativo
🎯 Tipos de Exercícios
Multiple Choice: Questões de múltipla escolha

Fill Blank: Preenchimento de lacunas

Translation: Tradução português-inglês

Reorder: Ordenação de palavras/frases

Match: Correspondência de pares

Conjugation: Conjugação verbal


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💾 Sistema de Dados
O projeto cria automaticamente uma pasta data_english_study contendo:

progress.json: Histórico de progresso e scores

vocab.json: Lista de vocabulário personalizável


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎮 Controles
Digite q a qualquer momento para voltar ao menu principal

Navegação por números nas opções de menu

Respostas em texto livre ou numéricas


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


🔄 Expansão
O projeto é facilmente expansível:

Adicione novos exercícios no array EXERCISES

Expanda o vocabulário no arquivo vocab.json

Modifique os níveis de dificuldade conforme necessário


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


📊 Progresso
O sistema monitora:

Exercícios completados

Taxa de acertos por exercício

Histórico temporal de prática

Vocabulário estudado
