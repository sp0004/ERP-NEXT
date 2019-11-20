function openPage(pageName, elmnt) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  //document.getElementById(pageName).style.display = "block";
  if (pageName == 'Dash')
  {
    var ajaxDiv = "Dash";
    $.ajax({
    url:"http://localhost:8000/Home/",
    datatype:"html",
    type: "POST",
    success: function(data) {
        ajaxDiv.replaceWith(ajaxDiv.html(data));
    }})
  }
  else if(pageName == 'ToDo')
  {
  var ajaxDiv = "ToDo";
      $.ajax({
    url:"http://localhost:8000/ToDo/",
    datatype:"html",
    type: "POST",
    success: function(data) {
        ajaxDiv.replaceWith(ajaxDiv.html(data));
    }})
  }

 }

// Get the element with id="defaultOpen" and click on it
//xdocument.getElementById("defaultOpen").click();


