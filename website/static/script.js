document.addEventListener("DOMContentLoaded", function() {
  var elements = document.querySelectorAll('.text-box > .h1');
  var delay = 5000; // Time to display each language message in milliseconds
  var currentIndex = 0;

  function showNextElement() {
      if (currentIndex < elements.length) {
          if (currentIndex > 0) {
              elements[currentIndex - 1].style.opacity = '0'; // Fade out the previous message
          }
          elements[currentIndex].style.opacity = '1'; // Fade in the current message
          setTimeout(function() {
              elements[currentIndex].style.opacity = '0'; // Fade out the current message
              currentIndex++;
              showNextElement();
          }, delay);
      } else {
          currentIndex = 0; // Reset index for next loop
          showNextElement(); // Restart animation loop
      }
  }

  // Start displaying elements after 5 seconds
  setTimeout(showNextElement, 1000);
});
const bigText = document.getElementById('bigText');

bigText.addEventListener('mousemove', (event) => {
  const { clientX, clientY } = event;
  const { offsetWidth, offsetHeight } = bigText;
  const centerX = offsetWidth / 2;
  const centerY = offsetHeight / 2;
  const deltaX = clientX - (bigText.offsetLeft + centerX);
  const deltaY = clientY - (bigText.offsetTop + centerY);
  const distance = Math.sqrt(deltaX ** 2 + deltaY ** 2);

  const maxRadius = Math.max(centerX, centerY);
  const normalizedDistance = Math.min(distance / maxRadius, 1);

  const circle = document.createElement('div');
  circle.classList.add('circle');
  circle.style.width = circle.style.height = `${maxRadius * 2}px`;
  circle.style.transform = `translate(-50%, -50%) scale(${normalizedDistance})`;

  // Remove any existing circles
  const existingCircle = bigText.querySelector('.circle');
  if (existingCircle) {
    existingCircle.remove();
  }

  bigText.appendChild(circle);
});

bigText.addEventListener('mouseleave', () => {
  const existingCircle = bigText.querySelector('.circle');
  if (existingCircle) {
    existingCircle.remove();
  }
});
