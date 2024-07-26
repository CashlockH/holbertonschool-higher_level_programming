const add_item =document.querySelector('div')
add_item.addEventListener('click', function (e) {
    const li = document.createElement('li')
    li.textContent = 'Item'
    const ul = document.querySelector('ul')
    ul.appendChild(li)
})