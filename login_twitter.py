from selenium import webdriver
from time import sleep
from check_pic import CheckProfilePic
from url_id import RetornaIdUrl

driver = webdriver.Edge('')
driver.get('https://twitter.com/login')
driver.maximize_window()


class LoginTwitter:

    def __init__(self, senha, twitter_user):
        self._senha = senha
        self._user = twitter_user

    def executa(self):
        sleep(1)

        driver.find_element_by_name('session[username_or_email]').send_keys(self._user)
        driver.find_element_by_name('session[password]').send_keys(self._senha)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div').click()

        sleep(1)

        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
        sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[2]').click()

        self.__verifica_e_da_unfollow()

    def __unfollow(self, id):
        driver.find_element_by_xpath(
            f'//div[@data-testid="{id}-unfollow"]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]').click()

    def __verifica_e_da_unfollow(self):
        for id in RetornaIdUrl.retorna_lista_id_by_user(self._user):
            if CheckProfilePic().verifica_imagem(id) >= 0.800:
                self.__unfollow(id)
            driver.execute_script("window.scrollBy(0,83)")
