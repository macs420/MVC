using Microsoft.AspNetCore.Mvc;
using MvcMovie.Models;
using Microsoft.EntityFrameworkCore;


namespace MvcMovie.Controllers
{
    public class MoviesController : Controller
    {
        private readonly MvcMovieContext _context;

        public MoviesController(MvcMovieContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var movies = _context.Movie.ToList(); // pobieranie z bazy
            return View(movies);
        }

        // GET: Movies/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Movies/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create([Bind("Title,ReleaseDate,Genre,Price")] Movie movie)
        {
            if (ModelState.IsValid)
            {
                _context.Add(movie);
                _context.SaveChanges();
                return RedirectToAction(nameof(Index));
            }
            return View(movie);
        }
        // GET: Movies/Edit/5
public IActionResult Edit(int? id)
{
    if (id == null || _context.Movie == null)
    {
        return NotFound();
    }

    var movie = _context.Movie.Find(id);
    if (movie == null)
    {
        return NotFound();
    }
    return View(movie);
}

[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Edit(int id, [Bind("Id,Title,ReleaseDate,Genre,Price")] Movie movie)
{
    if (id != movie.Id)
    {
        return NotFound();
    }

    if (ModelState.IsValid)
    {
        try
        {
            _context.Update(movie);
            _context.SaveChanges();
        }
        catch (DbUpdateConcurrencyException)
        {
            if (!_context.Movie.Any(e => e.Id == movie.Id))
            {
                return NotFound();
            }
            else
            {
                throw;
            }
        }
        return RedirectToAction(nameof(Index));
    }
    return View(movie);
}

public IActionResult Delete(int? id)
{
    if (id == null || _context.Movie == null)
    {
        return NotFound();
    }

    var movie = _context.Movie.FirstOrDefault(m => m.Id == id);
    if (movie == null)
    {
        return NotFound();
    }

    return View(movie);
}

[HttpPost, ActionName("Delete")]
[ValidateAntiForgeryToken]
public IActionResult DeleteConfirmed(int id)
{
    var movie = _context.Movie.Find(id);
    if (movie != null)
    {
        _context.Movie.Remove(movie);
        _context.SaveChanges();
    }

    return RedirectToAction(nameof(Index));
}


    }
}
