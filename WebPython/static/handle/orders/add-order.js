dsHD = document.getElementById('dsHD');
themHD = document.getElementById('themHD');
btnAddOrder = document.getElementById('btnAddOrder');

messageinvoiceId = document.getElementById('messageinvoiceId');
messageorderDate = document.getElementById('messageorderDate');
messageemployeeName = document.getElementById('messageemployeeName');
messageendTime = document.getElementById('messageendTime');
messagerenterCccd = document.getElementById('messagerenterCccd');
messagevehicleRegNumber = document.getElementById('messagevehicleRegNumber');
messagepaymentStatus = document.getElementById('messagepaymentStatus');

inputinvoiceId = document.getElementById('invoiceId');
inputorderDate = document.getElementById('orderDate');
inputemployeeName = document.getElementById('employeeName');
inputendTime = document.getElementById('endTime');
inputrenterCccd = document.getElementById('renterCccd');
inputvehicleRegNumber = document.getElementById('vehicleRegNumber');
inputpaymentStatus = document.getElementById('paymentStatus');

let isCanSubmit = true;
dsHD.addEventListener('click', function () {
    window.location.href = '/orders_list';
});
themHD.addEventListener('click', function () {
    location.reload();
});

inputemployeeName.addEventListener('blur', function () {
    if (inputemployeeName.value == '') {
        messageemployeeName.innerHTML = 'Employee Name is required';
    }
});
inputemployeeName.addEventListener('keydown', function () {
    messageemployeeName.innerHTML = '';
});
inputemployeeName.addEventListener('keyup', function () {
    // Đợi chị thảo :
    if (!/^\d+$/.test(inputemployeeName.value)) {
        messageemployeeName.innerHTML = 'ID number must be a number';
        isCanSubmit = false;
    } else
    // if (inputemployeeName.value.length != 12) {
    //     messageemployeeName.innerHTML = 'CCCD number must be 12 characters';
    //     canSubmit = false;
    // }
    {
        isCanSubmit = true;
    }
});

inputrenterCccd.addEventListener('blur', function () {
    if (inputrenterCccd.value == '') {
        messagerenterCccd.innerHTML = 'CCCD is required';
    }
});
inputrenterCccd.addEventListener('keydown', function () {
    messagerenterCccd.innerHTML = '';
});
inputrenterCccd.addEventListener('keyup', function () {
    if (!/^\d+$/.test(inputrenterCccd.value)) {
        messagerenterCccd.innerHTML = 'CCCD number must be a number';
        isCanSubmit = false;
    } else
        if (inputrenterCccd.value.length != 12) {
            messagerenterCccd.innerHTML = 'CCCD number must be 12 characters';
            isCanSubmit = false;
        } else {
            fetch('/checkCCCD', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    CCCD: inputrenterCccd.value
                })
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    if (data.status == 'fail') {
                        messagerenterCccd.innerHTML = '';
                        isCanSubmit = true;
                    } else {
                        messagerenterCccd.innerHTML='CCCD not found in the system, please add the customer first';
                        // messagerenterCccd.window.location.href = '/customer_add';
                        // isCanSubmit = false;
                        
                    }
                });
        }

});
inputvehicleRegNumber.addEventListener('blur', function () {
    if (inputvehicleRegNumber.value == '') {
        messagevehicleRegNumber.innerHTML = 'Vehicle Reg Number is required';
    }
});
inputvehicleRegNumber.addEventListener('keydown', function () {
    messagevehicleRegNumber.innerHTML = '';
});
inputvehicleRegNumber.addEventListener('keyup', function () {
    if (inputvehicleRegNumber.value != '') {
        fetch('/checkRegistrationNumber', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                registrationNumber: inputvehicleRegNumber.value
            })
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                if (data.status != 'existed registrationNumber' && data.status != 'OK') {
                    messagevehicleRegNumber.innerHTML = data.status;
                    isCanSubmit = false;
                }
                if (data.status == 'existed registrationNumber') {
                    messagevehicleRegNumber.innerHTML = '';
                    isCanSubmit = true;
                }
                if (data.status == 'OK') {
                    messagevehicleRegNumber.innerHTML = 'registrationNumber does not exist';
                    isCanSubmit = false;
                }
            });
    }
});
inputpaymentStatus.addEventListener('blur', function () {
    if (inputpaymentStatus.value == '') {
        messagepaymentStatus.innerHTML = 'Payment Status is required';
    }
});
inputpaymentStatus.addEventListener('keydown', function () {
    messagepaymentStatus.innerHTML = '';
});
inputorderDate.addEventListener('blur', function () {
    if (inputorderDate.value == '') {
        messageorderDate.innerHTML = 'Order Date is required';
    }
});
inputorderDate.addEventListener('keydown', function () {
    messageorderDate.innerHTML = '';
});
inputorderDate.addEventListener('keyup', function () {
    if (inputorderDate.value != '') {
        isCanSubmit = true;
    }
});
inputendTime.addEventListener('blur', function () {
    if (inputendTime.value == '') {
        messageendTime.innerHTML = 'End Time is required';
    }
});
inputendTime.addEventListener('keydown', function () {
    messageendTime.innerHTML = '';
});
inputendTime.addEventListener('keyup', function () {
    if (inputendTime.value != '') {
        isCanSubmit = true;
    }
});

btnAddOrder.addEventListener('click', function () {
    if (isCanSubmit && inputinvoiceId.value != '' && inputorderDate.value != '' && inputemployeeName.value != '' && inputendTime.value != '' && inputrenterCccd.value != '' && inputvehicleRegNumber.value != '' && inputpaymentStatus.value != '') {
        fetch('/checkCCCD', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                CCCD: inputrenterCccd.value
            })
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                if (data.status == 'fail') {
                    messagerenterCccd.innerHTML = '';
                    isCanSubmit = true;
                } else {
                    alert('CCCD not found in the system, please add the customer first');
                    isCanSubmit = false;
                    window.location.href = '/customer_add';
                }
            });
        if (isCanSubmit) {
            fetch("/addOrder", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    Id: inputinvoiceId.value,
                    DateOfBooking: inputorderDate.value,
                    IdStaff: inputemployeeName.value,
                    DateOfEnd: inputendTime.value,
                    IdCustomer: inputrenterCccd.value,
                    IdProducts: inputvehicleRegNumber.value,
                    Status: inputpaymentStatus.value
                })
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    if (data.status == 'success') {
                        alert('Add order success');
                        window.location.href = '/orders_list';
                    } else
                        if (data.status == 'fail') {
                            alert('Add order fail');
                        }
                        else {
                            alert(data.error);
                        }
                });
        }
    } else {
        alert('Please fill in all required fields');
    }
});
function getNewIdorder() {
    fetch('/getNewIdorder')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            inputinvoiceId.value = data.id;
        });
}
getNewIdorder();
