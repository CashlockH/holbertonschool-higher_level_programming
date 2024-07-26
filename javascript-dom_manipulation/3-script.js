const header = document.querySelector('header')
const toggle = document.querySelector('div')
toggle.addEventListener('click', function (e) {
    if (header.classList.value == 'green')
        header.classList.value = 'red'
    else if(header.classList.value == 'red')
        header.classList.value = 'green'
})