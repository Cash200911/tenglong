document.getElementById('actionBtn')?.addEventListener('click', () => {
  alert('欢迎加入腾龙娱乐，带来无限精彩体验！');
});

window.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  header.style.opacity = 0;
  header.style.transition = 'opacity 1s';
  setTimeout(() => { header.style.opacity = 1; }, 100);
});
