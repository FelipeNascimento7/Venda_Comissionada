from playwright.sync_api import sync_playwright
import time

class BuscadorDeOfertas:

  def __init__(self, nomeDoProduto,site):
    self.nomeDoProduto = nomeDoProduto
    self.site = site

  def buscarValorDoProduto(self):
    with sync_playwright() as p:
      navegador = p.chromium.launch(headless=False)
      pagina = navegador.new_page()
      pagina.goto("https://www.amazon.com.br")
      pagina.fill('xpath=//*[@id="twotabsearchtextbox"]', 'iphone 13')
      pagina.locator('xpath=//*[@id="nav-search-submit-button"]').click()
      time.sleep(5)
      navegador.close()
