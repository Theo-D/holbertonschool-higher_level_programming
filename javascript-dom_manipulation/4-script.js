const addItem = document.querySelector('#add_item');
const unList = document.querySelector('.my_list');

addItem.addEventListener('click', (Event) => {
  const li = document.createElement('li');
  li.textContent = 'item';
  unList.appendChild(li);
});
