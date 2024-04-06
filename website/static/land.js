// Function to handle click event on anchor element
function handleClick(event) {
    // Prevent the default behavior of the anchor element
    event.preventDefault();
  
    // Define the URL of the webpage to navigate to
    var newPageUrl = window.location.href;
  
    // Navigate to the new webpage
    window.location.href = "/login";
  }
  
  // Add a click event listener to the anchor element
  var anchorElement = document.getElementById('start');
  anchorElement.addEventListener('click', handleClick);