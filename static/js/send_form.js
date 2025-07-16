document.getElementById('contactForm').addEventListener('submit', function(e) {
    
    const formData = new FormData(this);
    
    // Вариант 1: Отправка через fetch API (асинхронно)
    
    e.preventDefault();
    
    fetch('/api/contact', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccessMessage();
        } else {
            showErrorMessage();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showErrorMessage();
    });
    
    
    // Вариант 2: Стандартная отправка формы (синхронно)
    // Форма отправится автоматически на /contact с методом POST
    
    // Показываем состояние загрузки
    showLoadingState();
});

function showLoadingState() {
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.textContent = 'Sending...';
    submitBtn.style.opacity = '0.7';
    submitBtn.disabled = true;
}
function showSuccessMessage() {
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.textContent = 'Message Sent!';
    submitBtn.style.background = 'linear-gradient(45deg, #27ae60, #2ecc71)';
    submitBtn.disabled = false;
    
    setTimeout(() => {
        submitBtn.textContent = 'Send Message';
        submitBtn.style.background = 'linear-gradient(45deg, #ffe071, #ffd347)';
        submitBtn.style.opacity = '1';
        document.getElementById('contactForm').reset();
    }, 2000);
}
function showErrorMessage() {
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.textContent = 'Error! Try again';
    submitBtn.style.background = 'linear-gradient(45deg, #e74c3c, #c0392b)';
    submitBtn.disabled = false;
    
    setTimeout(() => {
        submitBtn.textContent = 'Send Message';
        submitBtn.style.background = 'linear-gradient(45deg, #ffe071, #ffd347)';
        submitBtn.style.opacity = '1';
    }, 2000);
} 