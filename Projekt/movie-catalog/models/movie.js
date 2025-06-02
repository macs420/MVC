const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, 'movies.json');

function readMovies() {
    if (!fs.existsSync(dataPath)) return [];
    const data = fs.readFileSync(dataPath);
    return JSON.parse(data);
}

function writeMovies(movies) {
    fs.writeFileSync(dataPath, JSON.stringify(movies, null, 2));
}

module.exports = {
    getAll: () => readMovies(),
    get: (id) => readMovies()[id],
    add: (movie) => {
        const movies = readMovies();
        movies.push(movie);
        writeMovies(movies);
    },
    update: (id, movie) => {
        const movies = readMovies();
        movies[id] = movie;
        writeMovies(movies);
    },
    delete: (id) => {
        const movies = readMovies();
        movies.splice(id, 1);
        writeMovies(movies);
    }
};
