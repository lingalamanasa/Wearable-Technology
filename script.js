// ===== SPLASH SCREEN =====
window.addEventListener('load', () => {
  const splashScreen = document.getElementById('splashScreen');
  if (splashScreen) {
    setTimeout(() => {
      splashScreen.classList.add('hidden');
      document.body.style.overflow = 'auto';
    }, 2800);
  }
});

// ===== MOBILE MENU TOGGLE =====
const hamburger = document.querySelector('.hamburger');
const navLinks = document.getElementById('navLinks');
const navOverlay = document.getElementById('navOverlay');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
    if (navOverlay) navOverlay.classList.toggle('active');
    document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
  });
}

if (navOverlay) {
  navOverlay.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navLinks.classList.remove('active');
    navOverlay.classList.remove('active');
    document.body.style.overflow = '';
  });
}

document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth <= 768) {
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
      if (navOverlay) navOverlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
});

// ===== NAVBAR SCROLL EFFECT =====
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  });
}

// ===== SCROLL-TRIGGERED ANIMATIONS =====
const animatedElements = document.querySelectorAll('.fade-up, .slide-left, .slide-right, .scale-in');
const animationObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      animationObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });
animatedElements.forEach(el => animationObserver.observe(el));

// ===== COUNTER ANIMATION =====
function animateCounters() {
  document.querySelectorAll('.stat-number[data-target]').forEach(counter => {
    const target = parseInt(counter.getAttribute('data-target'));
    const suffix = counter.getAttribute('data-suffix') || '';
    const duration = 2000;
    const startTime = performance.now();

    function updateCounter(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);
      counter.textContent = current.toLocaleString() + suffix;
      if (progress < 1) requestAnimationFrame(updateCounter);
    }
    requestAnimationFrame(updateCounter);
  });
}

const statsSection = document.querySelector('.stats-section');
if (statsSection) {
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounters();
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  statsObserver.observe(statsSection);
}

// ===== TYPED TEXT EFFECT =====
function typedEffect(elementId, words, typeSpeed = 100, eraseSpeed = 60, pauseTime = 2000) {
  const el = document.getElementById(elementId);
  if (!el) return;
  let wordIndex = 0, charIndex = 0, isErasing = false;

  function type() {
    const currentWord = words[wordIndex];
    if (!isErasing) {
      el.textContent = currentWord.substring(0, charIndex + 1);
      charIndex++;
      if (charIndex === currentWord.length) {
        isErasing = true;
        setTimeout(type, pauseTime);
        return;
      }
      setTimeout(type, typeSpeed);
    } else {
      el.textContent = currentWord.substring(0, charIndex - 1);
      charIndex--;
      if (charIndex === 0) {
        isErasing = false;
        wordIndex = (wordIndex + 1) % words.length;
      }
      setTimeout(type, eraseSpeed);
    }
  }
  type();
}

// Initialize typed effect on homepage
if (document.getElementById('typedText')) {
  typedEffect('typedText', ['Smartwatches', 'Fitness Trackers', 'AR Glasses', 'Health Monitors', 'Smart Rings']);
}

// ===== TAB SWITCHING =====
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const tabGroup = btn.closest('.tab-section') || btn.closest('section');
    if (!tabGroup) return;

    tabGroup.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    tabGroup.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');

    const target = btn.getAttribute('data-tab');
    const pane = tabGroup.querySelector(`#${target}`);
    if (pane) pane.classList.add('active');
  });
});

// ===== FAQ ACCORDION =====
document.querySelectorAll('.faq-question').forEach(question => {
  question.addEventListener('click', () => {
    const item = question.parentElement;
    const isActive = item.classList.contains('active');

    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
    if (!isActive) item.classList.add('active');
  });
});

// ===== LOGIN FORM =====
const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const role = document.getElementById('loginRole').value;
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    if (!email || !password || !role) {
      showNotification('Please fill in all fields', 'error');
      return;
    }

    localStorage.setItem('userRole', role);
    localStorage.setItem('userEmail', email);
    localStorage.setItem('isLoggedIn', 'true');

    showNotification('Login successful! Redirecting...', 'success');

    setTimeout(() => {
      switch (role) {
        case 'admin': window.location.href = 'admin-dashboard.html'; break;
        case 'developer': window.location.href = 'developer-dashboard.html'; break;
        case 'user': window.location.href = 'user-dashboard.html'; break;
        default: window.location.href = 'user-dashboard.html';
      }
    }, 1500);
  });
}

// ===== REGISTER FORM =====
const registerForm = document.getElementById('registerForm');
if (registerForm) {
  registerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('regName').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const confirm = document.getElementById('regConfirm').value;
    const role = document.getElementById('regRole').value;

    if (!name || !email || !password || !confirm || !role) {
      showNotification('Please fill in all fields', 'error');
      return;
    }
    if (password !== confirm) {
      showNotification('Passwords do not match', 'error');
      return;
    }
    if (password.length < 6) {
      showNotification('Password must be at least 6 characters', 'error');
      return;
    }

    localStorage.setItem('userRole', role);
    localStorage.setItem('userEmail', email);
    localStorage.setItem('userName', name);
    localStorage.setItem('isLoggedIn', 'true');

    showNotification('Account created! Redirecting...', 'success');

    setTimeout(() => {
      switch (role) {
        case 'admin': window.location.href = 'admin-dashboard.html'; break;
        case 'developer': window.location.href = 'developer-dashboard.html'; break;
        case 'user': window.location.href = 'user-dashboard.html'; break;
        default: window.location.href = 'user-dashboard.html';
      }
    }, 1500);
  });
}

// ===== NOTIFICATION SYSTEM =====
function showNotification(message, type = 'info') {
  const existing = document.querySelector('.notification');
  if (existing) existing.remove();

  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.innerHTML = `
    <i class="bi bi-${type === 'success' ? 'check-circle' : type === 'error' ? 'x-circle' : 'info-circle'}"></i>
    <span>${message}</span>
  `;

  Object.assign(notification.style, {
    position: 'fixed', top: '20px', right: '20px',
    padding: '1rem 1.5rem',
    background: type === 'success' ? 'rgba(0, 245, 160, 0.15)' : type === 'error' ? 'rgba(255, 51, 102, 0.15)' : 'rgba(0, 180, 216, 0.15)',
    border: `1px solid ${type === 'success' ? '#00F5A0' : type === 'error' ? '#ff3366' : '#00B4D8'}`,
    borderRadius: '12px', color: '#fff',
    fontFamily: "'Outfit', sans-serif", fontSize: '0.95rem',
    display: 'flex', alignItems: 'center', gap: '0.7rem',
    zIndex: '10000', backdropFilter: 'blur(10px)',
    animation: 'slideInRight 0.4s ease',
    boxShadow: `0 4px 20px ${type === 'success' ? 'rgba(0,245,160,0.2)' : type === 'error' ? 'rgba(255,51,102,0.2)' : 'rgba(0,180,216,0.2)'}`
  });

  document.body.appendChild(notification);
  setTimeout(() => {
    notification.style.opacity = '0';
    notification.style.transform = 'translateX(100px)';
    notification.style.transition = 'all 0.4s ease';
    setTimeout(() => notification.remove(), 400);
  }, 3000);
}

// ===== CONTACT FORM =====
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    showNotification('Message sent successfully! We\'ll get back to you soon.', 'success');
    contactForm.reset();
  });
}

// ===== NEWSLETTER FORM =====
document.querySelectorAll('.newsletter-form').forEach(form => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    showNotification('You\'ve been subscribed to our newsletter!', 'success');
    form.reset();
  });
});

// ===== DASHBOARD SIDEBAR TOGGLE =====
const sidebarToggle = document.getElementById('sidebarToggle');
const dashSidebar = document.getElementById('dashSidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');

if (sidebarToggle && dashSidebar) {
  sidebarToggle.addEventListener('click', () => {
    dashSidebar.classList.toggle('active');
    if (sidebarOverlay) sidebarOverlay.classList.toggle('active');
  });
}
if (sidebarOverlay) {
  sidebarOverlay.addEventListener('click', () => {
    dashSidebar.classList.remove('active');
    sidebarOverlay.classList.remove('active');
  });
}

// ===== DASHBOARD LOGOUT =====
document.querySelectorAll('.logout-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('userRole');
    localStorage.removeItem('userEmail');
    localStorage.removeItem('userName');
    showNotification('Logged out successfully', 'success');
    setTimeout(() => { window.location.href = 'login.html'; }, 1000);
  });
});

// ===== PASSWORD TOGGLE =====
document.querySelectorAll('.toggle-password').forEach(toggle => {
  toggle.addEventListener('click', () => {
    const input = toggle.previousElementSibling;
    if (input && input.type === 'password') {
      input.type = 'text';
      toggle.classList.replace('bi-eye', 'bi-eye-slash');
    } else if (input) {
      input.type = 'password';
      toggle.classList.replace('bi-eye-slash', 'bi-eye');
    }
  });
});
