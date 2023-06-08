function navigateToSignup(event) {

    event.preventDefault();
    window.location.href = '/signup';
}

function login(event) {

    event.preventDefault();
    // Get the email and password from the input fields
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    if (email=='admin' && password=='admin'){
        window.location.href = '/admin';
    }
    // Create a request payload
    const payload = {
        email: email,
        password: password
    };
    // Send a POST request to the '/user/login' endpoint
    fetch('http://localhost:8080/api/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
        .then(response => {
            if (response.ok) {
                // console.log("hiii")
                // Redirect to the dashboard or display a success message
                return response.json();
            } else {
                return response.json().then(errorData => {
                    
                    const error = document.getElementById('message');
                    error.textContent = 'Try again! Check email and password';
                    error.style.display = 'block';
                    throw new Error(errorData.message); // Throw an error with the message from the backend
                });
            }
        })
        .then(data => {
            
            localStorage.setItem('email', email);
            
            if(data.password=="true0"){
                window.location.href = '/form_add';
            }
            if(data.password=="true1"){
                window.location.href = `/form_update?id=${data.id}`;
            }
            if(data.password=="true2"){
                console.log(data.bankdetails)                
                const bankdetailsParam = encodeURIComponent(JSON.stringify(data.bankdetails));
                const url = `/form_show?bankdetails=${bankdetailsParam}`;
                window.location.href = url;
            }
            // // Extract the JWT token from the response headers
            // const token = data.authToken;
            // //   console.log(token)
            // // Save the token to local storage
            // Redirect to the dashboard or display a success message
            // window.location.href = '/form';
        })
        .catch(error => {
            // Display an error message
            console.error('Error:', error);
        });
}