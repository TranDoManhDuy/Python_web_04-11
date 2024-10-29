{/* <tr>
    <td>#01DXO</td>
    <td>Mercedes</td>
    <td>Sedan</td>
    <td>78154</td>
    <td>Mercedes</td>
    <td>6</td>
    <td>200,000 VNĐ</td>
    <td>100%</td>
    <td>
        <a href="../products/edit-product.html" class="btn btn-sm btn-primary">Sửa</a>
    </td>
</tr> */}
listContainer = document.querySelector('#LIST_PRODUCT_CONTAINER')
inputVNameSearch = document.querySelector('#inputVNameSearch')
buttonKXFile = document.querySelector('#buttonKXFile')
chuyentrangDSPT = document.querySelector('#chuyentrangDSPT')
themPT = document.querySelector('#themPT')

// du lieu trang
let listProduct = {}
// Cac ham xu ly
function getIDForFix(id) {
    id = Number(id)
    fetch("/getIDForFix", {
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
            fetch("/chuyentrang_fixProduct")
            .then(function (response) { 
                if (response.redirected) {
                    window.location.href = response.url
                }
            })
        }
    })
}

function renderListProduct(listProduct) { 
    listContainer.innerHTML = ''
    if (listProduct.length == 0) {
        listContainer.innerHTML = `<tr><td colspan="9">Không có dữ liệu</td></tr>`
    }
    console.log(listProduct)
    for (let i = 0; i < listProduct.length; i++) {
        productI = listProduct[i]
        listContainer.innerHTML += 
        `<tr>
            <td>#${productI.id}</td>
            <td>${productI.danhmuc}</td>
            <td>${productI.loaiphuongtien}</td>
            <td>${productI.sodangki}</td>
            <td>${productI.tenphuongtien}</td>
            <td>${productI.sochongoi}</td>
            <td>${productI.giathue1n} VNĐ</td>
            <td>${productI.tinhtrangxe}%</td>
            <td>${productI.ready}</td>
            <td>
            <div style="cursor: pointer" class="btn btn-sm btn-primary" onclick=getIDForFix('${productI.id}')>Sửa</div>
            </td>
        </tr>`
    }
}
function fetchListProduct() {
    fetch("/products_getListPT")
    .then(response => response.json())
    .then(data => {
        listProduct = data
        renderListProduct(listProduct)
    })
}
function fetchListProduct_byName() {
    fetch("/products_getListPTtheoTen", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            tenphuongtien: inputVNameSearch.value
        })
    })
    .then(response => response.json())
    .then(data => {
        listProduct = data
        renderListProduct(listProduct)
    })
}

// bat su kien c
inputVNameSearch.addEventListener('keyup', function() {
    fetchListProduct_byName()
})
chuyentrangDSPT.addEventListener('click', function() {
    location.reload()
})
themPT.addEventListener('click', function() {
    fetch("/chuyentrang_addProduct")
    .then(function (response) { 
        if (response.redirected) {
            window.location.href = response.url
        }
    })
})

buttonKXFile.addEventListener('click', function() {
    fetch("/downloadFileExel", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            filename: "productslist.xlsx"
        })
    })
        .then(response => {
            console.log(response);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'dataProductslist.xlsx'); // Đặt tên file chính xác
            document.body.appendChild(link);
            link.click();
            link.remove();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => console.error('There was a problem with the fetch operation:', error));
})
// Cac ham thuc thi khi reload trang
fetchListProduct()