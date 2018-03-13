
/*
window.onload = function() {
    var all_divs = document.getElementsByClassName("time-slot-add");
    for (var i = 0; i < all_divs.length; i++) {
        var currentDiv = all_divs[i];
        currentDiv.onclick = function() { toggle_popup('sign-up-overlay'); }
    }
}
*/

function toggle_popup(elemId) {
    /*
      Toggles visibility of an html element
      Pre: An html element with a uniquely assigned id
      Post: html elements visibility will be toggled
      Param: elemId: String containing ID of element to be toggled
      Return: None
      Side Effects: Element identified by elemId will have its
        visibility toggled
    */
    elem = document.getElementById(elemId);
    if (elem.style.visibility == "visible") {
        elem.style.visibility = "hidden";
    }
    else {
        elem.style.visibility = "visible";
    }
}

function toggle_signup(day, date, times) {
  // Populate form fields
  var signup_date = document.getElementById("js-signup-date");
  var signup_day = document.getElementById("js-signup-day");
  signup_date.innerHTML = date;
  signup_day.innerHTML = day;
  
  var signup_class = document.getElementById("id_classroom");
  var signup_start = document.getElementById("id_startTime");
  var signup_end = document.getElementById("id_endTime");
  
  signup_start.value = times;
  signup_end.value = times;
  
/*  var signup_start = document.getElementById("signup_start");
  var signup_end = document.getElementById("signup_end");
  signup_start.value = times;
  signup_end.value = times;*/
  
  
  // Toggle visibility
  toggle_popup("sign-up-overlay");
}
