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
    "Escolha um local com boa iluminação, use terra rica em nutrientes e comece com plantas fáceis.",
    
    "Quando e como regar as plantas?",
    "Regue de manhã cedo ou à tarde, verificando se o solo está seco ao toque.",
    
    "Erros comuns ao cuidar de uma horta.",
    "Regar em excesso, falta de sol e uso de solo pobre são erros comuns.",
    
    "Quais são os principais cuidados para manter uma horta orgânica?",
    "Use adubos naturais, faça rotação de culturas e controle pragas de forma biológica.",
    
    "Quando devo podar uma planta?",
    "Pode no fim do inverno ou início da primavera, dependendo da espécie.",
    
    "Quais as plantas mais fáceis para começar uma horta em casa?",
    "Alface, cebolinha, salsinha e manjericão são boas opções para iniciantes.",
    
    "Como identificar e controlar pragas de solo?",
    "Verifique sinais de folhas danificadas e use métodos biológicos como predadores naturais.",
    
    "Quais são os melhores métodos para controlar a erosão do solo?",
    "Use cobertura vegetal e faça plantio direto para proteger o solo.",
    
    "Como escolher e aplicar fungicidas de maneira sustentável?",
    "Escolha fungicidas biológicos e aplique de acordo com as instruções, evitando excessos.",
    
    "Como fazer a análise química do solo e interpretar os resultados?",
    "Recolha amostras do solo e envie para um laboratório; os resultados indicam nutrientes e correções necessárias.",
    
    "Como fazer um sistema de irrigação em grande escala?",
    "Instale tubos de gotejamento ou aspersores automáticos, e controle o fluxo de água conforme a necessidade.",
    
    "Quais são as melhores técnicas de rotação de culturas?",
    "Alterne plantas que utilizam diferentes nutrientes do solo e inclua leguminosas para fixar nitrogênio.",
    
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