const movieList = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

async function getData (url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const json = await response.json();
    return json;
  } catch (error) {
    console.error(error.message);
  }
}

getData(url).then(data => {
  data.results.forEach(element => {
    const li = document.createElement('li');
    li.textContent = element.title;
    movieList.appendChild(li);
  });
});
