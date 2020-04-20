function validatePassword(){
    const pass = document.getElementById('password');
    const cpass = document.getElementById('confirm_password');
    const invalidMessage = 'Password must be 5-20 characters long with at least one lower-case, one upper-case, one-special case, one digit and no whitespace';
    var pValid = true;
    var cpValid = true;

    //USE REGEX FOR PASSWORD VALIDATION
    const regexValidator = /^(?!.*\s)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{5,20}$/;

    //ONLY CHECK IF INPUT HAS VALUE
    if(pass.value != ''){
        pValid = regexValidator.test(pass.value);
        if(!pValid){
            pass.classList.remove('is-valid');
            pass.classList.add('is-invalid');
            document.getElementById('passwordFeedback').textContent = invalidMessage;
        } else {
            pass.classList.remove('is-invalid');
            pass.classList.add('is-valid');
            document.getElementById('passwordFeedback').textContent = '';
        }
    } else {
        pass.classList.remove('is-valid');
        pass.classList.remove('is-invalid');
        document.getElementById('passwordFeedback').textContent = '';
    }

    if(cpass.value != ''){
        cpValid = regexValidator.test(cpass.value);
        if(!cpValid){
            cpass.classList.remove('is-valid');
            cpass.classList.add('is-invalid');
            document.getElementById('confirm_passwordFeedback').textContent = invalidMessage;
        } else {
            cpass.classList.remove('is-invalid');
            cpass.classList.add('is-valid');
            document.getElementById('confirm_passwordFeedback').textContent = '';
        }
    } else {
        cpass.classList.remove('is-valid');
        cpass.classList.remove('is-invalid');
        document.getElementById('confirm_passwordFeedback').textContent = '';
    }

    if(!pValid || !cpValid){
        document.getElementById('submit').disabled = true;
    } else {
        document.getElementById('submit').disabled = false;
    }
}

function validateEvent(){
    const date = document.getElementById('date');
    const fb_link = document.getElementById('fb_link');
    const invalidMessageDate = 'Please enter a valid date: YYYY-MM-DD'
    const invalidMessageFb = 'Please enter a facebook event link starting with \'https://www.facebook.com/events/\' followed by 10-20 digits and ending with \'/\''
    var fbValid = true;
    var dValid = true;

    //USE REGEX FOR VALIDATION
    const regexValidatorDate =  /^\d{4}-\d{2}-\d{2}$/;
    const regexValidatorFb = /^(https:\/\/www.facebook.com\/events\/)\d{10,20}\/$/;

    //ONLY CHECK IF INPUT HAS VALUE
    if(date.value != ''){
        dValid = regexValidatorDate.test(date.value);
        if(!dValid){
            date.classList.remove('is-valid');
            date.classList.add('is-invalid');
            document.getElementById('dateFeedback').textContent = invalidMessageDate;
        } else {
            date.classList.remove('is-invalid');
            date.classList.add('is-valid');
            document.getElementById('dateFeedback').textContent = '';
        }
    } else {
        date.classList.remove('is-valid');
        date.classList.remove('is-invalid');
        document.getElementById('dateFeedback').textContent = '';
    }

    if(fb_link.value != ''){
        fbValid = regexValidatorFb.test(fb_link.value);
        if(!fbValid){
            fb_link.classList.remove('is-valid');
            fb_link.classList.add('is-invalid');
            document.getElementById('fb_linkFeedback').textContent = invalidMessageFb;
        } else {
            fb_link.classList.remove('is-invalid');
            fb_link.classList.add('is-valid');
            document.getElementById('fb_linkFeedback').textContent = '';
        }
    } else {
        fb_link.classList.remove('is-valid');
        fb_link.classList.remove('is-invalid');
        document.getElementById('fb_linkFeedback').textContent = '';
    }

    if(!dValid || !fbValid){
        document.getElementById('submit').disabled = true;
    } else {
        document.getElementById('submit').disabled = false;
    }
}
