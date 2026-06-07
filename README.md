# Biblioteca Digital MVC

Um projeto ASP.NET Core MVC projetado para fornecer um catálogo interativo de obras clássicas da literatura, focando em uma experiência de usuário (UX) fluida e moderna que simula as transições de uma Single Page Application (SPA), apesar de usar a estrutura clássica de Views.

## 🌟 Funcionalidades

* **Catálogo Expansível:** Visualize as obras em um carrossel horizontal de rolagem suave ou expanda a grade para ter a visualização completa de todo o catálogo instantaneamente.
* **Sistema de Busca em Tempo Real:** Pesquise obras por título e autor com resultados sendo filtrados nativamente via JavaScript diretamente na DOM da tela principal.
* **Sistema de Favoritos (Local):** Marque obras favoritas na página do Livro e um indicador visual (⭐) aparecerá junto com o título do livro na listagem inicial. Todas as preferências são salvas localmente no `localStorage` do seu navegador.
* **SPA-Like Navigation:** A aplicação não depende de rotas com parâmetros complexos e consultas redundantes. O clique em um livro ou autor empacota as informações e as transfere via `localStorage` diretamente para as Views genéricas de detalhes.

## 🛠️ Tecnologias e Arquitetura

* **Framework Backend:** ASP.NET Core MVC (C#) .NET 10.0
* **Frontend UI:** HTML5, CSS3, e JavaScript Vanilla
* **Armazenamento:** `localStorage` para transporte de contexto entre Views e retenção de estado (como os Favoritos).
* **Ausência de Banco de Dados:** Para simplificar e focar na entrega visual, todo o conteúdo das obras é injetado diretamente em campos de classe estáticos por enquanto.

## 🚀 Como Executar Localmente

### Pré-requisitos
* Ter o .NET SDK versão `10.0` instalado em sua máquina.

### Executando a Aplicação
1. Clone ou extraia os arquivos do projeto.
2. Abra um terminal apontando para o diretório raiz do projeto.
3. Para garantir que as bibliotecas e compiláveis estão corretos, é recomendável rodar:
   ```bash
   dotnet clean
   dotnet build
   ```
4. Em seguida, inicie o servidor:
   ```bash
   dotnet run
   ```
5. O terminal indicará o endereço (geralmente `http://localhost:5239`). Abra no seu navegador.
