employeeName = document.getElementById("employeeName");
employeePhone = document.getElementById("employeePhone");
employeeAddress = document.getElementById("employeeAddress");
employeeSalary = document.getElementById("employeeSalary");
employeePosition = document.getElementById("employeePosition");

console.log(employeeName, employeePhone, employeeAddress, employeeSalary, employeePosition)

messName = document.getElementById("messName");
messPhone = document.getElementById("messPhone");
messAddress = document.getElementById("messAddress");
messSalary = document.getElementById("messSalary")

console.log(messName, messPhone, messAddress, messSalary)

submitBtn = document.getElementById("submitBtn");

employeeName.addEventListener("blur", () => {
    if (employeeName.value == "") {
        messName.innerHTML = "Name is required"
    }
})

employeePhone.addEventListener("blur", () => {
    if (employeePhone.value == "") {
        messPhone.innerHTML = "Phone is required"
    }
    if (employeePhone.value.length != 10) {
        messPhone.innerHTML = "Phone number is invalid (10 digits)"
    }
})

employeeAddress.addEventListener("blur", () => {    
    if (employeeAddress.value == "") {
        messAddress.innerHTML = "Address is required"
    }
})

employeeSalary.addEventListener("blur", () => {
    if (employeeSalary.value == "") {
        messSalary.innerHTML = "Salary is required"
    }
    if (employeeSalary.value < 0) {
        messSalary.innerHTML = "Salary is invalid (>= 0)"
    }
})

employeeName.addEventListener("keydown", () => {
    messName.innerHTML = ""
})
employeePhone.addEventListener("keydown", () => {
    messPhone.innerHTML = ""
    if (employeePhone.value.length > 10) {
        messPhone.innerHTML = "Phone number is invalid (10 digits)"
    }
})
employeePhone.addEventListener("input", (e) => {
    e.target.value = e.target.value.replace(/[^0-9]/g, "");
});
employeeAddress.addEventListener("keydown", () => {
    messAddress.innerHTML = ""
})
employeeSalary.addEventListener("keydown", () => {
    messSalary.innerHTML = ""
})

// (function() {
//     if (
//         employeeName.value != "" &&
//         employeePhone.value.length == 10 &&
//         employeeAddress.value != "" &&
//         employeeSalary.value != "" &&
//         Number(employeeSalary.value) >= 0
//     ) {
        
//     }
// })();
submitBtn.addEventListener("click", () => {
    if (
        employeeName.value != "" &&
        employeePhone.value.length == 10 &&
        employeeAddress.value != "" &&
        employeeSalary.value != "" &&
        Number(employeeSalary.value) >= 0
    ) {
        fetch("/addStaff", {
            method: "POST",
            body: JSON.stringify({
                name: employeeName.value,
                phone: employeePhone.value,
                address: employeeAddress.value,
                salary: employeeSalary.value,
                position: employeePosition.value
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.status == "success") {
                alert("Add staff successfully")
                window.location.href = "/list_users"
            }
        })
    }
    else {
        alert("Please fill in all fields correctly")
    }
})