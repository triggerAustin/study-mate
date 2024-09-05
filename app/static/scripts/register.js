// manage the cancel button to reset the login form.
document.getElementById("cancel-button").addEventListener('click', function(){
    document.getElementById("registration").reset();
});

// manage the register form to send the data to the server.
document.getElementById("registration").addEventListener('submit', function(event){
    event.preventDefault()

    const password = document.getElementById("password").value;
    const passconf = document.getElementById("passcode-confirmation").value;

    // check if the passcode is correct.
    if (password === passconf) {
        let usersdata;
        usersdata = new FormData(document.getElementById('registration'));
        //austin please change to the regester endpoint
        fetch('/register', {
            method: 'POST', body: usersdata,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("welcome to studymate!");
                    window.location.href = '/web_static/login.html';
                }
                else {
                    alert("failed to register")
                }
            })

    }
    else{
        alert("passwords don't match");
        document.getElementById("registration").reset();
    }

});
