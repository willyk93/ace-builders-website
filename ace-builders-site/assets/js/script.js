/* Ace Builders of Canada Ltd. — shared site script */
document.addEventListener('DOMContentLoaded', function () {

  // --- Mobile nav toggle ---
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  // --- Sticky header shadow on scroll ---
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 8) {
        header.style.boxShadow = '0 4px 18px rgba(11,58,39,0.10)';
      } else {
        header.style.boxShadow = 'none';
      }
    });
  }

  // --- Contact form (static site placeholder handling) ---
  var form = document.getElementById('contactForm');
  var status = document.getElementById('form-status');
  if (form && status) {
    form.addEventListener('submit', function (e) {
      // NOTE: This form is pre-wired for Netlify Forms (data-netlify="true").
      // If you're hosting elsewhere (GitHub Pages, custom server, etc.),
      // connect a service like Formspree or EmailJS and remove this
      // preventDefault so the form posts to that endpoint instead.
      var isNetlify = window.location.hostname.indexOf('netlify') !== -1 ||
                       document.querySelector('meta[name="netlify"]');
      if (!isNetlify) {
        e.preventDefault();
        status.textContent = 'Thanks! Your message has been noted. Please also call 780-667-8436 or email info@acebuilderscan.com — this demo form isn\'t connected to an inbox yet.';
        status.className = 'show success';
        form.reset();
      }
    });
  }

});
