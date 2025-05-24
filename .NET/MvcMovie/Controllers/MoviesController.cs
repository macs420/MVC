using Microsoft.AspNetCore.Mvc;
using MvcMovie.Models;

namespace MvcMovie.Controllers
{
    public class MoviesController : Controller
    {
        public IActionResult Index()
        {
            var movies = new List<Movie>
            {
                new Movie { Id = 1, Title = "The Matrix", ReleaseDate = DateTime.Parse("1999-03-31"), Genre = "Science Fiction", Price = 9.99M },
                new Movie { Id = 2, Title = "Inception", ReleaseDate = DateTime.Parse("2010-07-16"), Genre = "Action", Price = 12.99M }
            };

            return View(movies);
        }
    }
}
