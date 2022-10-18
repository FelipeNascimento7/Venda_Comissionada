from playwright.sync_api import sync_playwright
import time
import os

class ChatBotWhatsapp:
	def __init__(self):
		with sync_playwright() as p:
			navegador = p.chromium.launch(headless=False)
			pagina = navegador.new_page()
			pagina.goto('https://web.whatsapp.com')
			time.sleep(10)

		session_storage = pagina.evaluate("() => JSON.stringify(sessionStorage)")
		os.environ["SESSION_STORAGE"] = session_storage


		session_storage = os.environ["SESSION_STORAGE"]
		context.add_init_script("""(storage => {
				  if (window.location.hostname === 'example.com') {
				    const entries = JSON.parse(storage)
				    for (const [key, value] of Object.entries(entries)) {
				      window.sessionStorage.setItem(key, key)
				    }
				  }
				})('""" + session_storage + "')")

		with sync_playwright() as p:
			navegador = p.chromium.launch(headless=False)
			pagina = navegador.new_page()
			pagina.goto('https://web.whatsapp.com')
			time.sleep(10)


if __name__ == '__main__':
	chat = ChatBotWhatsapp()