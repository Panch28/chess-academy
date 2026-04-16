/**
 * GalleryCarousel - Vanilla JS curved carousel
 * Hooks into existing #galleryTrack populated by Firebase
 * Works on all screen sizes, no external dependencies
 */

class GalleryCarousel {
    constructor() {
        this.track = document.getElementById('galleryTrack');
        this.prevBtn = document.getElementById('galleryPrev');
        this.nextBtn = document.getElementById('galleryNext');
        this.centerLabel = document.getElementById('centerLabel');

        if (!this.track) return;

        this.currentIndex = 0;
        this.isDragging = false;
        this.startX = 0;
        this.dragDelta = 0;
        this.cards = [];

        // Wait for Firebase to populate cards, then init
        this.waitForCards();
    }

    waitForCards() {
        // If cards already exist, init immediately
        const existing = this.track.querySelectorAll('.gallery-item-3d');
        if (existing.length > 0) {
            this.cards = Array.from(existing);
            this.setup();
            return;
        }

        // Otherwise observe DOM for cards being added by Firebase
        const observer = new MutationObserver(() => {
            const items = this.track.querySelectorAll('.gallery-item-3d');
            if (items.length > 0) {
                observer.disconnect();
                this.cards = Array.from(items);
                this.setup();
            }
        });

        observer.observe(this.track, { childList: true, subtree: true });

        // Fallback: try again after 3s in case Firebase is slow
        setTimeout(() => {
            const items = this.track.querySelectorAll('.gallery-item-3d');
            if (items.length > 0 && this.cards.length === 0) {
                this.cards = Array.from(items);
                this.setup();
            }
        }, 3000);
    }

    setup() {
        if (this.cards.length === 0) return;

        this.currentIndex = Math.floor(this.cards.length / 2);
        this.updateClasses();
        this.bindEvents();
    }

    updateClasses() {
        this.cards.forEach((card, i) => {
            card.classList.remove('is-active', 'is-prev', 'is-next', 'is-far');

            const diff = i - this.currentIndex;

            if (diff === 0) {
                card.classList.add('is-active');
            } else if (diff === -1 || diff === 1) {
                card.classList.add(diff === -1 ? 'is-prev' : 'is-next');
            } else {
                card.classList.add('is-far');
            }
        });

        // Update center label
        if (this.centerLabel) {
            const activeCard = this.cards[this.currentIndex];
            const label = activeCard?.querySelector('.item-label');
            this.centerLabel.textContent = label ? label.textContent : '';
        }

        // Scroll active card into view smoothly
        const activeCard = this.cards[this.currentIndex];
        if (activeCard) {
            activeCard.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest',
                inline: 'center'
            });
        }
    }

    goTo(index) {
        const len = this.cards.length;
        this.currentIndex = Math.max(0, Math.min(len - 1, index));
        this.updateClasses();
    }

    next() { this.goTo(this.currentIndex + 1); }
    prev() { this.goTo(this.currentIndex - 1); }

    bindEvents() {
        // Button clicks
        this.prevBtn?.addEventListener('click', () => this.prev());
        this.nextBtn?.addEventListener('click', () => this.next());

        // Click on card to center it
        this.cards.forEach((card, i) => {
            card.addEventListener('click', () => {
                if (Math.abs(this.dragDelta) < 5) {
                    this.goTo(i);
                }
            });
        });

        // Mouse drag
        this.track.addEventListener('mousedown', e => this.onDragStart(e.clientX));
        window.addEventListener('mousemove', e => this.onDragMove(e.clientX));
        window.addEventListener('mouseup', () => this.onDragEnd());

        // Touch
        this.track.addEventListener('touchstart', e => {
            this.onDragStart(e.touches[0].clientX);
        }, { passive: true });

        this.track.addEventListener('touchmove', e => {
            this.onDragMove(e.touches[0].clientX);
        }, { passive: true });

        this.track.addEventListener('touchend', () => this.onDragEnd());

        // Keyboard
        document.addEventListener('keydown', e => {
            if (e.key === 'ArrowLeft') this.prev();
            if (e.key === 'ArrowRight') this.next();
        });

        // Auto-advance every 4s, pause on interaction
        this.startAutoPlay();

        this.track.addEventListener('mouseenter', () => this.stopAutoPlay());
        this.track.addEventListener('mouseleave', () => this.startAutoPlay());
        this.track.addEventListener('touchstart', () => this.stopAutoPlay(), { passive: true });
    }

    onDragStart(x) {
        this.isDragging = true;
        this.startX = x;
        this.dragDelta = 0;
        this.stopAutoPlay();
    }

    onDragMove(x) {
        if (!this.isDragging) return;
        this.dragDelta = x - this.startX;
    }

    onDragEnd() {
        if (!this.isDragging) return;
        this.isDragging = false;

        const threshold = 60;
        if (this.dragDelta < -threshold) this.next();
        else if (this.dragDelta > threshold) this.prev();

        this.startAutoPlay();
    }

    startAutoPlay() {
        this.stopAutoPlay();
        this.autoPlayTimer = setInterval(() => this.next(), 4000);
    }

    stopAutoPlay() {
        clearInterval(this.autoPlayTimer);
    }
}

// Init when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new GalleryCarousel());
} else {
    new GalleryCarousel();
}
