ListContainer = document.querySelector('#LIST_PRODUCT_CONTAINER')
CustomerSearch = document.querySelector('#InputCustomerSearch')
ButtonSearch = document.querySelector('#buttonSearch')
chuyentrangDSKH = document.querySelector('#chuyentrangDSKH')
themKH = document.querySelector('#themKH')

let listCustomer = {}
function getIDCustomerForFix(id) {
    fetch("/getIDCustomerForFix", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id
        })
    })
        .then(function (response) {
            return response.json()
        })
        .then(data => {
            if (data.status == "success") {
                fetch("/chuyentrang_fixCustomer")
                    .then(function (response) {
                        if (response.redirected) {
                            window.location.href = response.url
                        }
                    })
            }
        })
}

function renderListCustomer(listCustomer) {
    ListContainer.innerHTML = ''
    if (listCustomer.length == 0) {
        ListContainer.innerHTML = `<tr><td colspan="9">Không có dữ liệu</td></tr>`
    }
    for (let i = 0; i < listCustomer.length; i++) {
        console.log(listCustomer[i].id);
        customerI = listCustomer[i]
        ListContainer.innerHTML +=
            `<tr>
            <td>${customerI.id}</td>
            <td>${customerI.phone}</td>
            <td>${customerI.idlicense}</td>
            <td>${customerI.email}</td>
            <td>${customerI.Lname}</td>
            <td>${customerI.Fname}</td>
            <td>${customerI.SSN}</td>                   
            <td>
            <div style="cursor: pointer" class="btn btn-sm btn-primary" onclick=getIDCustomerForFix('${customerI.id}')>Sửa</div>
            </td>    
        </tr>`
    }
}
function fetchListCustomers() {
    fetch("/Customers_getListKH")
        .then(response => response.json())
        .then(data => {
            listCustomer = data
            renderListCustomer(listCustomer)
        })
}
function fetchListCustomersbyName() {
    fetch("/getListKHtheoTen", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            Fullname: CustomerSearch.value
        })
    })
        .then(response => response.json())
        .then(data => {
            listCustomer = data
            renderListCustomer(listCustomer)
        })
}
CustomerSearch.addEventListener('keyup', function () {
    fetchListCustomersbyName()
})
chuyentrangDSKH.addEventListener('click', function () {
    location.reload();
})
themKH.addEventListener('click', function () {
    fetch("/chuyentrang_addCustomer")
        .then(function (response) {
            if (response.redirected) {
                window.location.href = response.url
            }
        })
})
fetchListCustomers();