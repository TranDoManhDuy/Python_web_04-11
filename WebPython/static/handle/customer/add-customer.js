customerPhone = document.getElementById('customerPhone');
driverLicenseId = document.getElementById('driverLicenseId');
customerEmail = document.getElementById('customerEmail');
lastName = document.getElementById('lastName');
firstName = document.getElementById('firstName');
cccd = document.getElementById('cccd');
buttonAddCustomer = document.getElementById('buttonAddCustomer');
// ///////////////////////
messagecustomerPhone = document.getElementById('messagecustomerPhone');
messagedriverLicenseId = document.getElementById('messagedriverLicenseId');
messagecustomerEmail = document.getElementById('messagecustomerEmail');
messagelastName = document.getElementById('messagelastName');
messagefirstName = document.getElementById('messagefirstName');
messagecccd = document.getElementById('messagecccd');



chuyentrangDSKH = document.getElementById('chuyentrangDSKH');
loadThemKH = document.getElementById('loadThemKH');

let canSubmit = true;

loadThemKH.addEventListener('click', function () {
    location.reload();
});

chuyentrangDSKH.addEventListener('click', function () {
    console.log('chuyen trang')
    fetch('/chuyentrang_listCustomer')
        .then(function (response) {
            if (response.redirected) {
                window.location.href = response.url;
            }
        })
});

customerPhone.addEventListener('blur', function (event) {
    if (customerPhone.value == '') {
        messagecustomerPhone.innerHTML = 'Customer phone is required';
    }
});
customerPhone.addEventListener('keydown', function (event) {
    messagecustomerPhone.innerHTML = '';
});
customerPhone.addEventListener('keyup', function (event) {
    phone = customerPhone.value;
    if (!/^\d+$/.test(phone)) {
        messagecustomerPhone.innerHTML = 'Phone number must be a number';
        canSubmit = false;
    } else
        if (phone.length != 10) {
            messagecustomerPhone.innerHTML = 'Phone number must be 10 characters';
            canSubmit = false;
        }
    if (phone.length == 10) {
        messagecustomerPhone.innerHTML = '';
        canSubmit = true;
    }
});
driverLicenseId.addEventListener('blur', function (event) {
    if (driverLicenseId.value == '') {
        messagedriverLicenseId.innerHTML = 'Driver license id is required';
    }
});
driverLicenseId.addEventListener('keydown', function (event) {
    messagedriverLicenseId.innerHTML = '';
});
driverLicenseId.addEventListener('keyup', function (event) {
    driverLicenseId.value;
    if (driverLicenseId.value.length != 12) {
        messagedriverLicenseId.innerHTML = 'Driver license id must be 12 characters';
        canSubmit = false;
    } else {
        fetch('/checkDriverLicenseId', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ driverLicenseId: driverLicenseId.value })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status == "fail") {
                messagedriverLicenseId.innerHTML = 'Driver license id has exist';
                canSubmit = false;
            } else {
                messagedriverLicenseId.innerHTML = '';
                canSubmit = true;
            }
        });
    }
});
customerEmail.addEventListener('blur', function (event) {
    if (customerEmail.value == '') {
        messagecustomerEmail.innerHTML = 'Customer email is required';
    }
});
customerEmail.addEventListener('keydown', function (event) {
    messagecustomerEmail.innerHTML = '';
});
customerEmail.addEventListener('keyup', function (event) {
    fetch('/checkEmail', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: customerEmail.value })
    }).then(function (response) {
        return response.json();
    }).then(function (data) {
        if (data.status == "fail") {
            messagecustomerEmail.innerHTML = 'Email is exist';
            canSubmit = false;
        } else {
            messagecustomerEmail.innerHTML = '';
            canSubmit = true;
        }
    });
});
lastName.addEventListener('blur', function (event) {
    if (lastName.value == '') {
        messagelastName.innerHTML = 'Last name is required';
    }
});
lastName.addEventListener('keydown', function (event) {
    messagelastName.innerHTML = '';
});
lastName.addEventListener('keyup', function (event) {
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
            messagelastName.innerHTML = 'Invalid last name';
            canSubmit = false;
        } else {
            messagelastName.innerHTML = '';
            lastName.value = data.name;
            canSubmit = true;
        }
    });


});
firstName.addEventListener('blur', function (event) {
    if (firstName.value == '') {
        messagefirstName.innerHTML = 'First name is required';
    }
});
firstName.addEventListener('keydown', function (event) {
    messagefirstName.innerHTML = '';
});
firstName.addEventListener('keyup', function (event) {
    fetch('/checkName', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: firstName.value })
    }).then(function (response) {
        return response.json();
    }).then(function (data) {
        if (data.status == "fail") {
            messagefirstName.innerHTML = 'Invalid fist name';
            canSubmit = false;
        } else {
            messagefirstName.innerHTML = '';
            firstName.value = data.name;
            canSubmit = true;
        }
    });
});
cccd.addEventListener('blur', function (event) {
    if (cccd.value == '') {
        messagecccd.innerHTML = 'CCCD is required';
    }
});
cccd.addEventListener('keydown', function (event) {
    messagecccd.innerHTML = '';
});
cccd.addEventListener('keyup', function (event) {
    if (!/^\d+$/.test(cccd.value)) {
        messagecccd.innerHTML = 'CCCD number must be a number';
        canSubmit = false;
    } else
        if (cccd.value.length != 12) {
            messagecccd.innerHTML = 'CCCD must be 12 characters';
            canSubmit = false;
        } else {
            fetch('/checkCCCD', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ CCCD: cccd.value })
            }).then(function (response) {
                return response.json();
            }).then(function (data) {
                if (data.status == "fail") {
                    messagecccd.innerHTML = 'CCCD has exist';
                    canSubmit = false;
                } else {
                    messagecccd.innerHTML = '';
                    canSubmit = true;
                }
            });
        }
});
buttonAddCustomer.addEventListener('click', function () {
    if (canSubmit && customerPhone.value != '' && driverLicenseId.value != '' && customerEmail.value != '' && lastName.value != '' && firstName.value != '' && cccd.value != '') {
        fetch('/addCustomer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                customerPhone: customerPhone.value,
                driverLicenseId: driverLicenseId.value,
                customerEmail: customerEmail.value,
                lastName: lastName.value,
                firstName: firstName.value,
                cccd: cccd.value
            })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status == "success") {
                alert('Add customer success');
                customerPhone.value = '';
                driverLicenseId.value = '';
                customerEmail.value = '';
                lastName.value = '';
                firstName.value = '';
                cccd.value = '';
                location.reload();
                
            } else {
                alert('Add customer fail');
            }
        });
    }
});