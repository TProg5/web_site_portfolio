// Add floating animation to form elements
document.querySelectorAll('input, select, textarea').forEach(element => {
    element.addEventListener('focus', function() {
        this.style.transform = 'translateY(-2px)';
    });
    
    element.addEventListener('blur', function() {
        this.style.transform = 'translateY(0)';
    });
});