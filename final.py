import csv
import os
import time
score = 0

def start():
  os.system("cls")
  print('''  --------------------------------------------------------
           Olá, esse é um quiz sobre educação!
  ---------------------------------------------------------
  Esse quiz possui 3 níveis de difilcudade e você pode escolher das opções abaixo o que você quer fazer?
  Digite o número referente ao que quer fazer:
  ''')
  time.sleep(2)
  option1()


def option1():
  # Definindo as dificuldades do quiz
  menuInicial = int(input('''  1- Para escolher o nível fácil e jogar o quiz nesse nível
  2- Para escolher o nível médio e jogar o quiz nesse nível
  3- Para escolher o nível difícil e jogar o quiz nesse nível
  4- Para adicionar uma pergunta a um dos níveis do quiz
  5- Para remover uma pergunta do quiz
  0- Sair  
  '''))
  if menuInicial == 1:
    print("Ótima escolha, o primeiro degrau da escada é sempre o mais dificil. Vamos lá!")
    time.sleep(1)
    print("Quiz abrindo...")
    time.sleep(3)
    quizFacil()

  elif menuInicial == 2:
    print("Esse é o nível médio, teremos mais complexidade, está pronto? ")
    time.sleep(1)
    print("Vamos lá...")
    time.sleep(3)
    quizMedio()

  elif menuInicial == 3:
    print("WOW, você gosta de desafios ou já é um expert!")
    time.sleep(1)
    print("Quiz abrindo...")
    time.sleep(3)
    quizDificil()

  elif menuInicial == 4:
        os.system("cls")
        addQuestions()

  elif menuInicial == 5:
        os.system("cls")
        removeQuestion()

  elif menuInicial == 0:
        os.system("cls")
        print("Até a próxima! :)")

  else:
    print("Você digitou alguma coisa errada! :(")
    time.sleep(2)
    print("Por favor digite algumas das opções do menu.")
    option1()



def quizDificil():
  global score
  score = 0
# Abrindo o arquivo csv e lendo as perguntas
  with open('perguntasDificil.csv', 'r') as csvfile:
    with open('arquivo_saida.csv', 'w') as csvSaida:
      linhas = csv.reader(csvfile, delimiter=',')

# Imprimindo as questões e as alternativas
    for q in linhas:
      question = q[0]
      alternativas = (q[1],q[2],q[3],q[4])
      time.sleep (2)
      print ('''
        {}
        {} 
        {}
        {}
        {}
        '''.format(alternativas[0], alternativas[1], alternativas[2], alternativas[3]))
      respostaCerta = q[5]
      respostaJogador = input("Qual a resposta certa?").lower()
      time.sleep (2)
      print("A resposta certa é a",respostaCerta)
      if respostaJogador == respostaCerta:
        print("Você acertou!")
        time.sleep(2)
        score = score + 3
        print("Seu total de pontos é",score)
        print("Carregando....")
        time.sleep (3)
        
      else:
        print("Poxa, você errou, continue tentando!")
        time.sleep(2)
        print("Não tem problema errar, você também pode aprender com o erro.")
        time.sleep (2)
        print("Olhe os seus",score,"pontos e tente melhorar!")
        time.sleep (2)
        print("Você pode tentar ser melhor na próxima.")
        print("Continuando...")
        time.sleep (3)
  # Após 4 questões o jogo acaba e pergunta se quer começar de novo 
    print("Fim das questões")
    time.sleep (2)
    option = input("Quer jogar outra rodada ou sair? 1- Para jogar outra | 2- Para sair")
    if option == 1:
      option1()
    elif option == 2:
      print("Até a próxima!")
      print("")
    elif option != 1 or 2 :
      print("Você digitou alguma coisa errada! :(")
      time.sleep (2)
      print("Por favor digite 1 ou 2")
      return option 


  # se o jogador fez mais que 12 pontos ele conclui a etapa mnais difícil do quiz      
    elif score > 12:
      print("Parabéns!!! Você conseguiu acertar todas as questões!")
      time.sleep (2)
      print("Você somou",score,"pontos e podemos dizer que você já pode argumentar pontos de vistas reais sobre a educação e suas teorias do conhecimento.")
      time.sleep (2)
      print("Até a próxima, Tchau! :)")
      print("")

def quizMedio():
  global score
  score = 0
#Abrindo o arquivo csv e lendo as perguntas
  with open('perguntasMedio.csv', 'r') as csvfile:
    with open('arquivo_saida.csv', 'w') as csvSaida:

     linhas = csv.reader(csvfile, delimiter=',')

#Imprimindo as questões e as alternativas
    for q in linhas:
      question = q[0]
      print('''{}'''.format(question))
      alternativas = (q[1],q[2],q[3],q[4])
      time.sleep (2)
      print ('''
        {} 
        {}
        {}
        {}
        '''.format(alternativas[0], alternativas[1], alternativas[2], alternativas[3]))
      respostaCerta = q[5]
      respostaJogador = input("Qual a resposta certa?").lower()
      time.sleep (2)
      print("A resposta certa é a",respostaCerta)
      if respostaJogador == respostaCerta:
        print("Você acertou!")
        time.sleep(2)
        score = score + 3
        print("Seu total de pontos é",score)
        print("Carregando....")
        time.sleep (3)
        
      else:
        print("Poxa, você errou, continue tentando!")
        time.sleep(2)
        print("Não tem problema errar, você também pode aprender com o erro.")
        time.sleep (2)
        print("Olhe os seus",score,"pontos e tente melhorar!")
        time.sleep (2)
        print("Você pode tentar ser melhor na próxima.")
        print("Continuando...")
        time.sleep (3)
  # Após 4 questões o jogo acaba e pergunta se quer começar de novo 
    print("Fim das questões")
    time.sleep (2)
    option = input("Quer jogar outra rodada ou sair? 1- Para jogar outra | 2- Para sair")
    if option == 1:
      option1()
    elif option == 2:
      print("goodbye")
      print("")
    elif option != 1 or 2 :
      print("Você digitou alguma coisa errada! :(")
      time.sleep (2)
      print("Por favor digite 1 ou 2")
      option 


  # se o jogador fez mais que 6 pontos o quiz pergunta se quer ir para outro nível        
    elif score > 6:
      print("Parabéns!!! Você conseguiu passe livre para o próximo nível!")
      time.sleep (2)
      print("Você somou",score,"pontos")
      time.sleep (2)
      option3 = input("Quer ir para o próximo nível? Digite s- para sim ou n - para não").lower()
      if option3 == "s":
        quizDificil()
          
      elif option3 == "n":
        time.sleep (2)
        print("goodbye")
        print("")


def quizFacil():
  global score
  score = 0


# Abrindo o arquivo csv e lendo as perguntas
  with open('perguntasFacil.csv', 'r') as csvfile:
    with open('arquivo_saida.csv', 'w') as csvSaida:

      linhas = csv.reader(csvfile, delimiter=',')

# Imprimindo as questões e as alternativas
      for q in linhas:
        question = q[0]
        print('''{}'''.format(question))
      alternativas = (q[1],q[2],q[3],q[4])
      time.sleep (2)
      print ('''
            {} 
            {}
            {}
            {}
            '''.format(alternativas[0], alternativas[1], alternativas[2], alternativas[3]))
      respostaCerta = q[5]
      respostaJogador = input("Qual a resposta certa?").lower()
      time.sleep(2)
      print("A resposta certa é a", respostaCerta)
      if respostaJogador == respostaCerta:
          print("Você acertou!")
          time.sleep(2)
          score = score + 3
          print("Seu total de pontos é", score)
          print("Carregando....")
          time.sleep(3)

      else:
          print("Poxa, você errou, continue tentando!")
          time.sleep(2)
          print("Não tem problema errar, você também pode aprender com o erro.")
          time.sleep(2)
          print("Olhe os seus", score, "pontos e tente melhorar!")
          time.sleep(2)
          print("Você pode tentar ser melhor na próxima.")
          print("Continuando...")
          time.sleep(3)
    # Após 4 questões o jogo acaba e pergunta se quer começar de novo
    print("Fim das questões")
    time.sleep(2)
    option = input(
        "Quer jogar outra rodada ou sair? 1- Para jogar outra | 2- Para sair")
    if option == 1:
        option1()
    elif option == 2:
        print("goodbye")
        print("")
    elif option != 1 or 2:
        print("Você digitou alguma coisa errada! :(")
        time.sleep(2)
        print("Por favor digite 1 ou 2")
        option


# se o jogador fez mais que 6 pontos o quiz pergunta se quer ir para outro nível
    elif score > 6:
      print("Parabéns!!! Você conseguiu passe livre para o próximo nível!")
      time.sleep (2)
      print("Você somou",score,"pontos")
      time.sleep (2)
      option3 = input("Quer ir para o próximo nível? Digite s- para sim ou n - para não").lower()
      if option3 == "s":
        quizMedio()
          
      elif option3 == "n":
        time.sleep (2)
        print("goodbye")
        print("")

def delete_line(filename, line_number):
    with open(filename, 'r', encoding='utf-8') as file:
      lines = file.readlines()

  
    if (line_number <= len(lines)):
      del lines[line_number - 1]
      with open(filename, "w") as file:
        for line in lines:
          file.write(line)

    else:
      print("Line", line_number, "not in file.")
      print("File has", len(lines), "lines.")

def removeQuestion():
   os.system("cls")
   question_file = int(input('''De qual destes quiz você gostaria de remover a pergunta?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
    - '''))
  
   if question_file == 1:
        delete_filename = 'easy.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
          print('''{}
          '''.format(question))
        delete_line_number = int(input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
   elif question_file == 2:
        delete_filename = 'medium.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
          print('''{}
          '''.format(question))
        delete_line_number = int(input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
   elif question_file == 3:
        delete_filename = 'hard.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
          print('''{}
          '''.format(question))
        delete_line_number = int(input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
   else:
        print("Digite uma opção válida.")
        removeQuestion()  

def addQuestions():
    os.system("cls")
    question_level_add = int(input('''Você gostaria de adicionar questões de que nível?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
    - '''))
    if question_level_add == 1:
      csvfile = open('easy.csv', 'a', newline="")
    elif question_level_add == 2:
      csvfile = open('medium.csv', 'a', newline="")
    elif question_level_add == 3:
      csvfile = open('hard.csv', 'a', newline="")
    else:
      print("Escolha uma opção de adicionar válida.")
      addQuestions()

    question = input("Escreva aqui sua pergunta: ")
    answer1 = input('''Escreva aqui a primeira opção de alternativa:
    Ex.: A)Programação
    ''')
    answer2 = input('''Escreva aqui a segunda opção de alternativa:
    Ex.: B)Livros
    ''')
    answer3 = input('''Escreva aqui a terceira opção de alternativa:
    Ex.: C)Sapatos
    ''')
    answer4 = input('''Escreva aqui a quarta opção de alternativa:
    Ex.: D)Brinquedos
    ''')
    correctAnswer = input('''Agora escreva a letra da alternativa correta:
    Ex.: A
    ''')
    questions_and_answers = (question, answer1, answer2, answer3, answer4, correctAnswer)
    writer = csv.writer(csvfile)
    writer.writerow(questions_and_answers)
    print("Questão registrada. Obrigada!")
    csvfile.close()
    start()



start()