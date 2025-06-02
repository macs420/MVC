const express = require('express');
const router = express.Router();
const controller = require('../controllers/movieController');

router.get('/', controller.listMovies);
router.get('/add', controller.showAddForm);
router.post('/add', controller.addMovie);
router.get('/edit/:id', controller.showEditForm);
router.post('/edit/:id', controller.updateMovie);
router.post('/delete/:id', controller.deleteMovie);

module.exports = router;
