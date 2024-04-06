  // Use jQuery to wait for the document to be ready
  $(document).ready(function(){
    // Show the alert
    $("#myAlert").fadeIn();
    
    // Set a timeout to remove the alert after 5 seconds
    setTimeout(function(){
        $("#myAlert").fadeOut(function(){
            // Remove the alert from the DOM
            $(this).remove();
        });
    }, 2000); // 2000 milliseconds = 2 seconds
});