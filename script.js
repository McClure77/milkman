/* Fan art lightbox */
(function () {
  var gallery = document.getElementById('gallery');
  var box     = document.getElementById('lightbox');
  if (!gallery || !box) return;

  var img    = document.getElementById('lbImg');
  var close  = document.getElementById('lbClose');
  var prev   = document.getElementById('lbPrev');
  var next   = document.getElementById('lbNext');
  var links  = Array.prototype.slice.call(gallery.querySelectorAll('a'));
  var index  = 0;
  var opener = null;

  function show(i) {
    index = (i + links.length) % links.length;
    var a = links[index];
    img.src = a.getAttribute('href');
    img.alt = a.querySelector('img').alt;
  }

  function open(i, from) {
    opener = from || null;
    show(i);
    box.hidden = false;
    document.body.style.overflow = 'hidden';
    close.focus();
  }

  function shut() {
    box.hidden = true;
    img.src = '';
    document.body.style.overflow = '';
    if (opener) opener.focus();
  }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      open(i, a);
    });
  });

  close.addEventListener('click', shut);
  prev.addEventListener('click', function () { show(index - 1); });
  next.addEventListener('click', function () { show(index + 1); });

  box.addEventListener('click', function (e) {
    if (e.target === box) shut();
  });

  document.addEventListener('keydown', function (e) {
    if (box.hidden) return;
    if (e.key === 'Escape')     shut();
    if (e.key === 'ArrowLeft')  show(index - 1);
    if (e.key === 'ArrowRight') show(index + 1);
  });
})();
