// Remove Loader
window.addEventListener('load', () => {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.opacity = '0';
        setTimeout(() => loader.remove(), 500);
    }
});

// Scroll animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-slide-up').forEach((el) => observer.observe(el));

// 3D Tilt Effect
const tiltElements = document.querySelectorAll('.tiltable');
tiltElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = ((y - centerY) / centerY) * -5;
        const rotateY = ((x - centerX) / centerX) * 5;
        el.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });
    
    el.addEventListener('mouseleave', () => {
        el.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
    });
});

// Mobile menu toggle
const menuToggle = document.getElementById('mobile-menu');
const navLinks = document.getElementById('nav-links');
if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Form Focus Effects for Floating Labels
document.querySelectorAll('.form-group input, .form-group select, .form-group textarea').forEach(input => {
    const group = input.parentElement;
    
    // Check initial state
    if (input.value !== '') {
        group.classList.add('has-content');
    }

    input.addEventListener('focus', () => {
        group.classList.add('has-content');
    });

    input.addEventListener('blur', () => {
        if(input.value === '') {
            group.classList.remove('has-content');
        }
    });
});
