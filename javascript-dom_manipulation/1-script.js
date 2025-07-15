const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.addEventListener('click', (Event) => {
  header.style.color = '#FF0000';
});
