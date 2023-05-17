// dash.js

function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    sidebar.classList.toggle('expanded');
    content.classList.toggle('expanded');
}
function toggleSidebar() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('open');
}

// Handle navigation click event
var navLinks = document.querySelectorAll('.nav-link');
for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', function (event) {
        event.preventDefault();
        var target = this.getAttribute('href');
        scrollToTarget(target);
    });
}
function setActiveNav(navItem) {
    var activeNav = document.querySelector('.nav-link.active');
    if (activeNav) {
        activeNav.classList.remove('active');
    }
    navItem.classList.add('active');
}
// Scroll to target element
function scrollToTarget(target) {
    var element = document.querySelector(target);
    element.scrollIntoView({ behavior: 'smooth' });
}

// Close the sidebar when a menu item is clicked
function setActiveNav(element) {
    var navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(function(link) {
        link.classList.remove('active');
    });
    element.classList.add('active');
}