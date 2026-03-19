using Biblioteca.Models;
using Microsoft.AspNetCore.Mvc;

namespace Biblioteca.Controllers;

public class BibliotecaController : Controller
{
    public IActionResult Index()
    {
        List<Livro> l1 = new List<Livro>()
        {
            new Livro
            {
                Titulo = "Harry Potter",
                NumPaginas = 150,
                Autor = "Fulano",
                Genero = "Ficção Científica",
                DataPublicacao = DateOnly.MaxValue   
            },
            new Livro
            {
                Titulo = "Alíce no País das Maravilhas",
                NumPaginas = 500,
                Autor = "Fulana",
                Genero = "Fantasia",
                DataPublicacao = DateOnly.MinValue
            }
        };

        return View(l1);
    }
}