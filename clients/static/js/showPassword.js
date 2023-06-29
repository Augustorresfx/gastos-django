const showPasswordButton = document.querySelector('#showPassword');
const passwordInput = document.querySelector('#password');
showPasswordButton.addEventListener('click', () => {
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    showPasswordButton.innerHTML = '<i class="bi bi-eye-slash"></i>';
  } else {
    passwordInput.type = 'password';
    showPasswordButton.innerHTML = '<i class="bi bi-eye"></i>';
  }
});