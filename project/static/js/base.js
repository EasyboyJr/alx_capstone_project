// save reference of the dom in containers
const toggleButton = document.querySelector('.toggle-button');
const navbarLinks = document.querySelector('.navbar-links');

// add event listener to the toggle button
toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
})

// form validation

const nameError = document.getElementById('name-error');
const emailError = document.getElementById('email-error');
const messageError = document.getElementById('message-error');
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    // Validate the name field
    const name = document.getElementById('validate-name').value;
    const email = document.getElementById('validate-email').value;
    const message = document.getElementById('validate-message').value;
    
    if (name.length === 0) {
        nameError.innerHTML = 'Name is required';
        event.preventDefault();
    } else if (!name.match(/^[A-Za-z]{3,}$/)) {
        nameError.innerHTML = 'Enter a valid name';
        event.preventDefault();
    }

    if (email.length === 0) {
        emailError.innerHTML = 'Email is required';
        event.preventDefault();
    } else if (!email.match(/^\S+@\S+\.\S+$/)) {
        emailError.innerHTML = 'Enter a valid email address';
        event.preventDefault();
    }

    if (message.length === 0) {
        messageError.innerHTML = 'Message is required';
        event.preventDefault();
    } else if (message.length < 10) {
        messageError.innerHTML = 'Message should be at least 10 characters long';
        event.preventDefault();
    }


});

