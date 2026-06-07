# Protótipo Estático WEB3

Esta pasta contém o protótipo UI puramente estático das telas da aplicação.

## Propósito

Os arquivos HTML (`index.html`) e folhas de estilo CSS encontrados nesta pasta e em seus subdiretórios foram desenvolvidos visando isolar o design gráfico e o comportamento do layout das restrições e mecânicas do ASP.NET Core MVC.
Eles foram a base do trabalho criativo que posteriormente foi fragmentado e convertido nas `.cshtml` da aplicação real que fica no diretório raiz.

Aqui testamos e prototipamos componentes visuais como os cards arredondados de autores, o layout de grid das obras, e os comportamentos experimentais em JavaScript (como as validações do localStorage para a listagem de Favoritos).

## Como Testar o Protótipo

A interface estática pode ser analisada ou continuada abrindo diretamente os arquivos `.html` no seu navegador sem a necessidade de compilação ou do SDK do .NET.
Alternativamente, caso precise lidar com importações restritas, inicie um servidor python na raiz deste diretório WEB3:

```bash
python3 -m http.server 8000
```