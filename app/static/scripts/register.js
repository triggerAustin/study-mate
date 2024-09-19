let inputPwd = '';
let confPwd = '';
const cancelBtn = document.getElementById("cancelButton");
const pwd = document.getElementById('password');
const confirmPwd = document.getElementById('confirmPassword');
const pwdCheck = document.getElementById('pwdCheck');
const lenCheck = document.getElementById('len');
const numCheck = document.getElementById('num');
const caseCheck = document.getElementById('case');
const specCharCheck = document.getElementById('specialChar')
// manage the cancel button to reset the login form.
cancelBtn.addEventListener('click', function(){
//document.getElementById("cancel-button").addEventListener('click', function(){
    document.getElementById("registration").reset();
});

pwd.addEventListener('input', (ev) => {
	inputPwd = ev.target.value;
	if (inputPwd) {pwdCheck.style.display = 'block';}
	lenpt = /^.{8,16}$/
	nums = /(?=.*\d)/
	cases = /(?=.*[A-Z])/
	spec = /(?=.*[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~])/
	lenpt.test(inputPwd) ? lenCheck.style.color = 'green': lenCheck.style.color = 'red';
	nums.test(inputPwd) ? numCheck.style.color = 'green' : numCheck.style.color = 'red';
	cases.test(inputPwd) ? caseCheck.style.color = 'green': caseCheck.style.color = 'red';
	spec.test(inputPwd) ? specialChar.style.color = 'green' : specialChar.style.color = 'red';

});
confirmPwd.addEventListener('input', (ev) => {
        confPwd = ev.target.value;
	if (confPwd != inputPwd){
		confirmPwd.style.border = 'solid 1px red';
	}
	else{
		confirmPwd.style.border = 'transparent';
	}
})

// manage the register form to send the data to the server.
document.getElementById("registerButton").addEventListener('submit', function(event){
    event.preventDefault()

    const password = document.getElementById("password").value;
    const passconf = document.getElementById("confirmPassword").value;

    // check if the passcode is correct.
    if (password === passconf) {
        let usersdata;
        usersdata = new FormData(document.getElementById('registration'));
        //austin please change to the regester endpoint
        fetch('/register', {
            method: 'POST', body: usersdata,
            })
    }
    else{
        document.getElementById("error").innerHTML = "passwords don't match"
        document.getElementById("registration").reset();
    }

});
