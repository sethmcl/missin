function validateForm() {
    var x=document.forms["test"]["email"].value;
    var b=x.indexOf("@");
    var c=x.indexOf(".");
    if (b<1 || c<1) {
      x=document.getElementById("error");  // Find the element
      x.innerHTML="Invalid email";    // Change the content
      return false;
    }
  }
