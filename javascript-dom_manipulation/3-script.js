const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', (Event) => {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
