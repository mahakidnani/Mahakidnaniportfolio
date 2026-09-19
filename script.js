document.addEventListener('DOMContentLoaded', () => {
  const diveScreen = document.getElementById('dive-screen');
  let isDiving = false;

  if (!diveScreen) return;

  function startDive() {
    if (isDiving) return;
    isDiving = true;
    diveScreen.classList.add('is-diving');
  }

  diveScreen.addEventListener('click', startDive);
  diveScreen.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      startDive();
    }
  });
});
