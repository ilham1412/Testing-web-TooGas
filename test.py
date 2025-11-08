from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#Konfigurasi untuk Edge
def get_default_edge_options():
    options = Options()
    options.add_argument("--no-sandbox")
    return options

#Inisialisasi driver : Edge
def get_driver():
    service = Service("D:\\selenium\\msedgedriver.exe")  #\\ agar tidak dikira escape sequence
    options = get_default_edge_options()
    return webdriver.Edge(service=service, options=options)

# TEST 1: Cek Judul Halaman Website
def test_my_website_title():
    driver = get_driver()
    driver.get("https://todo-list-six-umber-66.vercel.app/")
    print("Page title is:", driver.title)
    time.sleep(2)
    driver.quit()

# TEST 2: Page Load Strategy
def test_page_load_strategy(strategy='normal'):
    options = get_default_edge_options()
    options.page_load_strategy = strategy
    service = Service("D:\\selenium\\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    driver.get("https://todo-list-six-umber-66.vercel.app/")
    print("Loaded with strategy:", strategy)
    driver.quit()

#TEST 3: Set Timeout
def test_timeouts(script=5000, page_load=10000, implicit=5000):
    driver = get_driver()
    driver.set_script_timeout(script / 1000)
    driver.set_page_load_timeout(page_load / 1000)
    driver.implicitly_wait(implicit / 1000)
    driver.get("https://todo-list-six-umber-66.vercel.app/")
    print("Timeouts set and page loaded.")
    driver.quit()

#TEST 4: Terima Sertifikat Tidak Aman
def test_accept_insecure_certs():
    options = get_default_edge_options()
    options.accept_insecure_certs = True
    service = Service("D:\\selenium\\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    driver.get("https://todo-list-six-umber-66.vercel.app/")
    print("Accessed insecure site successfully.")
    driver.quit()


#Eksekusi fungsi
if __name__ == "__main__":
    test_my_website_title()
    test_page_load_strategy('eager')
    test_timeouts()
    test_accept_insecure_certs()
