/* Add event listener to the fields of the form: name, email, and message */
document.getElementById('name').addEventListener('keyup', validateName);
document.getElementById('email').addEventListener('keyup', validateEmail);
document.getElementById('message').addEventListener('keyup', validateMessage);

/* Validate name, email, and message before enabling users to submit form */
function submitForm() {
    var valid_name = validateName();
    var valid_email = validateEmail();
    var valid_message = validateMessage();

    // All fields need to be valid to enable to submit button
    if (valid_name && valid_email && valid_message) {
        document.getElementById('submit').disabled = false;
    }
    else {
        document.getElementById('submit').disabled = true;
    }
}

/* This function checks the name entered by user.
 * Name should only contain letters, and between 3 - 100 characters long.
 */
function validateName() {
    const name = document.getElementById('name');
    const re = /^[a-zA-Z ]{3,100}$/;
 
    if ((!re.test(name.value)) || (name.value.trim() == "")) {
        name.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        name.classList.remove('is-invalid');
        name.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
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
        email.classList.remove('is-invalid');
        email.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
    }
}

/* This function checks the message entered by user.
 * Message should only contain letters, and between 3 - 1000 characters long.
 */
function validateMessage() {
    const message = document.getElementById('message');
    var min_length = 3;
    var max_length = 1000;
 
    if ((message.value.trim() == "") || (message.value.length < min_length) || (message.value.length > max_length)){
        message.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        message.classList.add('is-valid');
        message.classList.remove('is-invalid');
        document.getElementById('submit').disabled = false;
        return true;
    }
}