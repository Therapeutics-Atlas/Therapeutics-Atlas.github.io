/* Therapeutics Atlas — shared UI behaviour. Currently: a floating "back to top" control that
   appears once the page is scrolled and returns the reader to the top. No dependencies. */
(function () {
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'to-top';
  btn.hidden = true;
  btn.setAttribute('aria-label', 'Back to top');
  btn.title = 'Back to top';
  btn.innerHTML = '<span class="tt-arrow" aria-hidden="true"></span>';
  btn.addEventListener('click', function () {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  });
  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    btn.hidden = y < 400;
  }
  function mount() {
    if (!document.body) return;
    document.body.appendChild(btn);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount);
  else mount();
})();
