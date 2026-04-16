import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("Acessando a página inicial...")
        await page.goto("http://localhost:5239")

        print("Aguardando carregamento dos livros...")
        await page.wait_for_selector(".livro-card")

        print("Testando barra de pesquisa...")
        await page.fill("#inputPesquisa", "Frankenstein")
        await asyncio.sleep(1) # wait for event to trigger

        visible_cards = await page.evaluate('''() => {
            const cards = document.querySelectorAll('.livro-card');
            let count = 0;
            for(let card of cards) {
                if(card.style.display !== 'none') count++;
            }
            return count;
        }''')
        print(f"Livros visíveis após pesquisa (esperado: 1): {visible_cards}")

        print("Limpando barra de pesquisa...")
        await page.fill("#inputPesquisa", "")
        await asyncio.sleep(1)

        print("Clicando no primeiro livro para testar favoritos...")
        await page.click(".livro-card-link")

        print("Aguardando página do livro...")
        await page.wait_for_selector("#btnFavoritar")

        btn_text = await page.inner_text("#btnFavoritar")
        print(f"Texto do botão antes do clique: {btn_text}")

        await page.click("#btnFavoritar")
        await asyncio.sleep(1)

        btn_text_after = await page.inner_text("#btnFavoritar")
        print(f"Texto do botão após do clique: {btn_text_after}")

        favoritos = await page.evaluate("() => localStorage.getItem('bibliotecaFavoritos')")
        print(f"Favoritos no localStorage: {favoritos}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
