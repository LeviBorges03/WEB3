# Biblioteca Digital

## Sobre o Projeto
Este é um projeto de uma aplicação web desenvolvida em **ASP.NET Core MVC** utilizando **C#** e estruturada no padrão Model-View-Controller. A aplicação simula o catálogo e a navegação de uma biblioteca digital. O objetivo principal do projeto é oferecer um sistema fluído utilizando abordagens modernas de SPA (Single Page Application) sem o uso excessivo de frameworks JavaScript complexos, mantendo toda a passagem de dados de UI gerida pelo `localStorage` do navegador e views genéricas dinâmicas.

## Funcionalidades
- **Catálogo de Clássicos:** Uma vitrine completa de obras clássicas da literatura mundial.
- **Busca em Tempo Real:** Permite ao usuário filtrar livros no catálogo pelo título ou pelo autor instantaneamente.
- **Sistema de Favoritos:** O usuário pode marcar e desmarcar obras como "Favoritas". O estado é persistido no navegador via `localStorage`.
- **SPA-Like Navigation:** A navegação entre o Catálogo Principal, Detalhes da Obra (Livro) e Perfil do Autor é feita instantaneamente. Os dados são passados localmente evitando requisições desnecessárias para o backend (que atua principalmente como provedor da página estática base e da lista de dados).

## Tecnologias Utilizadas
- **Backend:** C# com ASP.NET Core MVC (.NET 10).
- **Banco de Dados:** Integração preparada com MySQL utilizando `Pomelo.EntityFrameworkCore.MySql`.
- **Frontend:** HTML5, CSS3 moderno (Variáveis CSS, CSS Grid/Flexbox) e JavaScript Vanilla.
- **Design:** Elementos UI arredondados e elegantes ("pill-shaped"), transições suaves e cores de capa dinâmicas não dependentes de imagens estáticas externas.

## Como Executar
1. Certifique-se de possuir o **.NET SDK 10.0** instalado.
2. Abra o terminal na raiz do repositório.
3. Configure a `ConnectionStrings__DefaultConnection` via variável de ambiente (se for fazer uso de acesso real a banco, caso contrário os dados são mockados no Controller).
4. Execute o comando de compilação:
   ```bash
   dotnet build
   ```
5. Inicie a aplicação (certifique-se de que a porta `5239` não está em uso):
   ```bash
   dotnet run
   ```
6. Acesse via navegador `http://localhost:5239`.

---

## Nota de Manutenção
Há um diretório `WEB3/` que contém um protótipo UI completamente estático. Todas as lógicas fundamentais de frontend implementadas no `Views/Biblioteca` costumam ser refletidas no `WEB3/` para facilitar testes de design isolados e homologações independentes do compilador C#. Leia o `WEB3/README.md` para mais detalhes.