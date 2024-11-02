
{/* <td>#01</td>
<td>Nguyễn Thảo</td>
<td>0999888777</td>
<td>Quận 9, TP HCM</td>
<td>10,000,000 VNĐ</td>
<td>Quản trị</td>
<td>
  <a href="./edit-user.html" class="btn btn-sm btn-primary">Sửa</a>
  <a href="./edit-user.html" class="btn btn-sm btn-danger">Xóa</a>
</td>
</tr> */}
inputNameStaffElement = document.getElementById("inputNameStaff")
listStaffElement = document.getElementById("listStaff")

function fixStaff(data) {
    fetch("/postIDStaff", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => {
        window.location.href = "/edit_user"
    })
}

function renderListStaff(data) {
    if (data.length == 0) {
        listStaffElement.innerHTML = `
            <tr>
                <td colspan="7">Không có dữ liệu</td>
            </tr>
        `
        return
    }
    for (let i = 0; i < data.length; i++) {
        listStaffElement.innerHTML += `
            <tr>
                <td>#${data[i]["ID"]}</td>
                <td>${data[i]["FullName"]}</td>
                <td>${data[i]["PhoneNumber"]}</td>
                <td>${data[i]["Address"]}</td>
                <td>${data[i]["Salary"]} VNĐ</td>
                <td>${data[i]["Position"]}</td>
                <td>
                    <div class="btn btn-sm btn-primary" onclick=fixStaff('${data[i]["ID"]}')>Sửa</div>
                </td>
            </tr>
        `
    }
}
function getDataListStaff() {
    fetch("/getListStaff")
    .then((response) => response.json())
    .then((data) => {
        renderListStaff(data)
    })
}

inputNameStaffElement.addEventListener("keyup", (event) => {
    fetch("/getListStaffByName", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "FullName": inputNameStaffElement.value
        })
    })
    .then((response) => response.json())
    .then((data) => {
        listStaffElement.innerHTML = ""
        renderListStaff(data)
    })
})
getDataListStaff()