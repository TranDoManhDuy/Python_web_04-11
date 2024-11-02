ListContainer = document.querySelector('#LIST_ORDER_CONTAINER')
OrderSearch = document.querySelector('#InputOrderSearch')
ButtonSearch = document.querySelector('#buttonSearch')

danhsachHD = document.querySelector('#danhsachHD')
themHD = document.querySelector('#themHD')

let listOrder = {}
function renderlistOrder(listOrder) {
    if (listOrder.length == 0) {
        ListContainer.innerHTML = `<tr><td colspan="9">Không có dữ liệu</td></tr>`
    }
    ListContainer.innerHTML = ''
    for (let i = 0; i < listOrder.length; i++) {
        orderI = listOrder[i]
        ListContainer.innerHTML +=
            `<tr>
            <td>${orderI.Id}</td>
            <td>${orderI.IdStaff}</td>
            <td>${orderI.DateOfBooking}</td>
            <td>${orderI.DateOfEnd}</td>
            <td>${orderI.IdCustomer}</td>
            <td>${orderI.IdProducts}</td>
            <td>chua co du lieu</td>
            <td>${orderI.Status}</td>                   
            <td>
            <div style="cursor: pointer" class="btn btn-sm btn-primary" onclick=getIDOrderForFix('${orderI.Id}')>Sửa</div>
            </td>    
        </tr>`
    }
}
function getIDOrderForFix(id) {
    
    fetch("/getIDOrderForFix", {
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
                console.log(data);
                fetch("/chuyentrang_fixOrder")
                    .then(function (response) {
                        if (response.redirected) {
                            window.location.href = response.url
                        }
                    })
            }
        })
}
function fetchListOrders() {
    fetch("/Orders_getListHD")
        .then(response => response.json())
        .then(data => {
            console.log(data);
            listOrder = data
            renderlistOrder(listOrder)
        })
}
OrderSearch.addEventListener('keyup', function (e) {
    fetch("/Orders_searchHD", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            key: OrderSearch.value
        })
    })
        .then(response => response.json())
        .then(data => {
            listOrder = data
            console.log(listOrder);
            renderlistOrder(listOrder)
        })
})
danhsachHD.addEventListener('click', function (e) {
    location.reload();
})
themHD.addEventListener('click', function (e) {
    window.location.href = "/orders_add"
})
fetchListOrders()