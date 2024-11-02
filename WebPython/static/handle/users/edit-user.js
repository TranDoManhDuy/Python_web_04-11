
employeeName = document.getElementById("employeeName");
employeePhone = document.getElementById("employeePhone");
employeeAddress = document.getElementById("employeeAddress");
employeeSalary = document.getElementById("employeeSalary");
employeePosition = document.getElementById("employeePosition");
submitBtn = document.getElementById("submitBtn");

messName = document.getElementById("messName");
messPhone = document.getElementById("messPhone");
messAddress = document.getElementById("messAddress");
messSalary = document.getElementById("messSalary")

console.log(messName, messPhone, messAddress, messSalary)

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

function render(data) {
    employeeName.value = data.FullName;
    employeePhone.value = data.PhoneNumber;
    employeeAddress.value = data.Address;
    employeeSalary.value = data.Salary.toString();
    employeePosition.value = data.Position;
}

function getData() {
    fetch("/getEditStaff")
    .then((response) => response.json())
    .then((data) => {
        render(data);
    })
}

submitBtn.addEventListener("click", () => {
    if (
        employeeName.value != "" &&
        employeePhone.value.length == 10 &&
        employeeAddress.value != "" &&
        employeeSalary.value != "" &&
        Number(employeeSalary.value) >= 0
    ) {
        fetch("/updateStaff", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                FullName: employeeName.value,
                PhoneNumber: employeePhone.value,
                Address: employeeAddress.value,
                Salary: employeeSalary.value,
                Position: employeePosition.value,
            }),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.status == "success") {
                alert("Update successfully")
                window.location.href = "/list_users"
            }
        })
    }
    else {
        console.log(employeeName.value != "", employeePhone.value.length == 10, employeeAddress.value != "", employeeSalary.value != "", employeePosition.value)
        alert("Please fill in all required fields")
    }
})
getData()