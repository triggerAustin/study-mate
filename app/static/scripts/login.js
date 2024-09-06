/* manage the login form and redirect the user
to the proper page student dashboard for the students and
the teacher dashboard for the teachers
 */
document.getElementById("login").addEventListener("submit", function(event){
    event.preventDefault();

    /* collect the user data and send it to the server to validate the login */
    /*austin please change the login to the proper endpoint */
    let user_data = new FormData(document.getElementById("loginForm"));

    fetch("/studyMate/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: user_data
    })
)
