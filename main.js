/**
 * Water Damage Restoration Arvada - Simple Clean Script
 * Domain: waterdamagerestorationarvada.com
 * Phone: (720) 735-8908
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Header scroll shadow
  const header = document.getElementById('main-header') || document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header?.classList.add('is-sticky', 'shadow-md');
    } else {
      header?.classList.remove('is-sticky');
    }
  });

  // 2. Mobile Nav Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const mobileNav = document.getElementById('mobile-nav');
  if (mobileToggle && mobileNav) {
    mobileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      mobileNav.classList.toggle('hidden');
    });
  }

  // 3. Simple FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const toggle = item.querySelector('.faq-toggle');
    toggle?.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // 4. Simple Quote Form Submission
  const quoteForm = document.getElementById('hero-quote-form');
  quoteForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = quoteForm.querySelector('button[type="submit"]');
    if (btn) {
      btn.disabled = true;
      btn.textContent = 'Sending...';
      setTimeout(() => {
        alert('Thank you! Your emergency request has been received. Our on-call technician will call you shortly at (720) 735-8908.');
        quoteForm.reset();
        btn.disabled = false;
        btn.textContent = 'Send Request to On-Call Tech';
      }, 800);
    }
  });

  // 5. Dynamic Year
  const yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
});
