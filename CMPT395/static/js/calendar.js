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

function toggle_signup(day, date, start, end) {
  // Populate form fields
  var signup_date = document.getElementById("js-signup-date");
  var signup_day = document.getElementById("js-signup-day");
  signup_date.innerHTML = date;
  signup_day.innerHTML = day;
  
  var signup_class = document.getElementById("id_classroom");
  var signup_start = document.getElementById("id_startTime");
  var signup_end = document.getElementById("id_endTime");
  
  signup_start.value = start;
  signup_end.value = end;
  
  var hidden_date = document.getElementById("js-signup-hidden-date");
  hidden_date.value = signup_date.innerHTML;
  // Toggle visibility
  toggle_popup("sign-up-overlay");
}
