document.addEventListener('DOMContentLoaded', () => {
    // 1. Active State Highlight
    const currentPath = window.location.pathname;
    let pageName = currentPath.split('/').pop();
    if (!pageName) pageName = 'index.html';
    
    const navLinks = document.querySelectorAll('.main-nav .nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkHref = link.getAttribute('href');
        if (linkHref === pageName) {
            link.classList.add('active');
        }
    });

    // 2. Theme Toggle
    const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
    const htmlElement = document.documentElement;
    
    // Check local storage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    }

    if (themeToggleBtns.length > 0) {
        themeToggleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const currentTheme = htmlElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                
                htmlElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                updateThemeIcon(newTheme);
            });
        });
    }

    function updateThemeIcon(theme) {
        themeToggleBtns.forEach(btn => {
            if (theme === 'dark') {
                btn.innerHTML = '<i class="bi bi-sun"></i>';
            } else {
                btn.innerHTML = '<i class="bi bi-moon"></i>';
            }
        });
    }

    // 3. RTL Toggle
    const rtlToggleBtns = document.querySelectorAll('.rtl-toggle-btn');
    
    const savedDir = localStorage.getItem('dir');
    if (savedDir) {
        htmlElement.setAttribute('dir', savedDir);
    }

    if (rtlToggleBtns.length > 0) {
        rtlToggleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const currentDir = htmlElement.getAttribute('dir');
                const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
                
                htmlElement.setAttribute('dir', newDir);
                localStorage.setItem('dir', newDir);
            });
        });
    }

    // 4. Initialize AOS if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 50
        });
    }

    // 5. Header Scroll Effect (Premium Glassmorphism)
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // 6. Premium Animated Counters
    const counters = document.querySelectorAll('.counter-val');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = parseInt(entry.target.getAttribute('data-target'));
                    const duration = 2000;
                    const step = target / (duration / 16);
                    let current = 0;
                    
                    const updateCounter = () => {
                        current += step;
                        if (current < target) {
                            entry.target.innerText = Math.ceil(current).toLocaleString();
                            requestAnimationFrame(updateCounter);
                        } else {
                            entry.target.innerText = target.toLocaleString();
                        }
                    };
                    updateCounter();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(counter => counterObserver.observe(counter));
    }

    // 7. Mobile Menu Toggle
    const mobileToggleBtn = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');
    if (mobileToggleBtn && mainNav) {
        mobileToggleBtn.addEventListener('click', () => {
            mainNav.classList.toggle('show');
            
            // Toggle icon between hamburger and close
            const icon = mobileToggleBtn.querySelector('i');
            if (icon) {
                if (mainNav.classList.contains('show')) {
                    icon.classList.remove('bi-list');
                    icon.classList.add('bi-x-lg');
                } else {
                    icon.classList.remove('bi-x-lg');
                    icon.classList.add('bi-list');
                }
            }
        });
    }
});
