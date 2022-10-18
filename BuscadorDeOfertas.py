from playwright.sync_api import sync_playwright
import time

class BuscadorDeOfertas:

  def __init__(self, nomeDoProduto):
    self.nomeDoProduto = nomeDoProduto

  def buscarValorDoProduto(self,nomeDoProduto):
    self.buscarNaAmazon()

  def buscarNaAmazon(self):
    with sync_playwright() as p:
      navegador = p.chromium.launch(headless=False)
      pagina = navegador.new_page()
      pagina.goto('https://www.amazon.com.br')
      pagina.fill('xpath=//*[@id="twotabsearchtextbox"]', self.nomeDoProduto)
      pagina.locator('xpath=//*[@id="nav-search-submit-button"]').click()
      time.sleep(5)
      navegador.close()

  if __name__ == "__main__":
    print('oi')
