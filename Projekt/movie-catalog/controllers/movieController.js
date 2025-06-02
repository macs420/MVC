const movieModel = require('../models/movie');

exports.listMovies = (req, res) => {
    res.render('list', { movies: movieModel.getAll() });
};

exports.showAddForm = (req, res) => {
    res.render('form', { movie: null, id: null });
};

exports.addMovie = (req, res) => {
    const { title, director, rating } = req.body;
    movieModel.add({ title, director, rating });
    res.redirect('/');
};

exports.showEditForm = (req, res) => {
    const id = req.params.id;
    res.render('form', { movie: movieModel.get(id), id });
};

exports.updateMovie = (req, res) => {
    const id = req.params.id;
    const { title, director, rating } = req.body;
    movieModel.update(id, { title, director, rating });
    res.redirect('/');
};

exports.deleteMovie = (req, res) => {
    movieModel.delete(req.params.id);
    res.redirect('/');
};
