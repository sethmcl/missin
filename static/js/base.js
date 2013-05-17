function validateForm() {
    var x=document.forms["test"]["email"].value;
    var b=x.indexOf("@");
    var c=x.indexOf(".");
    if (b<1 || c<1) {
      alert("That's not even an email!")
      return false;
    }
  }