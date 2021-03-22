/* Add event listener to all fields in the form */
document.getElementById('studentID').addEventListener('keyup', validateStudentId);
document.getElementById('firstName').addEventListener('keyup', validateFirstName);
document.getElementById('lastName').addEventListener('keyup', validateLastName);
document.getElementById('email').addEventListener('keyup', validateEmail);
document.getElementById('username').addEventListener('keyup', validateUsername);
document.getElementById('password').addEventListener('keyup', validatePassword);
document.getElementById('confirmPassword').addEventListener('keyup', validateConfirmPassword);


/* Validate name, email, and message before enabling users to submit form */
function submitForm() {
    var valid_student_id = validateStudentId();
    var valid_first_name = validateFirstName();
    var valid_last_name = validateLastName();
    var valid_email = validateEmail();
    var valid_username = validateUsername();
    var valid_password = validatePassword();
    var valid_confirm_password = validateConfirmPassword();

    // All fields need to be valid to enable to submit button
    if (valid_student_id &&
        valid_first_name &&
        valid_last_name &&
        valid_email &&
        valid_username &&
        valid_password &&
        valid_confirm_password) {
        document.getElementById('submit').disabled = false;
    }
    else {
        document.getElementById('submit').disabled = true;
    }
}

/* This function checks the studentID entered by user.
 * Student ID should only contain digits, and 8 digits long.
 */
function validateStudentId() {
    const studentID = document.getElementById('studentID');
    const re = /^[0-9]{8}$/;

    if(!re.test(studentID.value)){
        studentID.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        studentID.classList.remove('is-invalid');
        studentID.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
    }
}

/* This function checks the name entered by user.
 * Name should only contain letters, and between 2 - 100 characters long.
 */
function validateFirstName() {
    const firstName = document.getElementById('firstName');
    const re = /^[a-zA-Z ]{2,100}$/;

    if ((!re.test(firstName.value)) || (firstName.value.trim() == "")) {
        firstName.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        firstName.classList.remove('is-invalid');
        firstName.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
    }
}

/* This function checks the name entered by user.
 * Name should only contain letters, and between 2 - 100 characters long.
 */
function validateLastName() {
    const lastName = document.getElementById('lastName');
    const re = /^[a-zA-Z ]{2,100}$/;

    if ((!re.test(lastName.value)) || (lastName.value.trim() == "")) {
        lastName.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        lastName.classList.remove('is-invalid');
        lastName.classList.add('is-valid');
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

/* This function checks the username entered by user.
 * Username must be between 6 and 15 characters of letters or digits, without space.
 */
function validateUsername() {
    const username = document.getElementById('username');
    const re = /^[a-zA-Z0-9]{6,15}$/;

    if(!re.test(username.value)){
        username.classList.add('is-invalid')
        document.getElementById('submit').disabled = true;
    }
    else {
        username.classList.remove('is-invalid');
        username.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
    }
}

/* This function checks the username entered by user.
 * Password must be between 8 - 15 characters, contain at least one uppercase letter, one lowercase letter, one number
 and one special character.
 */
function validatePassword() {
    const password = document.getElementById('password');

    const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;

    if(!re.test(password.value)){
        password.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
    }
    else {
        password.classList.remove('is-invalid');
        password.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
    }
}

/* This function ensures that the password reentered for confirm password is the same as the first password entered. */
function validateConfirmPassword() {
	const password = document.getElementById('password');
	const confirmPassword = document.getElementById('confirmPassword');

	if ((confirmPassword.value == "") || (password.value != confirmPassword.value)) {
		confirmPassword.classList.add('is-invalid');
        document.getElementById('submit').disabled = true;
	}
	else {
		confirmPassword.classList.remove('is-invalid');
		confirmPassword.classList.add('is-valid');
        document.getElementById('submit').disabled = false;
        return true;
	}
}