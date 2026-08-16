(function () {
  var root = document.documentElement;
  var btn = document.getElementById('themeToggleBtn');
  var moonIcon = document.getElementById('themeIconMoon');
  var sunIcon = document.getElementById('themeIconSun');

  function updateIcon(theme) {
    moonIcon.style.display = theme === 'dark' ? 'none' : 'block';
    sunIcon.style.display = theme === 'dark' ? 'block' : 'none';
  }

  updateIcon(root.getAttribute('data-bs-theme'));

  btn.addEventListener('click', function () {
    var current = root.getAttribute('data-bs-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-bs-theme', next);
    localStorage.setItem('theme', next);
    updateIcon(next);
  });
})();