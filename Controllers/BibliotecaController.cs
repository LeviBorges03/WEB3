using Biblioteca.Models;
using Microsoft.AspNetCore.Mvc;

namespace Biblioteca.Controllers;

public class BibliotecaController : Controller
{
    // Ação principal que retorna a lista de livros para a View (Index.cshtml).
    public IActionResult Index()
    {
        // Cria uma lista de livros instanciando objetos da classe Livro.
        // O nome da imagem da capa de cada livro em wwwroot/capasImage deve corresponder exatamente à propriedade Titulo.
        List<Livro> l1 = new List<Livro>()
        {
            new Livro { Titulo = "O Alquimista", Autor = "Paulo Coelho", Genero = "Ficção", NumPaginas = 208, DataPublicacao = new DateOnly(1988, 1, 1) },
            new Livro { Titulo = "Harry Potter and the Prisoner of Azkaban", Autor = "J.K. Rowling", Genero = "Fantasia", NumPaginas = 317, DataPublicacao = new DateOnly(1999, 7, 8) },
            new Livro { Titulo = "Dom Casmurro", Autor = "Machado de Assis", Genero = "Romance", NumPaginas = 256, DataPublicacao = new DateOnly(1899, 1, 1) },
            new Livro { Titulo = "A Culpa é das Estrelas", Autor = "John Green", Genero = "Romance", NumPaginas = 313, DataPublicacao = new DateOnly(2012, 1, 10) },
            new Livro { Titulo = "A Moreninha", Autor = "Joaquim Manuel de Macedo", Genero = "Romance", NumPaginas = 180, DataPublicacao = new DateOnly(1844, 1, 1) },
            new Livro { Titulo = "Alice", Autor = "Lewis Carroll", Genero = "Fantasia", NumPaginas = 352, DataPublicacao = new DateOnly(1865, 11, 26) },
            new Livro { Titulo = "As Aventuras de Pinóquio", Autor = "Carlo Collodi", Genero = "Infantil", NumPaginas = 192, DataPublicacao = new DateOnly(1883, 1, 1) },
            new Livro { Titulo = "Memórias Póstumas de Brás Cubas", Autor = "Machado de Assis", Genero = "Romance", NumPaginas = 352, DataPublicacao = new DateOnly(1881, 1, 1) },
            new Livro { Titulo = "O Hobbit", Autor = "J.R.R. Tolkien", Genero = "Fantasia", NumPaginas = 310, DataPublicacao = new DateOnly(1937, 9, 21) },
            new Livro { Titulo = "O Mágico de Oz", Autor = "L. Frank Baum", Genero = "Fantasia", NumPaginas = 272, DataPublicacao = new DateOnly(1900, 5, 17) },
            new Livro { Titulo = "O Pequeno Príncipe", Autor = "Antoine de Saint-Exupéry", Genero = "Infantil", NumPaginas = 96, DataPublicacao = new DateOnly(1943, 4, 6) },
            new Livro { Titulo = "O Senhor dos Anéis", Autor = "J.R.R. Tolkien", Genero = "Fantasia", NumPaginas = 1216, DataPublicacao = new DateOnly(1954, 7, 29) }
        };

        // Ordena os livros por data de publicação, da mais recente para a mais antiga (descendente)
        var livrosOrdenados = l1.OrderByDescending(l => l.DataPublicacao).ToList();

        // Envia a lista ordenada para a View responsável por renderizar o HTML (Views/Biblioteca/Index.cshtml)
        return View(livrosOrdenados);
    }
}