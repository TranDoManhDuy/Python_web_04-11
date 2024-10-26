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
let listProduct = {}

function fetchListProduct() {
    fetch("/products_getListPT")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        listProduct = data
        for (let i = 0; i < listProduct.length; i++) {
            console.log(listProduct[i])
            product = listProduct[i]
            listContainer.innerHTML += `<tr><td>#${product.id}</td><td>${product.danhmuc}</td><td>${product.loaiphuongtien}</td><td>${product.sodangki}</td><td>${product.tenphuongtien}</td><td>${product.sochongoi}</td><td>${product.giathue1n} VNĐ</td><td>${product.tinhtrangxe}%</td><td><a href="../products/edit-product.html" class="btn btn-sm btn-primary">Sửa</a></td></tr>`
        }
    })
}
fetchListProduct()