// js/sidebar.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('components/sidebar.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('sidebar').innerHTML = data;
            setActiveNavItem();
        })
        .catch(error => console.error('Error loading sidebar:', error));
});

function setActiveNavItem() {
    var currentPage = window.location.pathname.split('/').pop() || 'index.html';
    var navItems = document.querySelectorAll('.sidebar-nav-item');
    navItems.forEach(function(item) {
        if (item.getAttribute('href') === currentPage) {
            item.classList.add('active');
        }
    });
}