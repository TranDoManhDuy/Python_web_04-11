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

btnSubmit = document.getElementById("btnSubmit")

addProductBtn = document.getElementById("addProductBtn")
listProductBtn = document.getElementById("listProductBtn")

addProductBtn.addEventListener('click', function() {
    window.location.href = "/products_add"
})
listProductBtn.addEventListener('click', function() {
    window.location.href = "/products_list"
})
console.log(addProductBtn, listProductBtn)

let dataGlobal = {}
isCanSubmit = true
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
        dataGlobal = data
        console.log(data)
        renderUIData(data)
    })
}

// bat cac su kien
registrationNumberInput.addEventListener("keydown", function() {
    messageRegistrationNumber.innerHTML = ""
    isCanSubmit = true
})
vehicleNameInput.addEventListener("keydown", function() {
    messagevVhicleName.innerHTML = ""
    isCanSubmit = true
})
vehicleSeatsInput.addEventListener("keydown", function() {
    messageVehicleSeats.innerHTML = ""
    isCanSubmit = true
})
vehiclePriceInput.addEventListener("keydown", function() {
    messageVehiclePrice.innerHTML = ""
    isCanSubmit = true
})
vehicleStatusInput.addEventListener("keydown", function() {
    messagevehicleStatus.innerHTML = ""
    isCanSubmit = true
})

registrationNumberInput.addEventListener('blur', function() {
    if (registrationNumberInput.value != dataGlobal.sodangki) {
        fetch('/checkRegistrationNumber', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                registrationNumber: registrationNumberInput.value
            })
        })
        .then(response => response.json())
        .then(function (data) {
            if (data.status != "OK") {
                isCanSubmit = false
                messageRegistrationNumber.innerHTML = data.status
            }
            else {
                isCanSubmit = true
            }
        })
    }
})
vehicleNameInput.addEventListener('blur', function() {
    if (vehicleNameInput.value == '') {
        isCanSubmit = false
        messagevVhicleName.innerHTML = 'Vehicle name is required'
    }
})
vehicleSeatsInput.addEventListener('blur', function() {
    if (vehicleSeatsInput.value == '') {
        isCanSubmit = false
        messageVehicleSeats.innerHTML = 'Vehicle seats is required'
    }
    if (Number(vehicleSeatsInput.value) <= 0) {
        vehicleSeatsInput.value = ""
        messageVehicleSeats.innerHTML = 'Vehicle seats must be greater than 0'
        isCanSubmit = false
    } else {
        vehicleSeatsInput.value = Number(vehicleSeatsInput.value)
        isCanSubmit = true
    }
})
vehiclePriceInput.addEventListener('blur', function() {
    if (vehiclePriceInput.value == '') {
        isCanSubmit = false
        messageVehiclePrice.innerHTML = 'Vehicle price is required'
    }
    if (Number(vehiclePriceInput.value) <= 0) {
        vehiclePriceInput.value = ""
        isCanSubmit = false
        messageVehiclePrice.innerHTML = 'Vehicle price must be greater than 0'
    } else {
        vehiclePriceInput.value = Number(vehiclePriceInput.value)
        isCanSubmit = true
    }
})
vehicleStatusInput.addEventListener('blur', function() {
    if (vehicleStatusInput.value == '') {
        isCanSubmit = false
        messagevehicleStatus.innerHTML = 'Vehicle status is required'
    }
    if (Number(vehicleStatusInput.value) < 0 || Number(vehicleStatusInput.value) > 100) {
        messagevehicleStatus.innerHTML = '0 <= Vehicle status <= 100'
        isCanSubmit = false
    }
    else {
        vehicleStatusInput.value = Number(vehicleStatusInput.value)
        isCanSubmit = true
    }
})

btnSubmit.addEventListener('click', function() {
    if (isCanSubmit && vehicleNameInput.value && registrationNumberInput.value && vehicleSeatsInput.value && vehiclePriceInput.value && vehicleStatusInput.value) {
        fetch('/fixVehicle', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: vehicleCodeInput.value,
                danhmuc: vehicleCategoryInput.value,
                loaiphuongtien: vehicleTypeInput.value,
                sodangki: registrationNumberInput.value,
                tenphuongtien: vehicleNameInput.value,
                sochongoi: vehicleSeatsInput.value,
                giathue1n: vehiclePriceInput.value,
                tinhtrangxe: vehicleStatusInput.value
            })
        })
        .then(function (response) {
            if (response.redirected) {
                window.location.href = response.url
            }
        })
    }
})
// goi ham
getPTToFix()