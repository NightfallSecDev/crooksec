/* Tailwind configuration and interactivity */

// Tailwind config for the CDN
tailwind.config = {
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                mono: ['JetBrains Mono', 'monospace'],
            },
            colors: {
                brand: {
                    cyan: '#06b6d4',
                    blue: '#3b82f6',
                    purple: '#8b5cf6',
                    dark: '#0f172a',
                    darker: '#020617',
                    accent: '#10b981'
                }
            },
            backgroundImage: {
                'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
            }
        }
    }
};

// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', () => {
    // -------------------------
    // Mobile Menu Toggle
    // -------------------------
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        const mobileMenuIcon = mobileMenuBtn.querySelector('i');

        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');

            if (mobileMenu.classList.contains('hidden')) {
                mobileMenuIcon.classList.remove('fa-xmark');
                mobileMenuIcon.classList.add('fa-bars');
            } else {
                mobileMenuIcon.classList.remove('fa-bars');
                mobileMenuIcon.classList.add('fa-xmark');
            }
        });

        // Close mobile menu when clicking a link
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenuIcon.classList.remove('fa-xmark');
                mobileMenuIcon.classList.add('fa-bars');
            });
        });
    }

    // -------------------------
    // Scroll Reveal Animations
    // -------------------------
    const revealElements = document.querySelectorAll('.reveal');

    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    };

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);

    // -------------------------
    // Advanced Cyber Interactivity
    // -------------------------

    // 1. Cursor Cyber-Spotlight & Parallax Effects
    const updateMouseVariables = (e) => {
        // Spotlight mapping
        const x = e.clientX;
        const y = e.clientY;
        document.documentElement.style.setProperty('--mouse-x', `${x}px`);
        document.documentElement.style.setProperty('--mouse-y', `${y}px`);

        // Parallax mapping (values between -1 and 1)
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        const moveX = (x - centerX) / centerX;
        const moveY = (y - centerY) / centerY;
        
        // Apply to any parallax elements
        const parallaxElements = document.querySelectorAll('.parallax-bg');
        parallaxElements.forEach(el => {
            const speed = el.getAttribute('data-speed') || 20;
            const xOffset = moveX * speed;
            const yOffset = moveY * speed;
            el.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
        });
    };
    
    window.addEventListener('mousemove', updateMouseVariables);

    // 2. Organic Glitch Controller
    const glitchElements = document.querySelectorAll('.glitch-effect');
    if (glitchElements.length > 0) {
        const triggerRandomGlitch = () => {
            // Select a random element
            const el = glitchElements[Math.floor(Math.random() * glitchElements.length)];
            
            // Apply active glitch class
            el.classList.add('glitch-active');
            
            // Remove it shortly after
            setTimeout(() => {
                el.classList.remove('glitch-active');
            }, Math.random() * 300 + 100); // Glitch lasts 100-400ms

            // Schedule next glitch
            setTimeout(triggerRandomGlitch, Math.random() * 4000 + 1000); // Next glitch in 1-5s
        };
        
        // Start the glitch loop
        setTimeout(triggerRandomGlitch, 2000);
    }

    // 3. Interactive Scanning Buttons
    const scanButtons = document.querySelectorAll('.btn-scan');
    scanButtons.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            btn.style.setProperty('--btn-mouse-x', `${x}px`);
            btn.style.setProperty('--btn-mouse-y', `${y}px`);
        });
    });

    // 4. Terminal Typing Simulator
    const typeTerminals = document.querySelectorAll('.terminal-type');
    
    const typeWriter = (element, text, speed = 30, i = 0) => {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(() => typeWriter(element, text, speed, i), speed + (Math.random() * 20)); // Add organic variance
        } else {
            // Finish typing
            element.classList.remove('typing');
        }
    };

    // Use Intersection Observer to trigger typing when scrolled into view
    const terminalObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const fullText = el.getAttribute('data-terminal-text');
                if (fullText && !el.classList.contains('typed')) {
                    el.innerHTML = ''; // Clear fallback text
                    el.classList.add('typing');
                    el.classList.add('typed'); // Mark as done so it doesn't repeat
                    
                    // Delay start slightly for effect
                    setTimeout(() => {
                        typeWriter(el, fullText, parseInt(el.getAttribute('data-type-speed') || 30));
                    }, 500);
                }
            }
        });
    }, { threshold: 0.5 });

    typeTerminals.forEach(el => {
        // Store the original text to type out
        if (!el.getAttribute('data-terminal-text')) {
            el.setAttribute('data-terminal-text', el.innerText || el.textContent);
        }
        // Only clear if we are going to type it (fallback for no-js)
        el.innerHTML = '<span class="opacity-20 block h-4"></span>'; // Placeholder to hold height roughly
        terminalObserver.observe(el);
    });
});
