vehicleCodeInput = document.getElementById("vehicleCode")
vehicleCategoryInput = document.getElementById("vehicleCategory")
vehicleTypeInput = document.getElementById("vehicleType")
registrationNumberInput = document.getElementById("registrationNumber")

vehicleNameInput = document.getElementById("vehicleName")
vehicleSeatsInput = document.getElementById("vehicleSeats")
vehiclePriceInput = document.getElementById("vehiclePrice")
vehicleStatusInput = document.getElementById("vehicleStatus")

messageRegistrationNumber = document.getElementById("messageRegistrationNumber")
messagevVhicleName = document.getElementById("messagevVhicleName")
messageVehicleSeats = document.getElementById("messageVehicleSeats")
messageVehiclePrice = document.getElementById("messageVehiclePrice")
messagevehicleStatus = document.getElementById("messagevehicleStatus")

console.log(messageRegistrationNumber, messagevVhicleName, messageVehicleSeats, messageVehiclePrice, messagevehicleStatus)

console.log(vehicleCodeInput, vehicleCategoryInput, vehicleTypeInput, registrationNumberInput, vehicleNameInput, vehicleSeatsInput, vehiclePriceInput, vehicleStatusInput)

// dinh nghia cac ham
function renderUIData(data) {
    vehicleCodeInput.value = data.id
    vehicleCategoryInput.value = data.danhmuc
    vehicleTypeInput.value = data.loaiphuongtien
    registrationNumberInput.value = data.sodangki

    vehicleNameInput.value = data.tenphuongtien
    vehicleSeatsInput.value = data.sochongoi
    vehiclePriceInput.value = data.giathue1n
    vehicleStatusInput.value = data.tinhtrangxe
}
// Lay du lieu
function getPTToFix() {
    fetch("/getPT")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        renderUIData(data)
    })
}

// bat cac su kien
registrationNumberInput.addEventListener("keydown", function() {
    messageRegistrationNumber.innerHTML = ""
})
vehicleNameInput.addEventListener("keydown", function() {
    messagevVhicleName.innerHTML = ""
})
vehicleSeatsInput.addEventListener("keydown", function() {
    messageVehicleSeats.innerHTML = ""
})
vehiclePriceInput.addEventListener("keydown", function() {
    messageVehiclePrice.innerHTML = ""
})
vehicleStatusInput.addEventListener("keydown", function() {
    messagevehicleStatus.innerHTML = ""
})


// goi ham
getPTToFix()