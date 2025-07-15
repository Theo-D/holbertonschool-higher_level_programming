const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

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
document.addEventListener('DOMContentLoaded', function() {
  const helloDiv = document.querySelector('#hello');
  getData(url).then(data => {
    helloDiv.textContent = data.hello;
  });
});
