/**
 * firebase-live.js
 * Pulls live data from Firebase and injects it into the Chess Academy website.
 * Handles: Testimonials, Gallery, Events (cards + countdown), Hero Mini.
 *
 * Import this AFTER the main script.js in index.html as a module:
 *   <script type="module" src="firebase-live.js"></script>
 */

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import {
  getFirestore, collection, getDocs, getDoc, doc, query, orderBy
} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

import { firebaseConfig } from "./firebase-config.js";

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// ─────────────────────────────────────────────
//  Wait for DOM + main script to settle
// ─────────────────────────────────────────────
window.addEventListener('DOMContentLoaded', () => {
  // Small delay so the original script.js carousel init runs first,
  // then we overwrite with live data
  setTimeout(async () => {
    await Promise.allSettled([
      loadHeroMini(),
      loadTestimonials(),
      loadGallery(),
      loadActivitiesGallery(),
      loadEvents(),
      loadCountdown(),
    ]);
  }, 500);
});

// ─────────────────────────────────────────────
//  HERO MINI TESTIMONIAL
// ─────────────────────────────────────────────
async function loadHeroMini() {
  try {
    const snap = await getDoc(doc(db, 'config', 'heroMini'));
    if (!snap.exists()) return;
    const { text, author } = snap.data();
    const miniP = document.querySelector('.testimonial-mini p');
    const miniSpan = document.querySelector('.testimonial-mini span');
    if (miniP && text) miniP.textContent = `"${text}"`;
    if (miniSpan && author) miniSpan.textContent = `- ${author}`;
  } catch (e) {
    console.warn('[Firebase] Hero mini load failed:', e.message);
  }
}

// ─────────────────────────────────────────────
//  TESTIMONIALS CAROUSEL
// ─────────────────────────────────────────────
async function loadTestimonials() {
  try {
    const q = query(collection(db, 'testimonials'), orderBy('createdAt', 'desc'));
    const snap = await getDocs(q);
    if (snap.empty) return; // keep hardcoded fallbacks

    const track = document.getElementById('carouselTrack');
    const dotsContainer = document.getElementById('carouselDots');
    const prevBtn = document.getElementById('carouselPrev');
    const nextBtn = document.getElementById('carouselNext');
    if (!track) return;

    // Clear old hardcoded slides and dots
    track.innerHTML = '';
    if (dotsContainer) dotsContainer.innerHTML = '';

    const docs = [];
    snap.forEach(d => docs.push(d.data()));

    docs.forEach((data, i) => {
      const stars = '<i class="fa-solid fa-star"></i>'.repeat(data.rating || 5);
      const initial = (data.name || 'A').charAt(0).toUpperCase();
      const slide = document.createElement('div');
      slide.className = `testimonial-card carousel-slide${i === 0 ? ' active' : ''}`;
      slide.innerHTML = `
        <div class="testimonial-badge bg-gold text-black">${data.badge || 'Parent'}</div>
        <div class="stars gold-text">${stars}</div>
        <p class="text-light">"${data.text}"</p>
        <div class="testimonial-author">
          <div class="avatar bg-white text-black">${initial}</div>
          <div>
            <h5 class="text-white">${data.name}</h5>
            <span class="gold-text">${data.role || ''}</span>
          </div>
        </div>`;
      track.appendChild(slide);
    });

    // Re-init carousel with new slides
    initCarousel(track, dotsContainer, prevBtn, nextBtn);

  } catch (e) {
    console.warn('[Firebase] Testimonials load failed:', e.message);
  }
}

function initCarousel(track, dotsContainer, prevBtn, nextBtn) {
  const slides = track.querySelectorAll('.carousel-slide');
  let current = 0;

  const updateCarousel = () => {
    track.style.transform = `translateX(-${current * 100}%)`;
    if (dotsContainer) {
      dotsContainer.querySelectorAll('.dot').forEach((d, i) => {
        d.classList.toggle('active', i === current);
      });
    }
  };

  // Build dots
  if (dotsContainer) {
    slides.forEach((_, i) => {
      const dot = document.createElement('span');
      dot.className = `dot${i === 0 ? ' active' : ''}`;
      dot.addEventListener('click', () => { current = i; updateCarousel(); });
      dotsContainer.appendChild(dot);
    });
  }

  const next = () => { current = (current + 1) % slides.length; updateCarousel(); };
  const prev = () => { current = (current - 1 + slides.length) % slides.length; updateCarousel(); };

  if (prevBtn) prevBtn.onclick = prev;
  if (nextBtn) nextBtn.onclick = next;

  let auto = setInterval(next, 5000);
  const carousel = document.getElementById('testimonialCarousel');
  if (carousel) {
    carousel.addEventListener('mouseenter', () => clearInterval(auto));
    carousel.addEventListener('mouseleave', () => { auto = setInterval(next, 5000); });
  }

  updateCarousel();
}

// ─────────────────────────────────────────────
//  GALLERY
// ─────────────────────────────────────────────
async function loadGallery() {
  try {
    const q = query(collection(db, 'gallery'), orderBy('createdAt', 'desc'));
    const snap = await getDocs(q);
    if (snap.empty) return;

    const track = document.getElementById('galleryTrack');
    if (!track) return;
    track.innerHTML = '';

    const items = [];
    snap.forEach(d => {
        const item = d.data();
        items.push(item);
        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item-3d';
        galleryItem.innerHTML = `
          <img src="${item.url}" alt="${item.label}" loading="lazy">
          <div class="item-overlay">
            <div class="item-label">${item.label}</div>
          </div>`;
        track.appendChild(galleryItem);
    });

    // Clean up old gallery artifacts and re-initialize
    if (window.init3DGallery) {
        window.init3DGallery(); // assuming this re-parses from DOM!
    } else {
        // Fallback simple fetch update if there's an array somewhere
        if (window.galleryItemsArray) window.galleryItemsArray = items;
    }
  } catch (e) {
    console.warn('[Firebase] Gallery load failed:', e.message);
  }
}

// ─────────────────────────────────────────────
//  EVENTS CARDS
// ─────────────────────────────────────────────
async function loadEvents() {
  try {
    const q = query(collection(db, 'events'), orderBy('date', 'asc'));
    const snap = await getDocs(q);
    if (snap.empty) return;

    const eventsGrid = document.querySelector('.events-grid');
    if (!eventsGrid) return;

    const tagColors = {
      Tournament: 'bg-gold text-black',
      Workshop: 'bg-primary text-black',
      Camp: 'bg-success text-white',
      Online: 'bg-primary text-black',
      Special: 'bg-gold text-black',
    };

    const delayClasses = ['', 'delay-1', 'delay-2', 'delay-3'];

    eventsGrid.innerHTML = '';
    let i = 0;
    snap.forEach(d => {
      const data = d.data();
      const dt = data.date ? new Date(data.date) : null;
      const day = dt ? dt.getDate() : '--';
      const month = dt ? dt.toLocaleString('en', { month: 'short' }).toUpperCase() : '--';
      const tagClass = tagColors[data.tag] || 'bg-gold text-black';
      const delay = delayClasses[i % 4];
      eventsGrid.innerHTML += `
        <div class="event-card scroll-reveal ${delay}">
          <div class="event-date">
            <span class="event-day">${String(day).padStart(2,'0')}</span>
            <span class="event-month">${month}</span>
          </div>
          <div class="event-content">
            <span class="event-tag ${tagClass}">${data.tag}</span>
            <h3>${data.title}</h3>
            <p>${data.desc}</p>
            <div class="event-meta">
              ${data.time ? `<span><i class="fa-solid fa-clock"></i> ${data.time}</span>` : ''}
              ${data.location ? `<span><i class="fa-solid fa-location-dot"></i> ${data.location}</span>` : ''}
            </div>
          </div>
        </div>`;
      i++;
    });

    // Re-trigger scroll reveal on new cards
    const newCards = eventsGrid.querySelectorAll('.scroll-reveal');
    newCards.forEach(el => {
      if (el.getBoundingClientRect().top < window.innerHeight) {
        el.classList.add('active');
      }
    });

  } catch (e) {
    console.warn('[Firebase] Events load failed:', e.message);
  }
}

// ─────────────────────────────────────────────
//  COUNTDOWN
// ─────────────────────────────────────────────
async function loadCountdown() {
  try {
    const snap = await getDoc(doc(db, 'config', 'countdown'));
    if (!snap.exists()) return;

    const { title, date } = snap.data();
    const targetTs = new Date(date).getTime();

    // Update heading text
    const heading = document.querySelector('.countdown-wrapper h3');
    if (heading && title) heading.textContent = `Next Event: ${title}`;

    // Override the countdown with new target date
    const daysEl = document.getElementById('days');
    const hoursEl = document.getElementById('hours');
    const minutesEl = document.getElementById('minutes');
    const secondsEl = document.getElementById('seconds');
    if (!daysEl) return;

    // Clear any existing interval (can't access original, so we just start a fresh one
    // that overwrites the DOM every 1s — this wins since it runs last)
    function tick() {
      const dist = targetTs - Date.now();
      if (dist < 0) {
        daysEl.textContent = hoursEl.textContent = minutesEl.textContent = secondsEl.textContent = '00';
        return;
      }
      daysEl.textContent = String(Math.floor(dist / 86400000)).padStart(2, '0');
      hoursEl.textContent = String(Math.floor((dist % 86400000) / 3600000)).padStart(2, '0');
      minutesEl.textContent = String(Math.floor((dist % 3600000) / 60000)).padStart(2, '0');
      secondsEl.textContent = String(Math.floor((dist % 60000) / 1000)).padStart(2, '0');
    }

    tick();
    setInterval(tick, 1000);

  } catch (e) {
    console.warn('[Firebase] Countdown load failed:', e.message);
  }
}

// ─────────────────────────────────────────────
//  ACTIVITIES GALLERY
// ─────────────────────────────────────────────
async function loadActivitiesGallery() {
  try {
    const q = query(collection(db, 'activitiesGallery'), orderBy('createdAt', 'desc'));
    const snap = await getDocs(q);
    if (snap.empty) return;

    const track = document.getElementById('actGalleryTrack');
    if (!track) return;
    track.innerHTML = '';

    snap.forEach(d => {
      const item = d.data();
      const galleryItem = document.createElement('div');
      galleryItem.className = 'gallery-item-3d';
      galleryItem.innerHTML = `
        <img src="${item.url}" alt="${item.label}" loading="lazy">
        <div class="item-overlay">
          <div class="item-label">${item.label}</div>
        </div>`;
      track.appendChild(galleryItem);
    });

    // Reset and re-init activities gallery engine
    window._actGalleryInit = false;
    if (window.initActivitiesGallery) window.initActivitiesGallery();

  } catch (e) {
    console.warn('[Firebase] Activities Gallery load failed:', e.message);
  }
}
