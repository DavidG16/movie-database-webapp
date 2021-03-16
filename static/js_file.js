
const query_type_selected = document.getElementById("queryType");
query_type_selected.addEventListener('change', (event) => {
    if (event.target.value === "is known for") {
        const  string_element = document.getElementById("string-val")
        string_element.classList.add("Required")
        string_element.classList.remove("d-none")
    }
    else {
        const  string_element = document.getElementById("string-val")
        string_element.classList.remove("Required")
        string_element.classList.add("d-none")
    }
});



