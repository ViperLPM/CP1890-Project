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