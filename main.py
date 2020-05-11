from selenium import webdriver
from time import sleep
import os
from colorama import Fore, Back, Style
import json

# from controleJson import jsonQuestion
# controleJson = jsonQuestion()
driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs')
                # dir_path = os.getcwd()
                # print(dir_path)
                # chrome = dir_path+'/chromedriver.exe'
                # options = webdriver.ChromeOptions()
                #     # self.options.add_argument(r"user-data-dir="+self.dir_path+"\profile\wpp")
                # options.add_argument("--log-level=3")
                #driver = webdriver.Chrome(chrome, chrome_options=options)

                #driver.set_window_size(1024, 768) # optional
driver.get('http://pt.akinator.com')
sleep(2) #wait time to scan the code in second

instanciaPergunta = 5

loop = True
lastAswer =""
contPergunta = 0

sleep(3)
descoberta_str = ""
perguntaCapturada =""

 # while loop == True:
#     try:
#         print(driver.find_element_by_class_name('proposal-title').text)
#         loop = False
#     except:
#          try:
#             text = driver.find_element_by_class_name('question-text').text

#             if lastAswer != text and lastAswer != "Carregando..."  and text  != "Carregando..." :
#                 print(text)
#                 lastAswer = text
#                 controleJson.salvarPergunta(instanciaPergunta,text,contPergunta)
#                 loopResposta = True
#             else:
#                print('while')
#                while loopResposta == True:
#                     resposta = controleJson.respostaPergunta(instanciaPergunta,contPergunta)
#                     print(resposta)
#                     if resposta != "":
#                         if resposta == "1":
#                             driver.find_element_by_id('a_yes').click()
#                             contPergunta +1
#                             loopResposta = False
#                         if resposta == "2":
#                             driver.find_element_by_id('a_no').click()
#                             contPergunta +1
#                             loopResposta = False
#                         if resposta == "3":
#                             driver.find_element_by_id('a_dont_know').click()
#                             contPergunta +1
#                             loopResposta = False
#                         if resposta == "4":
#                             driver.find_element_by_id('a_probaly_not').click()
#                             contPergunta +1
#                             loopResposta = False
#                         if resposta == "0":
#                             loopResposta = False

#                     else:
#                         print('resposta vazia')
#                     sleep(0.5)



#          except Exception as error:
#             print('Inside the except block: ' + repr(error))

#     try:
#         if lastAswer=="":
#             driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div[2]/a').click()
#     except:
#         print('erro3')

#     sleep(0.5)

















def startAki():
    try:
        if startGame == "False":
            driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div[2]/a').click()
            startGame = "True"
            print(Fore.Vlue + "Start")
    except Exception as error:
         print(f'{Fore.BLUE}startAki: ' + Fore.RED + repr(error))

def descoberta():
     try:
        descoberta_str = driver.find_element_by_class_name('proposal-title').text
        return True
     except Exception as error:
        return False
        print(f'{Fore.RED}Descoberta: ' + repr(error))

def salvarJson(fname_id,data):
        print("salvarJson")
        with open('../instancia/akinator/aki_'+str(fname_id)+'.json', 'w', encoding='utf8') as outfile:
                json.dump(data, outfile,indent=4,ensure_ascii=False)
        outfile.close()

def salvarPergunta(arq_id,pergunta,pergunta_id):
    print("salvarPergunta")
    json_file = open('../instancia/akinator/aki_'+str(arq_id)+'.json','r', encoding='utf8')
    data = json.load(json_file)
    json_file.close()
    vazio = data['instancia']['perguntas']
    temId =False
    for item in data['instancia']['perguntas']:
        if item['id'] == pergunta_id:
            temId = True

    if temId == False:
        data['instancia']['perguntas'].append({
            "id":pergunta_id,
            "text_pergunta":pergunta,
            "respostar":""
            })
        salvarJson(arq_id,data)
        return ""

def respostaPergunta(arq_id,pergunta_id):
        json_file = open('../instancia/akinator/aki_'+str(arq_id)+'.json','r', encoding='utf8')
        data = json.load(json_file)
        vazio = data['instancia']['perguntas']
        for item in data['instancia']['perguntas']:
            if item['id'] == pergunta_id:
                json_file.close()
                return item['respostar']


def tamanhoArray(arq_id):
    json_file = open('../instancia/akinator/aki_'+str(arq_id)+'.json','r', encoding='utf8')
    data = json.load(json_file)
    return len(data['instancia']['perguntas'])



def capturarPergunta():
     try:
        return driver.find_element_by_class_name('question-text').text
     except Exception as error:
            print(f'{Fore.RED}capturarPergunta: ' + repr(error))


def verificarResposta(_contPergunta):
    try:
        loopResposta =True
        while loopResposta == True:
            resposta = respostaPergunta(instanciaPergunta,_contPergunta)
            print(f"Resposta {resposta} contpergunta {_contPergunta}")

            if resposta != None:
                if resposta == "1":
                    driver.find_element_by_id('a_yes').click()

                    loopResposta = False
                if resposta == "2":
                    driver.find_element_by_id('a_no').click()
                    loopResposta = False
                if resposta == "3":
                    driver.find_element_by_id('a_dont_know').click()
                    loopResposta = False
                if resposta == "4":
                    driver.find_element_by_id('a_probaly_not').click()
                    loopResposta = False
                if resposta == "0":
                    loopResposta = False

            else:
                print(Fore.RED +'resposta vazia')
                loopResposta = False
            sleep(2)
    except Exception as error:
         print(f'{Fore.GREEN}verificarResposta: ' + Fore.RED + repr(error))

startGame = "False"
while loop == True:
    desc = descoberta()
    if desc == True:
        loop = False
        print(Fore.RED +descoberta_str)


    if startGame == "True":
        perguntaCapturada = capturarPergunta()
    sleep(2)

    if lastAswer != "Carregando..."  and perguntaCapturada  != "Carregando...":
        print(Fore.GREEN + 'lastAswer != perguntaCapturada')
        if lastAswer != perguntaCapturada and perguntaCapturada != None:
            lastAswer = perguntaCapturada
            print(Fore.GREEN + f'Pergunta:{perguntaCapturada}')
            salvarPergunta(instanciaPergunta,perguntaCapturada,tamanhoArray(instanciaPergunta))
            sleep(2)
        else:
             verificarResposta(tamanhoArray(instanciaPergunta)-1)
             sleep(2)
        # if perguntaCapturada == None:
        #     startGame ="False"
    try:
        if startGame == "False":
            driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div[2]/a').click()
            startGame = "True"
            print(Fore.BLUE + "Start")
    except Exception as error:
         print(f'{Fore.BLUE}startAki: ' + Fore.RED + repr(error))











#proposal-title
#proposal-subtitle
#a_propose_yes
#a_propose_no

# driver.save_screenshot('screen1.png') # save a screenshot to disk
# # botao_enviar = driver.find_element_by_class_name('btn-play')
# # botao_enviar.click()
# sleep(3)
# driver.save_screenshot('screen.png') # save a screenshot to disk
# sleep(3)
# print(driver.find_element_by_class_name('question-text').text)
# btn = driver.find_element_by_id('a_yes')
# btn.click()
# sleep(3)
# driver.save_screenshot('screen1.png') # save a screenshot to disk
# print(driver.find_element_by_class_name('question-text').text)



#a_yes
#a_no
#a_dont_know
#a_probaly_not
