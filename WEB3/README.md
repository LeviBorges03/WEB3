# Protótipos Estáticos (WEB3)

Este diretório contém protótipos puramente estáticos da UI da biblioteca, escritos em HTML, CSS e JavaScript puros (sem dependência do ASP.NET Core).

Eles servem como base para a validação rápida de design e UI.

## O que tem aqui
- `Livro/index.html`: A visão detalhada de uma obra, incluindo a lógica do Sistema de Favoritos utilizando o `localStorage`.
- `Autor/index.html`: A visão do perfil do autor.

## Como visualizar
Você não precisa de um servidor complexo. Basta abrir os arquivos `.html` diretamente no seu navegador, ou, se preferir uma simulação real de servidor, rode no terminal dentro da pasta `WEB3`:

```bash
python3 -m http.server 8000
```
E acesse `http://localhost:8000/Livro/index.html`.

**Nota de Manutenção:** Ao fazer alterações na UI do C# ASP.NET Core no diretório raiz, lembre-se de espelhar as alterações relevantes nos arquivos deste diretório para manter os protótipos em sincronia.