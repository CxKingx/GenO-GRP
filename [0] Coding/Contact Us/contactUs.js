/* Add event listener to the fields of the form: name, email, and message */
document.getElementById('name').addEventListener('blur', validateName);
document.getElementById('email').addEventListener('blur', validateEmail);
document.getElementById('message').addEventListener('blur', validateMessage);

/* Validate name, email, and message before enabling users to submit form */
function submitForm() {
    validateName();
    validateEmail();
    validateMessage();
}

/* This function checks the name entered by user.
 * Name should only contain letters, and between 3 - 50 characters long. 
 */
function validateName() {
    const name = document.getElementById('name');
    const re = /^[a-zA-Z ]{3,50}$/;
 
    if(!re.test(name.value)){
        name.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        name.classList.remove('is-invalid');
        name.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
    }
}

/* This function checks the email entered by user.
 * Email should only contain letters, digits, and allowed symbols. 
 */
function validateEmail() {
    const email = document.getElementById('email');
    const re = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;

    if(!re.test(email.value)){
        email.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        email.classList.add('is-valid');
        email.classList.remove('is-invalid');
        document.getElementById('submit').disabled = false;
    }
}

/* This function checks the message entered by user.
 * Message should only contain letters, and between 3 - 1000 characters long.
 */
function validateMessage() {
    const message = document.getElementById('message');
    var min_length = 3;
    var max_length = 1000;
 
    if((message.value.length < min_length) || (message.value.length > max_length)){
        message.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        message.classList.add('is-valid');
        message.classList.remove('is-invalid');
        document.getElementById('submit').disabled = false;
    }
}