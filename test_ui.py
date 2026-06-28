from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Acessando a página principal...")
        page.goto("http://localhost:5239")
        page.wait_for_selector(".livro-card")
        print("Página carregada com sucesso.")

        try:
            # Limpar localStorage antes
            page.evaluate("localStorage.clear()")
            page.reload()
            page.wait_for_selector(".livro-card")

            # Testar a barra de pesquisa
            print("Pesquisando por 'Dom Quixote'...")
            page.wait_for_selector("#pesquisaLivros", state="visible")
            page.fill("#pesquisaLivros", "Dom Quixote")
            time.sleep(1) # Aguardar a filtragem visual
            visible_cards = page.locator(".livro-card:visible").count()
            print(f"Cards visíveis após pesquisa: {visible_cards}")

            # Limpar pesquisa
            page.fill("#pesquisaLivros", "")
            time.sleep(1)

            # Testar os Favoritos na Index
            print("Clicando no botão de favoritar do primeiro livro...")
            first_star = page.locator(".livro-card:visible").first.locator(".estrela-favorito")
            first_star_text_before = first_star.inner_text()
            print(f"Estrela antes: {first_star_text_before}")

            # Como a estrela é um child node em position: absolute, podemos interagir clicando nela
            first_star.click()
            time.sleep(1)

            first_star_text_after = first_star.inner_text()
            print(f"Estrela depois: {first_star_text_after}")

            # Clicar no livro para ir a página de detalhes
            print("Navegando para a página de detalhes...")
            page.locator(".livro-card:visible").first.locator(".livro-info h4").click()

            page.wait_for_selector("#btnFavoritoLivro", state="visible")
            time.sleep(1)
            btn_text = page.locator("#btnFavoritoLivro").inner_text()
            print(f"Texto do botão de favoritos no Livro.cshtml: {btn_text}")
        except Exception as e:
            print(f"Erro no teste: {e}")

        browser.close()

run()
