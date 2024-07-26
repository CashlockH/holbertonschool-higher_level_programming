url = "https://hellosalut.stefanbohacek.dev/?lang=fr"
hello = document.getElementById("hello")
fetch(url)
.then((response) => {
    return response.json()
})
.then((response) => {
    hello.innerText = response.hello
})