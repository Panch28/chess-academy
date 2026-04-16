document.addEventListener('DOMContentLoaded', () => {
    
    const preloader = document.getElementById('preloader');
      const navbar = document.getElementById('navbar');
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');
    
    gsap.registerPlugin(ScrollTrigger);
    
    setTimeout(() => {
          if (preloader) preloader.classList.add('hidden');
          initHeroAnimations();
          initTypewriter();
          initCountdown();
      }, 2200);
    
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 80) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    mobileToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        const icon = mobileToggle.querySelector('i');
        if (navMenu.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
    
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            const icon = mobileToggle.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        });
    });
    
    function initHeroAnimations() {
        const fadeElements = document.querySelectorAll('.gsap-fade');
        
        gsap.to(fadeElements, {
            opacity: 1,
            y: 0,
            duration: 1,
            stagger: 0.2,
            ease: 'power3.out'
        });
    }
    
    // Typewriter Animation
    function initTypewriter() {
        const typewriterEl = document.getElementById('typewriter');
        if (!typewriterEl) return;
        
        const phrases = [
            'Master the Board.',
            '<span class="gold">Conquer the Mind.</span>',
            'Dominate the Game.',
            '<span class="gold">Think Ahead.</span>'
        ];
        
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typeSpeed = 100;
        
        function type() {
            const currentPhrase = phrases[phraseIndex];
            
            if (isDeleting) {
                typewriterEl.innerHTML = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
                typeSpeed = 50;
            } else {
                typewriterEl.innerHTML = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
                typeSpeed = 100;
            }
            
            if (!isDeleting && charIndex === currentPhrase.length) {
                typeSpeed = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                typeSpeed = 500;
            }
            
            setTimeout(type, typeSpeed);
        }
        
        setTimeout(type, 1500);
    }
    
    // Countdown Timer
    function initCountdown() {
        const daysEl = document.getElementById('days');
        const hoursEl = document.getElementById('hours');
        const minutesEl = document.getElementById('minutes');
        const secondsEl = document.getElementById('seconds');
        
        if (!daysEl) return;
        
        const targetDate = new Date('May 1, 2026 00:00:00').getTime();
        
        function updateCountdown() {
            const now = new Date().getTime();
            const distance = targetDate - now;
            
            if (distance < 0) {
                daysEl.textContent = '00';
                hoursEl.textContent = '00';
                minutesEl.textContent = '00';
                secondsEl.textContent = '00';
                return;
            }
            
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            daysEl.textContent = String(days).padStart(2, '0');
            hoursEl.textContent = String(hours).padStart(2, '0');
            minutesEl.textContent = String(minutes).padStart(2, '0');
            secondsEl.textContent = String(seconds).padStart(2, '0');
        }
        
        updateCountdown();
        setInterval(updateCountdown, 1000);
    }
    
    const revealElements = document.querySelectorAll('.scroll-reveal');
    
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    };
    
    const revealOptions = {
        root: null,
        rootMargin: '0px 0px -80px 0px',
        threshold: 0.1
    };
    
    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
    
    revealElements.forEach(el => {
        revealObserver.observe(el);
    });
    
    gsap.utils.toArray('.scroll-reveal').forEach(element => {
        gsap.fromTo(element, 
            { opacity: 0, y: 50 },
            {
                opacity: 1,
                y: 0,
                duration: 0.8,
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: element,
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                }
            }
        );
    });
    
    document.querySelectorAll('.about-card, .feature-item, .course-card, .activity-card, .event-card, .gallery-item, .teacher-card').forEach((card, index) => {
        gsap.fromTo(card,
            { opacity: 0, y: 40, scale: 0.95 },
            {
                opacity: 1,
                y: 0,
                scale: 1,
                duration: 0.6,
                delay: index * 0.1,
                ease: 'power2.out',
                scrollTrigger: {
                    trigger: card,
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                }
            }
        );
    });
    
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.nav-links a');
    
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 250)) {
                current = section.getAttribute('id');
            }
        });
        
        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href').substring(1) === current) {
                item.classList.add('active');
            }
        });
    });
    
    const statNumbers = document.querySelectorAll('.stat-number');
    
    const animateCounter = (element) => {
        const target = parseInt(element.getAttribute('data-count'));
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            current += step;
            if (current < target) {
                element.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target + '+';
            }
        };
        
        updateCounter();
    };
    
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statItems = entry.target.querySelectorAll('.stat-number');
                statItems.forEach(stat => animateCounter(stat));
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    const statsGrid = document.querySelector('.stats-grid');
    if (statsGrid) {
        statsObserver.observe(statsGrid);
    }
    
    const aboutHugeStats = document.querySelector('.about-huge-stats');
    if (aboutHugeStats) {
        statsObserver.observe(aboutHugeStats);
    }
    
    const carouselTrack = document.getElementById('carouselTrack');
    const slides = document.querySelectorAll('.carousel-slide');
    const prevBtn = document.getElementById('carouselPrev');
    const nextBtn = document.getElementById('carouselNext');
    const dotsContainer = document.getElementById('carouselDots');
    
    if (carouselTrack && slides.length > 0) {
        let currentSlide = 0;
        const totalSlides = slides.length;
        
        slides.forEach((_, index) => {
            const dot = document.createElement('span');
            dot.classList.add('dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });
        
        const dots = document.querySelectorAll('.carousel-dots .dot');
        
        function updateCarousel() {
            carouselTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
            
            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentSlide);
            });
        }
        
        function goToSlide(index) {
            currentSlide = index;
            updateCarousel();
        }
        
        function nextSlide() {
            currentSlide = (currentSlide + 1) % totalSlides;
            updateCarousel();
        }
        
        function prevSlide() {
            currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
            updateCarousel();
        }
        
        prevBtn.addEventListener('click', prevSlide);
        nextBtn.addEventListener('click', nextSlide);
        
        let autoplayInterval = setInterval(nextSlide, 5000);
        
        const carouselContainer = document.getElementById('testimonialCarousel');
        carouselContainer.addEventListener('mouseenter', () => {
            clearInterval(autoplayInterval);
        });
        carouselContainer.addEventListener('mouseleave', () => {
            autoplayInterval = setInterval(nextSlide, 5000);
        });
    }
    
    const form = document.getElementById('contactForm');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const btn = form.querySelector('button[type="submit"]');
            const originalContent = btn.innerHTML;
            
            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting...';
            btn.disabled = true;
            
            setTimeout(() => {
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Registration Submitted!';
                btn.style.background = 'linear-gradient(135deg, #22c55e, #16a34a)';
                
                setTimeout(() => {
                    btn.innerHTML = originalContent;
                    btn.style.background = '';
                    btn.disabled = false;
                    form.reset();
                }, 3000);
            }, 1500);
        });
    }
    
    document.querySelectorAll('.gallery-item').forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            
            gsap.to(item.querySelector('img'), {
                x: x * 10,
                y: y * 10,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
        
        item.addEventListener('mouseleave', () => {
            gsap.to(item.querySelector('img'), {
                x: 0,
                y: 0,
                duration: 0.5,
                ease: 'power2.out'
            });
        });
    });
    
    // 3D Chess King Animation - Floating Around
    (function initChessKing3D() {
        const canvas = document.getElementById('chessKing3D');
        if (!canvas || typeof THREE === 'undefined') return;
        
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ 
            canvas: canvas, 
            alpha: true, 
            antialias: true 
        });
        
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.setClearColor(0x000000, 0);
        
        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
        
        const mainLight = new THREE.DirectionalLight(0xd4af37, 2);
        mainLight.position.set(5, 10, 7);
        scene.add(mainLight);
        
        const fillLight = new THREE.DirectionalLight(0xffffff, 0.8);
        fillLight.position.set(-5, 5, -5);
        scene.add(fillLight);
        
        const rimLight = new THREE.PointLight(0xd4af37, 1.5, 30);
        rimLight.position.set(0, 5, -5);
        scene.add(rimLight);
        
        // Create Chess King
        const kingGroup = new THREE.Group();
        
        const goldMaterial = new THREE.MeshStandardMaterial({
            color: 0xd4af37,
            metalness: 0.95,
            roughness: 0.05,
            emissive: 0xd4af37,
            emissiveIntensity: 0.15
        });
        
        // Base
        const baseGeometry = new THREE.CylinderGeometry(0.8, 1, 0.3, 32);
        const base = new THREE.Mesh(baseGeometry, goldMaterial);
        base.position.y = -2;
        kingGroup.add(base);
        
        // Base ring
        const baseRingGeometry = new THREE.TorusGeometry(0.85, 0.08, 16, 32);
        const baseRing = new THREE.Mesh(baseRingGeometry, goldMaterial);
        baseRing.rotation.x = Math.PI / 2;
        baseRing.position.y = -1.82;
        kingGroup.add(baseRing);
        
        // Body
        const bodyGeometry = new THREE.CylinderGeometry(0.4, 0.7, 1.5, 32);
        const body = new THREE.Mesh(bodyGeometry, goldMaterial);
        body.position.y = -1;
        kingGroup.add(body);
        
        // Collar
        const collarGeometry = new THREE.TorusGeometry(0.5, 0.1, 16, 32);
        const collar = new THREE.Mesh(collarGeometry, goldMaterial);
        collar.rotation.x = Math.PI / 2;
        collar.position.y = -0.1;
        kingGroup.add(collar);
        
        // Neck
        const neckGeometry = new THREE.CylinderGeometry(0.25, 0.4, 0.6, 32);
        const neck = new THREE.Mesh(neckGeometry, goldMaterial);
        neck.position.y = 0.4;
        kingGroup.add(neck);
        
        // Crown body
        const crownBodyGeometry = new THREE.CylinderGeometry(0.5, 0.3, 1, 32);
        const crownBody = new THREE.Mesh(crownBodyGeometry, goldMaterial);
        crownBody.position.y = 1.2;
        kingGroup.add(crownBody);
        
        // Crown ring
        const crownRingGeometry = new THREE.TorusGeometry(0.55, 0.08, 16, 32);
        const crownRing = new THREE.Mesh(crownRingGeometry, goldMaterial);
        crownRing.rotation.x = Math.PI / 2;
        crownRing.position.y = 1.7;
        kingGroup.add(crownRing);
        
        // Cross on top
        const crossVerticalGeometry = new THREE.BoxGeometry(0.12, 0.5, 0.12);
        const crossVertical = new THREE.Mesh(crossVerticalGeometry, goldMaterial);
        crossVertical.position.y = 2.5;
        kingGroup.add(crossVertical);
        
        const crossHorizontalGeometry = new THREE.BoxGeometry(0.35, 0.12, 0.12);
        const crossHorizontal = new THREE.Mesh(crossHorizontalGeometry, goldMaterial);
        crossHorizontal.position.y = 2.7;
        kingGroup.add(crossHorizontal);
        
        // Small orb at top
        const orbGeometry = new THREE.SphereGeometry(0.1, 32, 32);
        const orb = new THREE.Mesh(orbGeometry, goldMaterial);
        orb.position.y = 2.85;
        kingGroup.add(orb);
        
        // Decorative elements (small spheres on crown)
        const sphereGeometry = new THREE.SphereGeometry(0.08, 16, 16);
        const crownSpheres = [];
        for (let i = 0; i < 8; i++) {
            const sphere = new THREE.Mesh(sphereGeometry, goldMaterial);
            const angle = (i / 8) * Math.PI * 2;
            sphere.position.x = Math.cos(angle) * 0.5;
            sphere.position.z = Math.sin(angle) * 0.5;
            sphere.position.y = 1.6;
            crownSpheres.push(sphere);
            kingGroup.add(sphere);
        }
        
        // Add glow effect sphere
        const glowGeometry = new THREE.SphereGeometry(3.5, 32, 32);
        const glowMaterial = new THREE.MeshBasicMaterial({
            color: 0xd4af37,
            transparent: true,
            opacity: 0.05
        });
        const glow = new THREE.Mesh(glowGeometry, glowMaterial);
        kingGroup.add(glow);
        
        scene.add(kingGroup);
        
        camera.position.set(-1, 1, 8);
        
        // Path points for the king to follow
        const pathPoints = [
            { x: 3.5, y: 2.5 },    // Top right
            { x: 3, y: 0.5 },      // Right middle
            { x: 3.5, y: -1.5 },    // Bottom right
            { x: 2, y: -2 },        // Bottom center-right
            { x: 0.5, y: -1 },      // Center-right
            { x: 0, y: 1 },         // Center
            { x: -2, y: 2 },        // Top left
            { x: -3, y: 0.5 },     // Left middle
            { x: -2.5, y: -1.5 },  // Bottom left
            { x: -1, y: -2.5 },    // Bottom center-left
            { x: 1, y: -2 },        // Bottom center
            { x: 2.5, y: -0.5 },    // Right
            { x: 3.5, y: 2.5 },     // Back to top right
        ];
        
        let currentPathIndex = 0;
        let pathProgress = 0;
        const pathSpeed = 0.003;
        
        let mouseX = 0;
        let mouseY = 0;
        let scrollOffset = 0;
        
        window.addEventListener('scroll', () => {
            const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
            scrollOffset = (window.scrollY / maxScroll) * 2;
        });
        
        window.addEventListener('mousemove', (e) => {
            mouseX = (e.clientX / window.innerWidth - 0.5) * 0.3;
            mouseY = (e.clientY / window.innerHeight - 0.5) * 0.2;
        });
        
        
    const prBtn = document.getElementById('galleryPrev');
    const nxBtn = document.getElementById('galleryNext');
    if (prBtn && nxBtn) {
        prBtn.addEventListener('click', () => {
            if(typeof targetScroll !== 'undefined') targetScroll -= getSpacing();
            if(typeof resetAutoplay === 'function') resetAutoplay();
        });
        nxBtn.addEventListener('click', () => {
            if(typeof targetScroll !== 'undefined') targetScroll += getSpacing();
            if(typeof resetAutoplay === 'function') resetAutoplay();
        });
    }
    
    // Export init3DGallery globally if it is inside DOMContentLoaded
    window.init3DGallery = init3DGallery;

    window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
        
        function lerp(start, end, t) {
            return start + (end - start) * t;
        }
        
        function animate() {
            requestAnimationFrame(animate);
            
            const time = Date.now() * 0.001;
            
            // Move along path
            pathProgress += pathSpeed;
            if (pathProgress >= 1) {
                pathProgress = 0;
                currentPathIndex = (currentPathIndex + 1) % pathPoints.length;
            }
            
            const nextIndex = (currentPathIndex + 1) % pathPoints.length;
            const currentPoint = pathPoints[currentPathIndex];
            const nextPoint = pathPoints[nextIndex];
            
            // Smooth easing
            const easeProgress = pathProgress * pathProgress * (3 - 2 * pathProgress);
            
            // Calculate position with smooth transition
            let targetX = lerp(currentPoint.x, nextPoint.x, easeProgress) + mouseX;
            let targetY = lerp(currentPoint.y, nextPoint.y, easeProgress) + mouseY - scrollOffset;
            
            // Smooth interpolation for current position
            kingGroup.position.x += (targetX - kingGroup.position.x) * 0.03;
            kingGroup.position.y += (targetY - kingGroup.position.y) * 0.03;
            kingGroup.position.z = 3;
            
            // Gentle rotation
            kingGroup.rotation.y = time * 0.3;
            kingGroup.rotation.x = Math.sin(time * 0.5) * 0.1;
            kingGroup.rotation.z = Math.cos(time * 0.4) * 0.05;
            
            // Floating scale effect
            const baseScale = 0.8 + Math.sin(time * 0.8) * 0.05;
            kingGroup.scale.set(baseScale, baseScale, baseScale);
            
            // Animate crown spheres
            crownSpheres.forEach((sphere, i) => {
                sphere.position.y = 1.6 + Math.sin(time * 2 + i * 0.5) * 0.08;
            });
            
            // Glow pulse
            glow.scale.setScalar(1 + Math.sin(time * 1.5) * 0.1);
            glowMaterial.opacity = 0.03 + Math.sin(time * 1.5) * 0.02;
            
            // Camera slight follow
            camera.position.x = -1 + mouseX * 0.3;
            camera.position.y = 1 - scrollOffset * 0.2;
            camera.lookAt(kingGroup.position.x * 0.3, kingGroup.position.y * 0.3, 0);
            
            renderer.render(scene, camera);
        }
        
        // Start animation after preloader
        setTimeout(() => {
            animate();
        }, 2300);
        
        // Initialize 3D Circular Gallery
        init3DGallery();
    })();
    
    // Staggered fade in intersection observer
    const staggerObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                staggerObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2, rootMargin: '0px 0px -50px 0px' });
    
    document.querySelectorAll('.stagger-about').forEach(el => staggerObserver.observe(el));
});

// Pure CSS 3D Curved Gallery
function init3DGallery() {
    const wrapper = document.getElementById('circularGallery');
    const track = document.getElementById('galleryTrack');
    const centerLabel = document.getElementById('centerLabel');
    const prevBtn = document.getElementById('galleryPrev');
    const nextBtn = document.getElementById('galleryNext');
    if (!wrapper || !track) return;
    
    // Only bind events and loops ONCE
    if (window._galleryInitialized) {
        // Just force an update
        if (window._updateGallery) window._updateGallery();
        return;
    }
    window._galleryInitialized = true;

    let currentScroll = 0;
    let targetScroll = 0;
    let velocity = 0;
    let isDragging = false;
    let lastX = 0;
    let animationId = null;
    let autoPlayTimer = null;
    let autoplayPaused = false;
    
    function startAutoplay() {
        if(autoPlayTimer) clearInterval(autoPlayTimer);
        autoPlayTimer = setInterval(() => {
            if(!autoplayPaused) {
                targetScroll += getSpacing();
            }
        }, 4000);
    }
    function resetAutoplay() { startAutoplay(); }
    function getSpacing() { return window.innerWidth <= 768 ? window.innerWidth * 0.75 + 15 : 440; }

    window._updateGallery = function updateGallery() {
        const items = track.querySelectorAll('.gallery-item-3d');
        if (items.length === 0) return;
        
        const spacing = getSpacing();
        const maxScroll = (items.length - 1) * spacing;
        
        if(currentScroll > maxScroll + spacing) {
            currentScroll = 0;
            targetScroll = 0;
        }

        let centerIndex = Math.round(currentScroll / spacing);
        centerIndex = Math.max(0, Math.min(centerIndex, items.length - 1));
        
        if (items[centerIndex]) {
            const lbl = items[centerIndex].querySelector('.item-label');
            if(lbl && centerLabel) {
                centerLabel.textContent = lbl.textContent;
                centerLabel.classList.add('active');
            }
        }
        
        items.forEach((item, index) => {
            const distance = (index * spacing) - currentScroll;
            const diffRatio = distance / spacing;
            const x = distance;
            
            const absRatio = Math.abs(diffRatio);
            const rotateY = diffRatio * -25;
            const translateZ = absRatio * -100;
            let scale = 1 - Math.min(0.3, absRatio * 0.2); 
            const opacity = Math.max(0, 1 - absRatio * 0.5); 
            const zIndex = 100 - Math.round(absRatio * 10);
            
            if (item.matches(':hover') && absRatio < 0.2) scale += 0.03;
            
            item.style.transform = `translateX(${x}px) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`;
            item.style.opacity = opacity;
            item.style.zIndex = zIndex;
            
            const img = item.querySelector('img');
            if (img) {
                if (absRatio < 0.2) img.style.filter = 'grayscale(0%) saturate(120%)';
                else img.style.filter = 'grayscale(100%)';
            }
        });
    }

    function animate() {
        if (!isDragging) {
            velocity *= 0.9;
            currentScroll += (targetScroll - currentScroll) * 0.1;
        } else {
            currentScroll = targetScroll;
        }
        
        const spacing = getSpacing();
        const items = track.querySelectorAll('.gallery-item-3d');
        const maxScroll = Math.max(0, (items.length - 1) * spacing);
        if(currentScroll < -spacing/2) currentScroll = targetScroll = -spacing/2;
        
        window._updateGallery();
        animationId = requestAnimationFrame(animate);
    }
    
    function snapToNearest() {
        const spacing = getSpacing();
        const items = track.querySelectorAll('.gallery-item-3d');
        let nearestIndex = Math.round(targetScroll / spacing);
        nearestIndex = Math.max(0, Math.min(nearestIndex, items.length - 1));
        targetScroll = nearestIndex * spacing;
    }

    wrapper.addEventListener('mousedown', (e) => {
        isDragging = true; autoplayPaused = true;
        lastX = e.clientX; wrapper.style.cursor = 'grabbing';
    });
    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        targetScroll -= (e.clientX - lastX) * 1.5;
        lastX = e.clientX;
    });
    window.addEventListener('mouseup', () => {
        if (!isDragging) return;
        isDragging = false; wrapper.style.cursor = 'grab';
        snapToNearest(); autoplayPaused = false; resetAutoplay();
    });
    
    wrapper.addEventListener('touchstart', (e) => {
        isDragging = true; autoplayPaused = true; lastX = e.touches[0].clientX;
    }, {passive: true});
    window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        targetScroll -= (e.touches[0].clientX - lastX) * 1.5;
        lastX = e.touches[0].clientX;
    });
    window.addEventListener('touchend', () => {
        if (!isDragging) return;
        isDragging = false; snapToNearest(); autoplayPaused = false; resetAutoplay();
    });

    wrapper.addEventListener('mouseenter', () => autoplayPaused = true);
    wrapper.addEventListener('mouseleave', () => {
        if(!isDragging) autoplayPaused = false;
        targetScroll = currentScroll; 
    });

    if (prevBtn) prevBtn.addEventListener('click', () => { targetScroll -= getSpacing(); snapToNearest(); });
    if (nextBtn) nextBtn.addEventListener('click', () => { targetScroll += getSpacing(); snapToNearest(); });

    wrapper.style.cursor = 'grab';
    startAutoplay();
    animate();
}

window.init3DGallery = init3DGallery;



// ── ACTIVITIES CAROUSEL ──────────────────────────────────────────────
(function initActivitiesCarousel() {
    var track   = document.getElementById('activitiesTrack');
    var prevBtn = document.getElementById('activitiesPrev');
    var nextBtn = document.getElementById('activitiesNext');
    if (!track || !prevBtn || !nextBtn) return;

    var cards = track.querySelectorAll('.activity-card');
    if (cards.length === 0) return;

    var offset = 0;

    function getVisible() {
        var w = window.innerWidth;
        if (w >= 1200) return 4;
        if (w >= 900)  return 3;
        if (w >= 600)  return 2;
        return 2;
    }

    function maxOffset() {
        return Math.max(0, cards.length - Math.floor(getVisible()));
    }

    function getCardWidth() {
        if (!cards[0]) return 240;
        var rect = cards[0].getBoundingClientRect();
        return rect.width + 20;
    }

    function update() {
        track.style.transform = 'translateX(-' + (offset * getCardWidth()) + 'px)';
        prevBtn.disabled = offset <= 0;
        nextBtn.disabled = offset >= maxOffset();
    }

    prevBtn.addEventListener('click', function() {
        if (offset > 0) { offset--; update(); }
    });

    nextBtn.addEventListener('click', function() {
        if (offset < maxOffset()) { offset++; update(); }
    });

    var touchStartX = 0;
    track.parentElement.addEventListener('touchstart', function(e) {
        touchStartX = e.touches[0].clientX;
    }, { passive: true });
    track.parentElement.addEventListener('touchend', function(e) {
        var diff = touchStartX - e.changedTouches[0].clientX;
        if (Math.abs(diff) > 50) {
            if (diff > 0) nextBtn.click();
            else prevBtn.click();
        }
    });

    window.addEventListener('resize', function() {
        if (offset > maxOffset()) offset = maxOffset();
        update();
    });

    update();
})();

// -- ACTIVITIES GALLERY (same engine as init3DGallery, separate IDs) --
function initActivitiesGallery() {
    var wrapper = document.getElementById('actGallery');
    var track = document.getElementById('actGalleryTrack');
    var centerLabel = document.getElementById('actCenterLabel');
    var prevBtn = document.getElementById('actGalleryPrev');
    var nextBtn = document.getElementById('actGalleryNext');
    if (!wrapper || !track) return;
    if (window._actGalleryInit) { if (window._updateActGallery) window._updateActGallery(); return; }
    window._actGalleryInit = true;
    var cur = 0, tgt = 0, dragging = false, lastX = 0, timer = null, paused = false;

    function spacing() { return window.innerWidth <= 768 ? window.innerWidth * 0.75 + 15 : 440; }

    function startAuto() {
        if (timer) clearInterval(timer);
        timer = setInterval(function() { if (!paused) tgt += spacing(); }, 4000);
    }

    window._updateActGallery = function() {
        var items = track.querySelectorAll('.gallery-item-3d');
        if (!items.length) return;
        var sp = spacing();
        var ci = Math.max(0, Math.min(Math.round(cur / sp), items.length - 1));
        if (items[ci] && centerLabel) {
            var l = items[ci].querySelector('.item-label');
            if (l) { centerLabel.textContent = l.textContent; centerLabel.classList.add('active'); }
        }
        items.forEach(function(item, i) {
            var dist = i * sp - cur;
            var ratio = dist / sp;
            var absR = Math.abs(ratio);
            item.style.transform = 'translateX(' + dist + 'px) translateZ(' + (absR * -100) + 'px) rotateY(' + (ratio * -25) + 'deg) scale(' + (1 - Math.min(0.3, absR * 0.2)) + ')';
            item.style.opacity = Math.max(0, 1 - absR * 0.5);
            item.style.zIndex = 100 - Math.round(absR * 10);
            var img = item.querySelector('img');
            if (img) img.style.filter = absR < 0.2 ? 'grayscale(0%) saturate(120%)' : 'grayscale(100%)';
        });
    };

    function snap() {
        var sp = spacing();
        var items = track.querySelectorAll('.gallery-item-3d');
        var ni = Math.max(0, Math.min(Math.round(tgt / sp), items.length - 1));
        tgt = ni * sp;
    }

    function loop() {
        cur += (tgt - cur) * 0.1;
        window._updateActGallery();
        requestAnimationFrame(loop);
    }

    wrapper.addEventListener('mousedown', function(e) { dragging = true; paused = true; lastX = e.clientX; wrapper.style.cursor = 'grabbing'; });
    window.addEventListener('mousemove', function(e) { if (!dragging) return; tgt -= (e.clientX - lastX) * 1.5; lastX = e.clientX; });
    window.addEventListener('mouseup', function() { if (!dragging) return; dragging = false; wrapper.style.cursor = 'grab'; snap(); paused = false; startAuto(); });
    wrapper.addEventListener('touchstart', function(e) { dragging = true; paused = true; lastX = e.touches[0].clientX; }, { passive: true });
    window.addEventListener('touchmove', function(e) { if (!dragging) return; tgt -= (e.touches[0].clientX - lastX) * 1.5; lastX = e.touches[0].clientX; });
    window.addEventListener('touchend', function() { if (!dragging) return; dragging = false; snap(); paused = false; startAuto(); });
    wrapper.addEventListener('mouseenter', function() { paused = true; });
    wrapper.addEventListener('mouseleave', function() { if (!dragging) { paused = false; tgt = cur; } });
    if (prevBtn) prevBtn.addEventListener('click', function() { tgt -= spacing(); snap(); });
    if (nextBtn) nextBtn.addEventListener('click', function() { tgt += spacing(); snap(); });

    wrapper.style.cursor = 'grab';
    startAuto();
    loop();
}

window.initActivitiesGallery = initActivitiesGallery;

