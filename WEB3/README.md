# WEB3 - Protótipos de Interface (UI)

A pasta `WEB3/` abriga representações puramente estáticas (HTML, CSS, JS) das interfaces da aplicação. Esses arquivos **não utilizam ASP.NET Core** ou C#, servindo exclusivamente como **protótipos** para experimentação e validação visual de design e UX antes ou paralelamente à implementação no sistema MVC principal.

## Como Servir Localmente

Para visualizar e interagir com os protótipos de forma isolada do backend .NET, você pode iniciar um servidor estático leve diretamente nesta pasta usando Python:

```bash
cd WEB3
python3 -m http.server 8000
```

Após iniciar o servidor, abra o navegador e acesse:
`http://localhost:8000`

> **Nota para Desenvolvedores:** Qualquer alteração no design validada aqui em `WEB3/` deve ser posteriormente migrada/sincronizada para as *Views* (arquivos `.cshtml`) e arquivos estáticos (CSS/JS na pasta `wwwroot`) na raiz do projeto principal para ter efeito na aplicação final.
