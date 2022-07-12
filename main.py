from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from datetime import timedelta, datetime
from tqdm import tqdm
import playsound
import smtplib
import os

ADDRESS = r'https://row2.vfsglobal.com/PolandBelarus-Appointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/ASnHZRMROGDyz5YljrTPrmD7weWKDzHm/9+x4kyou3TsMOg99oc+0bfYTDhNi8VXO2A4zs7wBkyB6b15tURU2eT0aS3CJYjFGR6LRWzfcsZ5BzitruEIjN+SeHc17EKqO0YlhR3T0Pc1cO5uD69/WY='



class Find_visa:

    NOT_WORK = 1
    AUTORIZATION = 2
    SELECT_FIND_VISA = 3
    FIND_VISA = 4
    ENTER_ADDRESS = 5
    THERE_ARE_PLACES = 6
    STOP = 7
    SCROLL_AUTORIZATION = 8

    LOG = 'my.log'


    def __init__(self, name_file, address, config):
        self.name_file = name_file
        self.status = None
        self.address = address
        load_dotenv(config)


    def logging(self, text):
        print(datetime.now(), text)
        print(datetime.now(), text, file=self.log)


    def send_email(self):
        EMAIL_FROM = os.getenv('EMAIL_FROM')
        PASSWORD_FROM = os.getenv('PASSWORD_FROM')
        EMAIL_TO = os.getenv('EMAIL_TO')
        if EMAIL_FROM and PASSWORD_FROM and EMAIL_TO:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login(EMAIL_FROM, PASSWORD_FROM)
            smtpObj.sendmail(EMAIL_FROM, EMAIL_TO, 'Hooray! There are places for a visa!')
            smtpObj.quit()


    def find_visa(self, list_sity):
        pass
        # run = True
        # while run:
        #     for i in list_sity:
        #         self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #         coords = self.wait_element('static/select_city_check.png', 30, region=(350,450,200,200))
        #         if coords:
        #             click(coords.x + 250, coords.y-7)  # выбор визового центра
        #         else:
        #             self.status = None
        #             run = False
        #             break
        #         coords = self.wait_element('static/' + str(i) + '.png',300)
        #         if coords:
        #             click(coords)  # нажимаем на визовый центр
        #         self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #         if self.check_text('Нет доступных мест', 10):
        #             self.logging('Нет мест в центре ' + str(i))
        #         else:
        #             self.logging('Пробую выбрать категорию визы')
        #             coords = self.wait_element('static/category_record.png',5, region=(400, 420, 300,230))
        #             if coords:
        #                 click(coords.x + 300, coords.y)
        #                 moveTo(0,200)
        #             if self.wait_element('static/select_record_category.png',5, region=(420, 320, 730,330)):
        #                 self.logging('Похоже сайт не работает.')
        #                 self.status = self.ENTER_ADDRESS
        #                 run = False
        #                 break
        #             coords = self.wait_element('static/karta_polaka_visa_D.png', 3, region=(600, 550, 350,210))
        #             if coords:
        #                 click(coords)
        #                 self.logging('Выбираю визу D по карте поляка.')
        #                 click(locateCenterOnScreen('static/next.png'))
        #                 self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #                 if self.check_text('Нет доступных мест', 10):
        #                     self.logging('Нет мест в центре ' + str(i))
        #                 else:
        #                     self.status = self.THERE_ARE_PLACES
        #                     run = False
        #                     break
        #             click(50,200)
        #             coords = self.wait_element('static/category_record.png', 5, region=(400, 420, 300, 230))
        #             if coords:
        #                 click(coords.x + 300, coords.y)
        #                 moveTo(0, 200)
        #             coords = self.wait_element('static/nacional_visa_D.png', 3, region=(600, 550, 350,210))
        #             if coords:
        #                 click(coords)
        #                 self.logging('Выбираю визу D национальную.')
        #                 self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #                 click(locateCenterOnScreen('static/next.png'))
        #                 self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #                 if self.check_text('Нет доступных мест', 10):
        #                     self.logging('Нет мест в центре ' + str(i))
        #                 else:
        #                     self.status = self.THERE_ARE_PLACES
        #                     run = False
        #                     break
        #             click(50, 200)
        #             coords = self.wait_element('static/category_record.png', 5, region=(400, 420, 300, 230))
        #             if coords:
        #                 click(coords.x + 300, coords.y)
        #                 moveTo(0, 200)
        #             coords = self.wait_element('static/courier_visa_D.png', 3, region=(600, 550, 350,210))
        #             if coords:
        #                 click(coords)
        #                 self.logging('Выбираю курьера на визу D')
        #                 self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #                 click(locateCenterOnScreen('static/next.png'))
        #                 self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #                 if self.check_text('Нет доступных мест', 10):
        #                     self.logging('Нет мест в центре ' + str(i))
        #                 else:
        #                     if self.check_text('доступных мест нет', 10):
        #                         self.logging('Нет мест в центре ' + str(i))
        #                     else:
        #                         if self.check_text('Sorry, looks like you were going too fast.', 5):
        #                             self.status = self.ENTER_ADDRESS
        #                         else:
        #                             self.status = self.THERE_ARE_PLACES
        #                         run = False
        #                         break
        #         click(locateCenterOnScreen('static/next.png'))
        #         self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        #     if run:
        #         for i in tqdm(range(400)):
        #             sleep(1)


    def check_status(self):
        if self.status == None:
            input('>')
            # elem = self.driver.find_element(By.XPATH, "")
            #     if 'Выбрать город' in s:
            #         self.logging('Выбран статус поиска визы.')
            #         self.status = self.FIND_VISA
            #         break
            #     elif 'Запись на подачу документов' in s:
            #         self.logging('Выбираем "Запись на подачу документов."')
            #         self.status = self.SELECT_FIND_VISA
            #         break
            #     elif 'Назначить дату подачи документов' in s:
            #         if 'Ваша учетная запись заблокирована' in s:
            #             sleep(130)
            #         self.logging('Нажимаем капчу')
            #         self.status = self.AUTORIZATION
            #         break
            #     elif 'You are now in line' in s:
            #         self.status = self.NOT_WORK
            #         break
            #     elif 'Инструкция' in s:
            #         self.status = self.SCROLL_AUTORIZATION


    def autorization(self):
        self.driver.get(self.address)
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="EmailId"]')))
        elem.send_keys(os.getenv('LOGIN'))
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "Password"]')))
        elem.send_keys(os.getenv('PASSWORD'))
        input('Пройдите капчу и нажмите "Продолжить"')
        self.status = None


    def select_find_visa(self):
        pass
        # self.wait_element('static/site_work.png', 120, region=(0, 0, 150, 150))
        # coords = self.wait_element('static/schedule_appointment_rus.png', 10, region=(170, 240, 300, 160))
        # if coords:
        #     click(coords)
        # else:
        #     coords = self.wait_element('static/schedule_appointment.png', 10, region=(170, 240, 300, 160))
        #     if coords:
        #         click(coords)
        #     else:
        #         self.logging('Не нашёл пункт меню "Запись на подачу документов".')
        # sleep(5)
        # self.status = None


    def record_for_visa(self):
        pass
        # sleep(1)
        # pyautogui.screenshot(str(datetime.now()).split('.')[0].replace(':', '-') +'.png')
        # self.status = None
        # if input('>') == 'q':
        #     self.status = self.STOP


    def run(self):
        gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        self.driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko + '.exe')
        with open(self.LOG, 'a', encoding='utf-8') as self.log:
            self.logging('Авторизация')
            self.autorization()
            run = True
            while run:
                self.check_status()
                if self.status == self.STOP:
                    break
                # elif self.status == self.NOT_WORK:
                #         self.logging('Сайт ожидает очереди.')
                #         self.wait_site_work()
                #         self.logging('Очередь подошла.')
                # elif self.status == self.AUTORIZATION:
                #         self.logging('Авторизация.')
                #         self.autorization()
                #         self.logging('Конец авторизации.')
                # elif self.status == self.FIND_VISA:
                #         self.logging('Начало поиска визового центра со свободными местами.')
                #         self.find_visa((3,4,5,6,7,8,9,10,11,12,13))
                #         self.logging('Конец поиска визового центра со свободными местами.')
                # elif self.status == self.SELECT_FIND_VISA:
                #         self.logging('Выбор меню поиска визового центра.')
                #         self.select_find_visa()
                #         self.logging('Выбрано меню поиска визового центра.')
                # elif self.status == self.THERE_ARE_PLACES:
                #     self.logging('Есть свободные места. Начало записи на подачу документов.')
                #     playsound.playsound('signal-gorna-na-obed.mp3')
                #     self.send_email()
                #     self.record_for_visa()
                # elif self.status == self.SCROLL_AUTORIZATION:
                #     self.logging('Скроллинг вниз и авторизация.')
                #     self.autorization()
                #     self.logging('Конец авторизации.')
        self.driver.close()


# try:
fv = Find_visa('Coordinates', ADDRESS, 'config.env')
print('Версия 0.01')
fv.run()
# except Exception as e:
#     playsound.playsound('signal-gorna-na-obed.mp3')
#     fv.logging(e)

program = ((True, (By.XPATH, '/html/body/app-root/div/app-login/section/div/div/mat-card/form/button')),
           (True, (By.XPATH, '/html/body/app-root/div/app-dashboard/section/div/div[2]/button')),
           (True, (By.XPATH, '//*[@id="mat-select-0"]')),
           (True, (By.XPATH, '//*[@id="mat-option-0"]')),  #Барановичи
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-13')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-select-value-1')),
           (True, (By.ID, 'mat-option-1')),  #Брест
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-18')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-select-value-1')),
           (True, (By.ID, 'mat-option-2')),  #Гомель
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-23')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-select-value-1')),
           (True, (By.ID, 'mat-option-3')),  #Гродно
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-28')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-select-value-1')),
           (True, (By.ID, 'mat-option-4')),  # Лида
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-33')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-select-value-1')),
           (True, (By.ID, 'mat-option-5')),  # Минск
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-38')),
           (True, (By.ID, 'mat-select-4')),
           (True, (By.ID, 'mat-option-44')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-select-value-1')),
           (True, (By.ID, 'mat-option-6')),  # Могилёв
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-47')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')),
           (True, (By.ID, 'mat-option-7')),  # Пинск
           (True, (By.ID, 'mat-select-2')),
           (True, (By.ID, 'mat-option-51')),
           (False, (By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')))


