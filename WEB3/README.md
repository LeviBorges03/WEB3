# WEB3 - Ambiente de Prototipagem Estática

A pasta **WEB3** é um diretório independente e essencial no repositório da aplicação **Biblioteca**. O propósito exclusivo desta pasta é servir como um **ambiente de prototipagem estática isolado** (contendo apenas HTML, CSS e JavaScript puro, sem ligação com o backend ASP.NET Core).

## 🎯 Objetivo

Sempre que novas interfaces, interações de UI/UX, animações CSS ou layouts responsivos precisarem ser concebidos ou testados, o desenvolvimento primário deve iniciar ou ser refletido aqui. Isso garante:
1. **Velocidade na aprovação do Design:** Designers ou Desenvolvedores Frontend podem avaliar o comportamento visual sem precisar rodar o servidor .NET ou configurar o banco de dados.
2. **Consistência:** Atua como a "fonte da verdade visual" do projeto. Funcionalidades como a interface do Sistema de Favoritos e o comportamento dos botões são previamente validadas neste ambiente antes de serem transcritas para as Views `.cshtml` dinâmicas.

## ⚠️ Manutenção

- **Regra de Ouro:** Toda manutenção de UI, inserção de scripts locais ou atualizações na documentação do frontend devem considerar tanto a raiz do projeto MVC quanto o diretório `WEB3/`.
- Caso adicione uma funcionalidade nova de interface (por exemplo, a mecânica do `localStorage` nos botões), ela deve estar representada de forma estática aqui, demonstrando como o componente reage perante o usuário.