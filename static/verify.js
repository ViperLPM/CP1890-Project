/*document.getElementById("form").addEventListener("submit", (event => {

        const brand = getElementById("brand");
        const car = getElementById("car");
        const year = getElementById("year");
        const game = getElementById("game");

        const brandValue = brand.value;
        const carValue = car.value;
        const yearValue = year.value;
        const gameValue = game.value;

        const validBrand = brandValue.split(" ").length;
        const validCar = carValue.split(" ").length;
        const validYear = yearValue.split(" ").length;
        const validGame = gameValue.split(" ").length

        if (validBrand === 0) {
            brand.innerText = "Please enter the brand for your vehicle";
            return;
        } else if (validCar === 0) {
            car.innerText = "Please enter the name of your vehicle";
            return;
        } else if (validYear === 0) {
            year.innerText = "Please enter the year of your vehicle (or game)";
            return;
        } else if (validGame === 0) {
            game.innerText = "Please enter the name of the game your vehicle if from";
            return;
        } else {
            return;
        }
}));*/


// for testing purposes
addEventListener("DOMContentLoaded", () => {
    let form = document.querySelector("form");

    form.addEventListener("submit", event => {
        let inputs = document.querySelectorAll("input");
        for( let input of inputs ) {
            if( input.value == "") {
                event.preventDefault()
                alert("you need to fill this out")
                return
            }
        }
    });
})