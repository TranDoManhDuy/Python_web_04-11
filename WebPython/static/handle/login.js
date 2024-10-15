// let submitFormBtn = document.querySelector('#submitFormBtn')
// let exampleInputEmail = document.querySelector('#exampleInputEmail')
// let exampleInputPassword = document.querySelector('#exampleInputPassword')
// let customCheck = document.querySelector('#customCheck')

// console.log(submitFormBtn)
// console.log(exampleInputEmail)
// console.log(exampleInputPassword)

// function chuyentrang() {
//     window.location.href = "/home"
// }

// submitFormBtn.addEventListener('click', function() {
//     let email = exampleInputEmail.value
//     let password = exampleInputPassword.value
//     let check = customCheck.checked
//     let data = {
//         email: email,
//         password: password,
//         check: check
//     }
//     console.log(data)
    
//     fetch("/loginHandle", {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     }).then(res => {
//         console.log(res)
//         if (res.status === 200) {
//             chuyentrang()
//         }
//         return res.json()
//     }
//     ).then(data => {
//         console.log(data)
//     })
// })