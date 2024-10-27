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
buttonSearch = document.querySelector('#buttonSearch')
chuyentrangDSPT = document.querySelector('#chuyentrangDSPT')
themPT = document.querySelector('#themPT')

// du lieu trang
let listProduct = {}

// Cac ham xu ly
function renderListProduct(listProduct) { 
    listContainer.innerHTML = ''
    if (listProduct.length == 0) {
        listContainer.innerHTML = `<tr><td colspan="9">Không có dữ liệu</td></tr>`
    }
    for (let i = 0; i < listProduct.length; i++) {
        product = listProduct[i]
        listContainer.innerHTML += `<tr><td>#${product.id}</td><td>${product.danhmuc}</td><td>${product.loaiphuongtien}</td><td>${product.sodangki}</td><td>${product.tenphuongtien}</td><td>${product.sochongoi}</td><td>${product.giathue1n} VNĐ</td><td>${product.tinhtrangxe}%</td><td><a href="../products/edit-product.html" class="btn btn-sm btn-primary">Sửa</a></td></tr>`
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
// Cac ham thuc thi khi reload trang
fetchListProduct()