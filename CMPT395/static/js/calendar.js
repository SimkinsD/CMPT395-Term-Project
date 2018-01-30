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

function struct_sign_up(time_start, time_end, day, date) {
    this.time_start = time_start;
    this.time_end = time_end;
    this.day = day;
    this.date = date;
}

function populate_signup_form(elem, sign_up_info, date) {
    var day_date = document.createElement("P").appendChild
      (document.createTextNode(day + date));
    var info = document.createElement("P").appendChild
      (document.createTextNode(sign_up_info));

    elem.appendChild(day_date);
    elem.appendChild(info);
    
}

function apply_popup_links() {
    var all_divs = document.getElementsByTagName("div");
    for (var i = 0; i < all_divs.length; i++) {
        var currentDiv = all_divs[i];
        if (currentDiv.className == "time-slot-add") {
            currentDiv.onclick = function() { toggle_popup('sign-up-overlay'); }
        }
    }
}