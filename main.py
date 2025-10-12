#!/usr/bin/env python3
"""
Projeto de Estudo de Inglês (iniciante -> avançado)
Arquivo único: Projeto_Estudo_Ingles.py
Descrição: CLI interativo com mais de 40 exercícios, organização por níveis, rastreamento de progresso
Como usar: python Projeto_Estudo_Ingles.py

Observações: código em português, focado em usabilidade e facilidade de estudo.
"""

import json
import os
import random
import sys
import time
from datetime import datetime

# -----------------------------
# Configs e utilitários
# -----------------------------
DATA_DIR = "data_english_study"
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")
VOCAB_FILE = os.path.join(DATA_DIR, "vocab.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

# Progresso do usuário
progress = load_json(PROGRESS_FILE, {
    "last_seen": None,
    "completed": [],
    "scores": {},
})

# Vocabulário básico (pode ser expandido pelo usuário)
vocab_default = [
    {"en": "hello", "pt": "olá"},
    {"en": "goodbye", "pt": "adeus"},
    {"en": "please", "pt": "por favor"},
    {"en": "thank you", "pt": "obrigado"},
    {"en": "yes", "pt": "sim"},
    {"en": "no", "pt": "não"},
    {"en": "house", "pt": "casa"},
    {"en": "water", "pt": "água"},
    {"en": "food", "pt": "comida"},
    {"en": "friend", "pt": "amigo"},
]

vocab = load_json(VOCAB_FILE, vocab_default)

# -----------------------------
# Exercícios (mais de 40) organizados por nível
# Cada exercício é um dict com: id, level, title, type, data
# types: multiple_choice, fill_blank, translation, reorder, match, conjugation
# -----------------------------
EXERCISES = [
    # Iniciante (1-15)
    {"id": "E01", "level": "iniciante", "title": "Saudações - escolha múltipla", "type": "multiple_choice",
     "data": {"question": "What is 'olá' in English?", "options": ["goodbye", "hello", "please", "thanks"], "answer": "hello"}},
    {"id": "E02", "level": "iniciante", "title": "Traduza - palavra simples", "type": "translation",
     "data": {"question": "Por favor", "answer": ["please"]}},
    {"id": "E03", "level": "iniciante", "title": "Sim ou Não", "type": "multiple_choice",
     "data": {"question": "How do you say 'sim' in English?", "options": ["yes", "no", "maybe", "later"], "answer": "yes"}},
    {"id": "E04", "level": "iniciante", "title": "Construa a frase - 1", "type": "reorder",
     "data": {"question": "ordenar: 'I / am / student'", "answer": "I am student"}},
    {"id": "E05", "level": "iniciante", "title": "Artigos básicos", "type": "multiple_choice",
     "data": {"question": "Escolha o artigo correto: ___ apple", "options": ["a", "an", "the", "no article"], "answer": "an"}},
    {"id": "E06", "level": "iniciante", "title": "Vocabulário - casa", "type": "translation",
     "data": {"question": "Translate: 'casa'", "answer": ["house", "home"]}},
    {"id": "E07", "level": "iniciante", "title": "Verbo to be - escolha", "type": "multiple_choice",
     "data": {"question": "Complete: I ___ a teacher.", "options": ["is", "are", "am", "be"], "answer": "am"}},
    {"id": "E08", "level": "iniciante", "title": "Pronomes pessoais", "type": "match",
     "data": {"pairs": [["I", "eu"], ["You", "você"], ["He", "ele"], ["We", "nós"]]}},
    {"id": "E09", "level": "iniciante", "title": "Números 1-10", "type": "translation",
     "data": {"question": "Translate: 'cinco'", "answer": ["five"]}},
    {"id": "E10", "level": "iniciante", "title": "Perguntas básicas - where", "type": "multiple_choice",
     "data": {"question": "How do you ask 'Onde você mora?'", "options": ["Where do you live?", "What are you doing?", "How old are you?", "Do you live?"], "answer": "Where do you live?"}},
    {"id": "E11", "level": "iniciante", "title": "Dias da semana - reorder", "type": "reorder",
     "data": {"question": "ordenar: 'Monday / Sunday / Saturday' (coloque em ordem correta)", "answer": "Sunday Monday Saturday"}},
    {"id": "E12", "level": "iniciante", "title": "Expressões polidas", "type": "translation",
     "data": {"question": "Translate: 'obrigado' (forma masculina)", "answer": ["thank you", "thanks"]}},
    {"id": "E13", "level": "iniciante", "title": "Colors - multiple choice", "type": "multiple_choice",
     "data": {"question": "What is 'vermelho'?", "options": ["blue", "red", "green", "yellow"], "answer": "red"}},
    {"id": "E14", "level": "iniciante", "title": "Frases negativas com to be", "type": "fill_blank",
     "data": {"question": "I ___ not a doctor. (use 'am/is/are')", "answer": "am"}},
    {"id": "E15", "level": "iniciante", "title": "Family vocabulary", "type": "match",
     "data": {"pairs": [["Mother", "mãe"], ["Father", "pai"], ["Brother", "irmão"], ["Sister", "irmã"]]}},

    # Intermediário (16-35)
    {"id": "E16", "level": "intermediario", "title": "Present Simple - completar", "type": "fill_blank",
     "data": {"question": "She ___ (work) every day.", "answer": "works"}},
    {"id": "E17", "level": "intermediario", "title": "Past Simple - escolha", "type": "multiple_choice",
     "data": {"question": "Choose past of 'go'", "options": ["goed", "went", "gone", "goes"], "answer": "went"}},
    {"id": "E18", "level": "intermediario", "title": "Prepositions - fill", "type": "fill_blank",
     "data": {"question": "I live ___ Brazil.", "answer": "in"}},
    {"id": "E19", "level": "intermediario", "title": "Phrasal Verb - match", "type": "match",
     "data": {"pairs": [["give up", "desistir"], ["look for", "procurar"], ["turn on", "ligar"]]}},
    {"id": "E20", "level": "intermediario", "title": "Comparativos", "type": "multiple_choice",
     "data": {"question": "Which is correct: 'My car is ___ than yours'", "options": ["more fast", "faster", "fastest", "most fastest"], "answer": "faster"}},
    {"id": "E21", "level": "intermediario", "title": "Question tags", "type": "multiple_choice",
     "data": {"question": "You like coffee, ___?", "options": ["don't you", "do you", "aren't you", "did you"], "answer": "don't you"}},
    {"id": "E22", "level": "intermediario", "title": "Make sentences - reorder", "type": "reorder",
     "data": {"question": "ordenar: 'visited / last / I / Paris'", "answer": "I visited Paris last"}},
    {"id": "E23", "level": "intermediario", "title": "Modal verbs - fill", "type": "fill_blank",
     "data": {"question": "You ___ (should) study more.", "answer": "should"}},
    {"id": "E24", "level": "intermediario", "title": "Gerúndio vs Infinitivo", "type": "multiple_choice",
     "data": {"question": "I enjoy ___ (to swim/swimming)", "options": ["to swim", "swimming", "swim", "swam"], "answer": "swimming"}},
    {"id": "E25", "level": "intermediario", "title": "Vocabulário - trabalho", "type": "translation",
     "data": {"question": "Translate: 'emprego'", "answer": ["job", "employment"]}},
    {"id": "E26", "level": "intermediario", "title": "Reading curto - compreensão", "type": "translation",
     "data": {"question": "Leia: 'Anna lives in London. She has a cat.' Pergunta: 'Where does Anna live?'", "answer": ["London"]}},
    {"id": "E27", "level": "intermediario", "title": "Conversão de tempo verbal", "type": "conjugation",
     "data": {"question": "Simple present -> third person: 'to have'", "answer": "has"}},
    {"id": "E28", "level": "intermediario", "title": "Preposições de tempo", "type": "multiple_choice",
     "data": {"question": "Escolha: 'I will see you ___ Monday'", "options": ["in", "on", "at", "by"], "answer": "on"}},
    {"id": "E29", "level": "intermediario", "title": "Colocations comuns", "type": "match",
     "data": {"pairs": [["make a decision", "tomar uma decisão"], ["have a break", "fazer uma pausa"], ["take a photo", "tirar uma foto"]]}},
    {"id": "E30", "level": "intermediario", "title": "Reported speech - transformar", "type": "fill_blank",
     "data": {"question": "She said: 'I am tired' -> He said he ___ tired.", "answer": "was"}},
    {"id": "E31", "level": "intermediario", "title": "Expressões idiomáticas simples", "type": "translation",
     "data": {"question": "Translate: 'break the ice'", "answer": ["quebrar o gelo", "começar uma conversa"]}},

    # Avançado (32-45+)
    {"id": "E32", "level": "avancado", "title": "Conditionals - first", "type": "fill_blank",
     "data": {"question": "If it ___ (rain) tomorrow, I will stay home.", "answer": "rains"}},
    {"id": "E33", "level": "avancado", "title": "Passive voice", "type": "multiple_choice",
     "data": {"question": "The letter ___ (send) yesterday.", "options": ["was sent", "sent", "is sent", "had sent"], "answer": "was sent"}},
    {"id": "E34", "level": "avancado", "title": "Phrasal verbs avançados", "type": "match",
     "data": {"pairs": [["look forward to", "ansiar por"], ["put up with", "tolerar"], ["come up with", "inventar"]]}},
    {"id": "E35", "level": "avancado", "title": "Collocations avançadas", "type": "multiple_choice",
     "data": {"question": "Choose correct collocation: 'strong ___'", "options": ["friend", "coffee", "opinion", "wind"], "answer": "opinion"}},
    {"id": "E36", "level": "avancado", "title": "Inferred meaning - leitura", "type": "translation",
     "data": {"question": "Leia: 'Despite the rain, the festival went ahead.' Pergunta: 'Did the festival happen?'", "answer": ["yes", "it went ahead"]}},
    {"id": "E37", "level": "avancado", "title": "Formal vs Informal", "type": "multiple_choice",
     "data": {"question": "Choose formal option for 'give me'", "options": ["provide", "gimme", "lend", "take"], "answer": "provide"}},
    {"id": "E38", "level": "avancado", "title": "Advanced grammar - subjunctive (prática)", "type": "fill_blank",
     "data": {"question": "I suggest that he ___ (be) present.", "answer": "be"}},
    {"id": "E39", "level": "avancado", "title": "Word formation", "type": "multiple_choice",
     "data": {"question": "Choose noun form of 'decide'", "options": ["decision", "decide", "decisive", "decider"], "answer": "decision"}},
    {"id": "E40", "level": "avancado", "title": "Register and tone", "type": "translation",
     "data": {"question": "Translate: 'Could you possibly send the report?' Qual é o tom?", "answer": ["formal", "pedido educado"]}},
    {"id": "E41", "level": "avancado", "title": "Advanced reading - infer meaning 2", "type": "translation",
     "data": {"question": "Leia: 'He barely scraped by.' Pergunta: 'What does it mean?'", "answer": ["ele mal se virou", "teve pouca verba"]}},
    {"id": "E42", "level": "avancado", "title": "Academic vocabulary", "type": "match",
     "data": {"pairs": [["analyze", "analisar"], ["evidence", "evidência"], ["theory", "teoria"]]}},
    {"id": "E43", "level": "avancado", "title": "Paraphrase", "type": "translation",
     "data": {"question": "Paraphrase: 'He failed to arrive on time' -> write another way", "answer": ["He didn't arrive on time", "He was late"]}},
    {"id": "E44", "level": "avancado", "title": "Debate prompt - escrita", "type": "translation",
     "data": {"question": "Escreva 2 frases defendendo: 'Online education is effective'", "answer": []}},
    {"id": "E45", "level": "avancado", "title": "Idioms avançados", "type": "multiple_choice",
     "data": {"question": "What does 'to bite the bullet' mean?", "options": ["to avoid something", "to face a difficult situation", "to eat quickly", "to run away"], "answer": "to face a difficult situation"}},
]

# -----------------------------
# Core do app: funções para executar exercícios
# -----------------------------


def show_header():
    print("\n=== PROJETO DE ESTUDO DE INGLÊS — iniciante → avançado ===")
    print("Dica: digite 'q' a qualquer momento para voltar ao menu principal.\n")


def choose_level():
    levels = ["iniciante", "intermediario", "avancado"]
    print("Escolha o nível:")
    for i, lv in enumerate(levels, 1):
        print(f"{i}. {lv}")
    choice = input("Nível (número): ").strip()
    if choice.lower() == 'q':
        return None
    try:
        idx = int(choice) - 1
        return levels[idx]
    except Exception:
        print("Escolha inválida. Tente novamente.")
        return choose_level()


def list_exercises(level=None):
    filtered = [e for e in EXERCISES if (level is None or e['level'] == level)]
    print(f"\n{len(filtered)} exercícios encontrados para o nível: {level if level else 'todos'}")
    for e in filtered:
        print(f"{e['id']}: {e['title']}")
    return filtered


def input_answer(prompt):
    ans = input(prompt).strip()
    if ans.lower() == 'q':
        raise KeyboardInterrupt
    return ans


def run_multiple_choice(ex):
    q = ex['data']['question']
    opts = ex['data']['options']
    ans = ex['data']['answer']
    print('\n' + q)
    for i, o in enumerate(opts, 1):
        print(f"  {i}. {o}")
    choice = input_answer("Escolha (número ou texto): ")
    # aceitar número ou texto
    if choice.isdigit():
        idx = int(choice) - 1
        selected = opts[idx] if 0 <= idx < len(opts) else ''
    else:
        selected = choice
    correct = selected.strip().lower() == ans.strip().lower()
    return correct, ans


def run_fill_blank(ex):
    q = ex['data']['question']
    ans = ex['data']['answer']
    print('\n' + q)
    choice = input_answer("Resposta: ")
    correct = choice.strip().lower() == ans.strip().lower()
    return correct, ans


def run_translation(ex):
    q = ex['data']['question']
    answers = ex['data'].get('answer', [])
    print('\nTraduza / responda: ' + q)
    choice = input_answer("Resposta (em inglês): ")
    ok = any(choice.strip().lower() == a.strip().lower() for a in answers) if answers else None
    return ok, answers


def run_reorder(ex):
    q = ex['data']['question']
    ans = ex['data']['answer']
    print('\nOrdene para formar a frase correta: ' + q)
    choice = input_answer("Escreva a frase ordenada: ")
    correct = choice.strip().lower() == ans.strip().lower()
    return correct, ans


def run_match(ex):
    pairs = ex['data']['pairs']
    print('\nFaça o pareamento: escreva as correspondências como "1-a,2-b"')
    left = [p[0] for p in pairs]
    right = [p[1] for p in pairs]
    random.shuffle(right)
    for i, l in enumerate(left, 1):
        print(f"{i}. {l}")
    for j, r in enumerate(right, 1):
        print(f"{chr(96+j)}. {r}")
    choice = input_answer("Correspondências: ")
    # Simplificado: aceitar se todas as correspondências corretas estiverem nas respostas (verificação leve)
    normalized = choice.replace(' ', '').lower()
    ok = True
    for i, l in enumerate(left, 1):
        correct_r = pairs[i-1][1].lower()
        if correct_r not in normalized:
            ok = False
    return ok, pairs


def run_conjugation(ex):
    q = ex['data']['question']
    ans = ex['data']['answer']
    print('\n' + q)
    choice = input_answer("Resposta: ")
    correct = choice.strip().lower() == ans.strip().lower()
    return correct, ans


RUNNERS = {
    'multiple_choice': run_multiple_choice,
    'fill_blank': run_fill_blank,
    'translation': run_translation,
    'reorder': run_reorder,
    'match': run_match,
    'conjugation': run_conjugation,
}


def run_exercise(ex):
    runner = RUNNERS.get(ex['type'])
    if not runner:
        print("Exercício com tipo desconhecido.")
        return False
    try:
        correct, ans = runner(ex)
    except KeyboardInterrupt:
        print('\nVoltando ao menu...')
        return None
    if correct is None:
        print("Não há resposta esperada (exercício aberto). Avalie sua resposta manualmente.")
        score = 0
    else:
        if correct:
            print("✅ Correto!")
            score = 1
        else:
            print(f"❌ Incorreto. Resposta esperada: {ans}")
            score = 0
    # salvar progresso rápido
    progress['last_seen'] = datetime.utcnow().isoformat()
    progress['completed'].append({'id': ex['id'], 'time': progress['last_seen'], 'score': score})
    progress['scores'][ex['id']] = progress['scores'].get(ex['id'], 0) + score
    save_json(PROGRESS_FILE, progress)
    return correct


# -----------------------------
# Funções extras: treino de vocabulário, revisão espaçada simples
# -----------------------------


def vocab_trainer(n=10):
    print('\n=== Treinador de Vocabulário ===')
    pool = vocab.copy()
    random.shuffle(pool)
    pool = pool[:n]
    correct = 0
    for item in pool:
        ans = input_answer(f"Traduza para o inglês: '{item['pt']}': ")
        if ans.strip().lower() == item['en'].lower():
            print("✅")
            correct += 1
        else:
            print(f"❌ - Resposta correta: {item['en']}")
    print(f"Você acertou {correct}/{len(pool)}")


def quick_review():
    print('\n=== Revisão rápida (últimos 10 exercícios) ===')
    last = progress.get('completed', [])[-10:]
    if not last:
        print('Nenhum exercício feito ainda.')
        return
    for it in last:
        print(f"{it['id']} - score: {it['score']} - {it['time']}")


# -----------------------------
# Menu principal
# -----------------------------

def main_menu():
    show_header()
    while True:
        print('\nMenu principal:')
        print('1. Escolher nível e fazer exercício')
        print('2. Listar exercícios por nível')
        print('3. Treinador de vocabulário')
        print('4. Revisão rápida (progresso)')
        print('5. Exportar progresso')
        print('6. Sair')
        choice = input('Escolha: ').strip()
        if choice == '1':
            level = choose_level()
            if not level:
                continue
            filtered = [e for e in EXERCISES if e['level'] == level]
            print('\nEscolha um exercício:')
            for i, e in enumerate(filtered, 1):
                print(f"{i}. {e['id']} - {e['title']}")
            sel = input('Número do exercício: ').strip()
            if not sel.isdigit():
                print('Entrada inválida.')
                continue
            idx = int(sel) - 1
            if idx < 0 or idx >= len(filtered):
                print('Número fora do intervalo.')
                continue
            ex = filtered[idx]
            run_exercise(ex)

        elif choice == '2':
            lvl = choose_level()
            if not lvl:
                continue
            list_exercises(lvl)
        elif choice == '3':
            vocab_trainer()
        elif choice == '4':
            quick_review()
        elif choice == '5':
            path = input('Nome do arquivo para exportar (ex: progresso_export.json): ').strip()
            if path:
                save_json(path, progress)
                print(f'Progresso exportado para {path}')
        elif choice == '6':
            print('Até mais! Boa prática :)')
            break
        else:
            print('Escolha inválida. Tente novamente.')


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print('\nInterrompido. Até logo!')
