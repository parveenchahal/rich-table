function init2() {

  var arr = [
    {
      "name": "Multi Veggie Pizza",
      "desc": "Lots of cheese, tomato, onion, capsicum.",
      "price" : "₹105"
    },
    {
      "name": "Paneer and Veggie Pizza",
      "desc": "Lots of cheese, tomato, onion, capsicum, paneer.",
      "price" : "₹125"
    },
    {
      "name": "Multi Veggie Pizza",
      "desc": "index.html",
      "price" : "₹105"
    },
    {
      "name": "Multi Veggie Pizza",
      "desc": "index.html",
      "price" : "₹105"
    },
    {
      "name": "Multi Veggie Pizza",
      "desc": "index.html",
      "price" : "₹105"
    }
  ]

  var out = "";

  var i;
  for (i = 0; i < arr.length; i++) {
    out += '<div class="col-lg-4 d-flex ftco-animate"><p>' + arr[i].name; + '</p></div>'
  }
  document.getElementById("bestseller-menu").innerHTML = out;

}
window.onload = init2;