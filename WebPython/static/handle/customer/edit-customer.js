listCustomerBtn = document.getElementById('listCustomerBtn');
addCustomerBtn = document.getElementById('addCustomerBtn');
buttonSubmit = document.getElementById('buttonSubmit');

messageCustomerPhone = document.getElementById('messageCustomerPhone');
messageCustomerIDLicense = document.getElementById('messageDriverLicenseId');
messageCustomerEmail = document.getElementById('messageCustomerEmail');
messageLastName = document.getElementById('messageLastName');
messageFirstName = document.getElementById('messageFirstName');
messageCCCD = document.getElementById('messageCCCD');

inputID = document.getElementById('customerId');
inputPhone = document.getElementById('customerPhone');
inputIDLicense = document.getElementById('driverLicenseId');
inputEmail = document.getElementById('customerEmail');
inputLastName = document.getElementById('lastName');
inputFirstName = document.getElementById('firstName');
inputCCCD = document.getElementById('cccd');

let dataGlobal = {}
isCanSubmit = true
// ///////////////////
// // Add Event Listener
listCustomerBtn.addEventListener('click', function () {
    window.location.href = '/customer_list';
});
addCustomerBtn.addEventListener('click', function () {
    window.location.href = '/customer_add';
});

inputPhone.addEventListener('blur', function () {
    if (inputPhone.value == '') {
        messageCustomerPhone.innerHTML = 'Phone is required';
    }
});
inputIDLicense.addEventListener('blur', function () {
    if (inputIDLicense.value == '') {
        messageCustomerIDLicense.innerHTML = 'ID License is required';
    }
});
inputEmail.addEventListener('blur', function () {
    if (inputEmail.value == '') {
        messageCustomerEmail.innerHTML = 'Email is required';
    }
});
inputLastName.addEventListener('blur', function () {
    if (inputLastName.value == '') {
        messageLastName.innerHTML = 'Last Name is required';
    }
});
inputFirstName.addEventListener('blur', function () {
    if (inputFirstName.value == '') {
        messageFirstName.innerHTML = 'First Name is required';
    }
});
inputCCCD.addEventListener('blur', function () {
    if (inputCCCD.value == '') {
        messageCCCD.innerHTML = 'CCCD is required';
    }
});

inputPhone.addEventListener('keyup', function (event) {
    phone = inputPhone.value;
    if (!/^\d+$/.test(phone)) {
        messageCustomerPhone.innerHTML = 'Phone number must be a number';
        isCanSubmit = false;
    } else
        if (phone != dataGlobal.phone) {
            if (phone.length != 10) {
                messageCustomerPhone.innerHTML = 'Phone number must be 10 characters';
                isCanSubmit = false;
            }
            if (phone.length == 10) {
                messageCustomerPhone.innerHTML = 'Phone number will be changed';
                isCanSubmit = true;
            }
        } else {
            messageCustomerPhone.innerHTML = '';
            isCanSubmit = true;
        }

});
inputIDLicense.addEventListener('keyup', function (event) {
    if (inputIDLicense.value != dataGlobal.idlicense) {
        if (inputIDLicense.value.length != 12) {
            messageCustomerIDLicense.innerHTML = 'Driver license id must be 12 characters';
            console.log(inputIDLicense.value.length)
            isCanSubmit = false;
        } else {
            fetch('/checkDriverLicenseId', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ driverLicenseId: inputIDLicense.value }),
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status == "fail") {
                        messageCustomerIDLicense.innerHTML = 'Driver license id has exist';
                        isCanSubmit = false;
                    } else {
                        messageCustomerIDLicense.innerHTML = 'Driver license id wil be changed';
                        isCanSubmit = true;
                    }
                })
        }
    } else {
        messageCustomerIDLicense.innerHTML = '';
        isCanSubmit = true;
    }

});
inputEmail.addEventListener('keyup', function (event) {
    if (inputEmail.value != dataGlobal.email) {
        fetch('/checkEmail', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: inputEmail.value }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.status == "fail") {
                    messageCustomerEmail.innerHTML = 'Email is exist';
                    isCanSubmit = false;
                } else {
                    messageCustomerEmail.innerHTML = 'Email will be changed';
                    isCanSubmit = true;
                }
            })
    } else {
        messageCustomerEmail.innerHTML = '';
        isCanSubmit = true;
    }
});
inputLastName.addEventListener('keyup', function (event) {
    if (inputLastName.value != dataGlobal.Lname) {
        fetch('/checkName', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: lastName.value })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status == "fail") {
                messageLastName.innerHTML = 'Invalid last name';
                isCanSubmit = false;
            } else {
                messageLastName.innerHTML = 'Last name will be changed';
                inputLastName.value = data.name;
                isCanSubmit = true;
            }
        });
    } else {
        messageLastName.innerHTML = '';
        isCanSubmit = true;
    }
});
inputFirstName.addEventListener('keyup', function (event) {
    if (inputFirstName.value != dataGlobal.Fname) {
        fetch('/checkName', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: inputFirstName.value })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status == "fail") {
                messageFirstName.innerHTML = 'Invalid first name';
                isCanSubmit = false;
            } else {
                messageFirstName.innerHTML = 'First name will be changed';
                inputFirstName.value = data.name;
                isCanSubmit = true;
            }
        });
    } else {
        messageFirstName.innerHTML = '';
        isCanSubmit = true;
    }
});
inputCCCD.addEventListener('keyup', function (event) {
    if (!/^\d+$/.test(cccd.value)) {
        messageCCCD.innerHTML = 'CCCD number must be a number';
        isCanSubmit = false;
    } else
        if (cccd.value != dataGlobal.SSN) {
            if (cccd.value.length != 12) {
                messageCCCD.innerHTML = 'CCCD must be 12 characters';
                isCanSubmit = false;
            } else {
                fetch('/checkCCCD', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ CCCD: inputCCCD.value })
                }).then(function (response) {
                    return response.json();
                }).then(function (data) {
                    if (data.status == "fail") {
                        messageCCCD.innerHTML = 'CCCD has exist';
                        isCanSubmit = false;
                    } else {
                        messageCCCD.innerHTML = '';
                        isCanSubmit = true;
                    }
                });
            }
        } else {
            messageCCCD.innerHTML = '';
            isCanSubmit = true;
        }
});

buttonSubmit.addEventListener('click', function () {
    if (isCanSubmit && inputPhone.value != '' && inputIDLicense.value != '' && inputEmail.value != '' && inputLastName.value != '' && inputFirstName.value != '' && inputCCCD.value != '') {
        fetch('/updateCustomer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: inputID.value,
                phone: inputPhone.value,
                idlicense: inputIDLicense.value,
                email: inputEmail.value,
                Lname: inputLastName.value,
                Fname: inputFirstName.value,
                CCCD: inputCCCD.value
            }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.status == 'success') {
                    alert('Update customer success');
                    location.reload();
                    window.location.href = '/customer_list';
                } else {
                    alert('Update customer fail');
                }
            });
    }
});

function renderUIData(data) {
    inputID.value = data.id
    inputPhone.value = data.phone
    inputIDLicense.value = data.idlicense
    inputEmail.value = data.email
    inputLastName.value = data.Lname
    inputFirstName.value = data.Fname
    inputCCCD.value = data.SSN
}
function getCustomerFix() {
    fetch('/getCustomerFix')
        .then(response => response.json())
        .then(data => {
            dataGlobal = data
            console.log(dataGlobal)
            renderUIData(dataGlobal)
        })
}
getCustomerFix()


