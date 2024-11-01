danhsachHD = document.getElementById('danhsachHD');
themHD = document.getElementById('themHD');
buttonSubmit = document.getElementById('buttonSubmit');

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

let dataGlobal = {}
isCanSubmit = true
// ///////////////////
danhsachHD.addEventListener('click', function () {
    window.location.href = '/orders_list';
});
themHD.addEventListener('click', function () {
    window.location.href = '/orders_add';
});
//
inputemployeeName.addEventListener('blur', function () {
    if (inputemployeeName.value == '') {
        messageemployeeName.innerHTML = 'Employee Name is required';
        isCanSubmit = false;
    }
});
inputemployeeName.addEventListener('keydown', function () {
    messageemployeeName.innerHTML = '';
});
inputemployeeName.addEventListener('keyup', function () {
    if (inputemployeeName.value != dataGlobal.IdStaff) {
        // fetch(/checkStaff, {) đợi chị thảo :))))))))))))))))))

    }
});
inputrenterCccd.addEventListener('blur', function () {
    if (inputrenterCccd.value == '') {
        messagerenterCccd.innerHTML = 'CCCD is required';
        isCanSubmit = false;
    }
});
inputrenterCccd.addEventListener('keydown', function () {
    messagerenterCccd.innerHTML = '';
});
inputrenterCccd.addEventListener('keyup', function () {
    if (inputrenterCccd.value != dataGlobal.IdCustomer) {
        // fetch(/checkCustomer, {)
        fetch('/checkCCCD', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ CCCD: inputrenterCccd.value })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status == "fail") {
                messagerenterCccd.innerHTML = 'CCCD will be changed';
                isCanSubmit = true;
            } else {
                messagerenterCccd.innerHTML = 'CCCD not found';
                isCanSubmit = false;
            }
        });

    }
});
inputvehicleRegNumber.addEventListener('blur', function () {
    if (inputvehicleRegNumber.value == '') {
        messagevehicleRegNumber.innerHTML = 'Vehicle Reg Number is required';
        isCanSubmit = false;
    }
});
inputvehicleRegNumber.addEventListener('keydown', function () {
    messagevehicleRegNumber.innerHTML = '';
});
inputvehicleRegNumber.addEventListener('keyup', function () {
    if (inputvehicleRegNumber.value != dataGlobal.IdProducts) {
        fetch('/checkRegistrationNumber', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ registrationNumber: inputvehicleRegNumber.value })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
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
buttonSubmit.addEventListener('click', function (event) {
    if (isCanSubmit && inputinvoiceId.value != '' && inputorderDate.value != '' && inputemployeeName.value != '' && inputendTime.value != '' && inputrenterCccd.value != '' && inputvehicleRegNumber.value != '') {
        fetch("/editOrder", {
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
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            if (data.status == 'success') {
                alert('Update order success');
                window.location.href = '/orders_list';
            } else
                if (data.status == 'fail') {
                    alert('Update order fail');
                }
                else {
                    alert(data.error);
                }

        });
    } else {
        alert('Please fill all field');
    }
})

function renderUIData(data) {
    inputinvoiceId.value = data.Id
    inputorderDate.value = data.DateOfBooking
    inputemployeeName.value = data.IdStaff
    inputendTime.value = data.DateOfEnd
    inputrenterCccd.value = data.IdCustomer
    inputvehicleRegNumber.value = data.IdProducts
    inputpaymentStatus.value = data.Status
}
function getOrderFix() {
    fetch('/getOrderFix')
        .then(response => response.json())
        .then(data => {
            dataGlobal = data
            console.log(data)
            renderUIData(data)
        })
}
getOrderFix()