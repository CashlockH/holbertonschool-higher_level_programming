let url = "https://swapi-api.hbtn.io/api/people/5/?format=json"
character = document.getElementById("character")
fetch(url)
.then((response) => {
    result = response.json()
    return result
})
.then((response) => {
    character.innerText = response.name
})