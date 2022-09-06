from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

chave_de_seguranca = ['expand','scout','sport','news','soda','weapon','rack','record','forward','diagram','scrub','involve','131412TI','131412TI']
lista_formulario1 = ['import-srp__srp-word-0','import-srp__srp-word-1',
                'import-srp__srp-word-2','import-srp__srp-word-3',
                'import-srp__srp-word-4','import-srp__srp-word-5',
                'import-srp__srp-word-6','import-srp__srp-word-7',
                'import-srp__srp-word-8','import-srp__srp-word-9',
                'import-srp__srp-word-10','import-srp__srp-word-11',
                'password','confirm-password']

lista_dados_BSC = ['Smart Chain','https://bsc-dataseed.binance.org/','56','BNB','https://bscscan.com']

class RoboPositionExchange:

    def __init__(self,chave_de_seguranca,lista_formulario1,lista_dados_BSC):

        self.driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())
        self.driver.install_addon('C:\\Users\\Marcos\Desktop\\robo do milhao\\metamask-10.12.4-an+fx.xpi')
        self.chave_de_seguranca = chave_de_seguranca
        self.lista_formulario1 = lista_formulario1
        self.lista_dados_BSC = lista_dados_BSC

    def fecha_janela(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def primeiros_passos_btn_primary(self,botao):
        time.sleep(3)
        while len(self.driver.find_elements_by_class_name(botao)) != 0 and self.driver.find_element_by_class_name(botao).is_enabled():
            self.clicar_by_class_name(botao)
        
    def clicar_by_class_name(self,botao):
        self.driver.find_element_by_class_name(botao).click()

    def formulario_keys_metamask(self,formulario,chave):
        for i, form in enumerate(formulario):
            self.driver.find_element_by_id(formulario[i]).send_keys(chave[i])
        self.driver.find_element_by_id('create-new-vault__terms-checkbox').click()
        self.driver.find_element_by_class_name('create-new-vault__form').submit()

    def rede_bsc_na_metamask(self):
        self.lista_formulario2 = self.driver.find_elements_by_class_name('form-field__input')
        for x, form2 in enumerate(self.lista_formulario2):
            self.driver.find_element_by_class_name('form-field__input')
            self.lista_formulario2[x].send_keys(self.lista_dados_BSC[x])
            time.sleep(0.2)
    
    def trocar_janela(self,num = 0):
        while len(self.driver.window_handles) != 2:
                time.sleep(0.01)
        self.escolher_janela(num)
    
    def escolher_janela(self,num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def entrar_site_position(self):
        self.driver.get('https://app.position.exchange/farming')
    
    def aguardar_para_clicar_by_xpath(self,botao):

        while len(self.driver.find_elements_by_xpath(botao)) != 1:
            if not self.driver.find_element_by_xpath(botao).is_enabled():
                time.sleep(0.1)
        self.driver.find_element_by_xpath(botao).click()
    
    def aguardar_para_clicar_class_name(self,botao):
            while len(self.driver.find_elements_by_class_name(botao)) != 1:
                time.sleep(0.01)
            self.clicar_by_class_name(botao)

#INSTANCIA DA CLASSE 
Roboposition = RoboPositionExchange(lista_formulario1,chave_de_seguranca,lista_dados_BSC)
#fecha a primeira aba aberta
Roboposition.fecha_janela()
#clica em todos botões com nome primary
Roboposition.primeiros_passos_btn_primary('btn-primary')
#preenche as keys da metamask
Roboposition.formulario_keys_metamask(lista_formulario1,chave_de_seguranca)
Roboposition.aguardar_para_clicar_class_name('button.btn--rounded.btn-primary.first-time-flow__button')
time.sleep(2)
Roboposition.clicar_by_class_name('fas.fa-times.popover-header__button')
Roboposition.clicar_by_class_name('network-display__icon')
Roboposition.clicar_by_class_name('btn--rounded')
#adiciona a rede BSC na metamask
Roboposition.rede_bsc_na_metamask()
#entra no site da position exchange
Roboposition.entrar_site_position()
Roboposition.aguardar_para_clicar_by_xpath('//button[@title="Close"]')
Roboposition.clicar_by_class_name('css-9fnpzn')
Roboposition.clicar_by_class_name('css-1h74k4x')
#sincroniza a metamask no site
Roboposition.trocar_janela(1)
Roboposition.primeiros_passos_btn_primary('btn-primary')
Roboposition.primeiros_passos_btn_primary('btn-primary')
Roboposition.escolher_janela(0)
#aguarda o botao claim habilitar para realizar o click
Roboposition.aguardar_para_clicar_class_name('css-lwmkhd')
Roboposition.aguardar_para_clicar_class_name('css-1kblcjz')
Roboposition.aguardar_para_clicar_class_name('css-1wr5kox')
Roboposition.trocar_janela(1)
#faz as confirmações da transação
Roboposition.aguardar_para_clicar_class_name('btn-primary')
time.sleep(3)
#volta no site da position e clica em view in BSCscan
Roboposition.escolher_janela(0)
time.sleep(10)
Roboposition.aguardar_para_clicar_class_name('css-1ydplb0')