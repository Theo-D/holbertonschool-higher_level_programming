const charDiv = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

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
  charDiv.textContent = data.name;
});
