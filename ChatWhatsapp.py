from playwright.sync_api import sync_playwright
import time
import os

class ChatBotWhatsapp:
	def __init__(self):
		pass
	async def inicio(self):
		async with sync_playwright() as p:
			navegador = p.chromium.launch(headless=False)
			context = await navegador.new_context()
			pagina = await context.new_page()
			pagina.goto('https://web.whatsapp.com')
			session_storage = await pagina.evaluate("() => JSON.stringify(sessionStorage)")
			os.environ["SESSION_STORAGE"] = session_storage
			time.sleep(10)
			await context.close()

		storage = await context.storage_state(path="state.json")

		session_storage = os.environ["SESSION_STORAGE"]
		await context.add_init_script("""(storage => {
		  if (window.location.hostname === 'example.com') {
		    const entries = JSON.parse(storage)
		    for (const [key, value] of Object.entries(entries)) {
		      window.sessionStorage.setItem(key, key)
		    }
		  }
		})('""" + session_storage + "')")

		async with sync_playwright() as p:
			navegador = p.chromium.launch(headless=False)
			context = navegador.new_context(storage_state="state.json")
			pagina = navegador.new_page()
			pagina.goto('https://web.whatsapp.com')
			time.sleep(10)


if __name__ == '__main__':
	chat = ChatBotWhatsapp()
	chat.inicio()