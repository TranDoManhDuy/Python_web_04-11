let inputEmail = document.querySelector('#exampleInputEmail')
let inputPassword = document.querySelector('#exampleInputPassword')
let btnSubmit = document.querySelector('#submitFormBtn')
let btnRememberLogin = document.querySelector('#customCheck')
btnSubmit.addEventListener('click', function() {
    fetch('/login_post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: inputEmail.value,
            password: inputPassword.value,
            remember: btnRememberLogin.checked
        })
    })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url;  // Chuyển hướng theo URL trả về
        }
        else {
            inputEmail.value = ''
            inputPassword.value = ''
            return response.json()
        }
    })
    .then(function (data) {
        if (data != undefined) {
            console.log(data)
        }
    })
})

inputEmail.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        inputPassword.focus()
    }
})
inputPassword.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        btnSubmit.click()
    }
})