url = "https://swapi-api.hbtn.io/api/films/?format=json"
ul = document.getElementById("list_movies")
fetch(url)
.then((response) => {
    return response.json()
})
.then((response) => {
    response.results.forEach(element => {
        let li = document.createElement("li")
        li.innerText = element.title
        ul.appendChild(li)
    });
})
