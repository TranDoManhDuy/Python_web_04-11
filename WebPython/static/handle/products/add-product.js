// dinh nghia cac phan tu
vehicleCodeInput = document.getElementById('vehicleCode')
vehicleCategoryInput = document.getElementById('vehicleCategory')
vehicleTypeInput = document.getElementById('vehicleType')
registrationNumberInput = document.getElementById('registrationNumber')
vehicleNameInput = document.getElementById('vehicleName')
vehicleSeatsInput = document.getElementById('vehicleSeats')
vehiclePriceInput = document.getElementById('vehiclePrice')
vehicleStatusInput = document.getElementById('vehicleStatus')
buttonSubmit = document.getElementById('buttonSubmit')
messageCheckRegistrationNumber = document.getElementById('messageCheckRegistrationNumber')
messageVehicleStatus = document.getElementById('messageVehicleStatus')
messageVehicleName = document.getElementById('messageCheckVehicleName')
messageVehicleSeats = document.getElementById('messageVehicleSeats')
messageVehiclePrice = document.getElementById('messageVehiclePrice')

chuyentrangDSPT = document.getElementById('chuyentrangDSPT')
reloadAddPT = document.getElementById('reloadAddPT')

// xu ly cac su kien
reloadAddPT.addEventListener('click', function() {
    location.reload()
})
chuyentrangDSPT.addEventListener('click', function() {
    console.log('chuyen trang')
    fetch("/chuyentrangDSPT")
    .then(function(response) {
        console.log(response)
        if (response.redirected) {
            console.log('chuyen trang')
            window.location.href = response.url
        }
    })
})

let canSubmit = true

vehicleSeatsInput.addEventListener('blur', function(event) {
    if (vehicleSeatsInput.value == '') {
        messageVehicleSeats.innerHTML = 'Vehicle seats is required'
    }
})
vehiclePriceInput.addEventListener('blur', function(event) {
    if (vehiclePriceInput.value == '') {
        messageVehiclePrice.innerHTML = 'Vehicle price is required'
    }
})
vehicleStatusInput.addEventListener('blur', function(event) {
    if (vehicleStatusInput.value == '') {
        messageVehicleStatus.innerHTML = 'Vehicle status is required'
    }
})
registrationNumberInput.addEventListener('blur', function() {
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
            canSubmit = false
            messageCheckRegistrationNumber.innerHTML = data.status
        }
        else {
            canSubmit = true
        }
    })
})
vehicleNameInput.addEventListener('blur', function(event) {
    if (vehicleNameInput.value == '') {
        messageVehicleName.innerHTML = 'Vehicle name is required'
    }
})

registrationNumberInput.addEventListener('keydown', function(event) {
    messageCheckRegistrationNumber.innerHTML = ''
})
vehiclePriceInput.addEventListener('keydown', function(event) {
    messageVehiclePrice.innerHTML = ''
})
vehicleNameInput.addEventListener('keydown', function(event) {
    messageVehicleName.innerHTML = ''
})

vehicleStatusInput.addEventListener('keyup', function(event) {
    if (Number(vehicleStatusInput.value)) {
        if (Number(vehicleStatusInput.value) < 0 || Number(vehicleStatusInput.value) > 100) {
            messageVehicleStatus.innerHTML = '0 <= Vehicle status <= 100'
            canSubmit = false
        }
        else {
            canSubmit = true
            messageVehicleStatus.innerHTML = ''
        }
    }
})

vehicleSeatsInput.addEventListener('keyup', function(event) {
    if (Number(vehicleSeatsInput.value) || Number(vehicleSeatsInput.value) == 0) {
        if (Number(vehicleSeatsInput.value) <= 0) {
            console.log(Number(vehicleSeatsInput.value))
            vehicleSeatsInput.value = ""
            messageVehicleSeats.innerHTML = 'Vehicle seats must be greater than 0'
            canSubmit = false
        }
        else {
            canSubmit = true
            messageVehicleSeats.innerHTML = ''
        }
    }
})

vehiclePriceInput.addEventListener('keyup', function(event) {
    if (Number(vehiclePriceInput.value) || Number(vehiclePriceInput.value) == 0) {
        if (Number(vehiclePriceInput.value) <= 0) {
            console.log(Number(vehiclePriceInput.value))
            vehiclePriceInput.value = ""
            messageVehiclePrice.innerHTML = 'Vehicle price must be greater than 0'
            canSubmit = false
        }
        else {
            canSubmit = true
            messageVehiclePrice.innerHTML = ''
        }
    }
})


buttonSubmit.addEventListener('click', function() {
    if (canSubmit && registrationNumberInput.value != '' && vehicleNameInput.value != '' && vehicleSeatsInput.value != '' && vehiclePriceInput.value != '' && vehicleStatusInput.value != '') {
        fetch('/addVehicle', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                vehicleCode: vehicleCodeInput.value,
                vehicleCategory: vehicleCategoryInput.value,
                vehicleType: vehicleTypeInput.value,
                registrationNumber: registrationNumberInput.value,
                vehicleName: vehicleNameInput.value,
                vehicleSeats: vehicleSeatsInput.value,
                vehiclePrice: vehiclePriceInput.value,
                vehicleStatus: vehicleStatusInput.value
            })
        })
        .then(response => response.json())
        .then(function (data) {
            if (data.status == "success") {
                alert('Add vehicle success')
                vehicleCategory.value = ''
                vehicleType.value = ''
                registrationNumberInput.value = ''
                vehicleNameInput.value = ''
                vehicleSeatsInput.value = ''
                vehiclePriceInput.value = ''
                vehicleStatusInput.value = ''
                getNextVehicleCode()
                location.reload()
            }
            else {
                alert('Add vehicle fail')
            }
        })
    }
    else {
        if (registrationNumberInput.value == '') {
            messageCheckRegistrationNumber.innerHTML = 'Registration number is required'
        }
        if (vehicleNameInput.value == '') {
            messageVehicleName.innerHTML = 'Vehicle name is required'
        }
        if (vehicleSeatsInput.value == '') {
            messageVehicleSeats.innerHTML = 'Vehicle seats is required'
        }
        if (vehiclePriceInput.value == '') {
            messageVehiclePrice.innerHTML = 'Vehicle price is required'
        }
        if (vehicleStatusInput.value == '') {
            messageVehicleStatus.innerHTML = 'Vehicle status is required'
        }
    }
})

// cac ham xu ly
function getNextVehicleCode() {
    fetch('/getNextVehicleCode')
    .then(response => response.json())
    .then(function (data) {
        vehicleCodeInput.value = data.id
    })
}
// cac IIFE
getNextVehicleCode()