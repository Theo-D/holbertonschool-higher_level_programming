const header = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', (Event) => {
  header.textContent = 'New Header!!!'
});
