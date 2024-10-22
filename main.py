from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
from spacy.cli import download

download("en_core_web_sm")
nltk.download('punkt')
nltk.download('punkt_tab')

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
    ENGLISH_NAME = 'English'
    ISO_639 = 'en'

chatbot = ChatBot('Mavin', tagger_language=ENGSM)

conversa = [
    "Olá, tenho uma dúvida",
    "Olá, meu nome é Marvin. Qual a sua dúvida?",
    "Como começar uma horta em casa?",
    "",
    "Como você se chama?",
    "Meu nome é Marvin",
    "Qual a sua idade?",
    "Sou um bot, meu criador me criou em 2024-10-21"
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

#chatbot.storage.drop() #-- para limpar memória do boot
while True:
    mensagem = input("Mande uma mensagem para o chatbot:")
    if mensagem == 'parar':
        print("Encerrando conversa")
        break
    response = chatbot.get_response(mensagem)
    print('---', response, '---')