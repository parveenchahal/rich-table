function init() {

  var arr = [
    {
      "name": "Build Your Own Pizza with Three Toppings",
      "desc": "Get a pizza of your own choice. Choose any 3 toppings and get ... more",
      "price" : "₹125"
    },
    {
      "name": "Build Your Own Pizza with Four Toppings",
      "desc": "Get a pizza of your own choice. Choose any 4 toppings and get ... more",
      "price" : "₹150"
    },
    {
      "name": "Onion Pizza[7 Inches]+Corn Pizza[7 Inches]",
      "desc": "Lots of Cheese, onion & corn",
      "price" : "₹120"
    },
    {
      "name": "Red Sauce Pasta",
      "desc": "Pasta slow cooked in tangy tomato sauce",
      "price" : "₹160"
    },
    {
      "name": "Corn and Mushroom Pizza[7 Inches]+Simple Macaroni",
      "desc": "Corn and Mushroom Pizza served with typical macroni.",
      "price" : "₹180"
    },
    {
      "name": "Tomato Pizza",
      "desc": "Lots of cheese, tomato.",
      "price" : "₹65"
    }
  ]

  var out = "";

  var j= 1;
  for (i = 0; i < arr.length/2; i++) {
    out +=  '<div class="pricing-entry">' +
    '<div class="d-flex">' +
    '<div class="img" style="background-image: url(images/pizza-' + j + '.jpg);"></div>' +
    '<div class="desc pl-3">' +
      '<div class="d-flex text align-items-center">' +
        '<h3><span>' + arr[i].name + '</span></h3>' +
        '<span class="price">'+ arr[i].price + '</span>' +
      '</div>' +
      '<div class="d-block">' +
        '<p>' + arr[i].desc + '</p>' +
     '</div></div></div>' ;
    
    j++;
  }
  document.getElementById("recommended1").innerHTML = out;

  var out1 = "";

  var j= 1;
  for (; i < arr.length; i++) {
    out1 +=  '<div class="pricing-entry">' +
    '<div class="d-flex">' +
    '<div class="img" style="background-image: url(images/pizza-' + j + '.jpg);"></div>' +
    '<div class="desc pl-3">' +
      '<div class="d-flex text align-items-center">' +
        '<h3><span>' + arr[i].name + '</span></h3>' +
        '<span class="price">'+ arr[i].price + '</span>' +
      '</div>' +
      '<div class="d-block">' +
        '<p>' + arr[i].desc + '</p>' +
     '</div></div></div>' ;
    
    j++;
  }
  document.getElementById("recommended2").innerHTML = out1;

  
}
//document.addEventListener("DOMContentLoaded", ready, init);
document.getElementById("recommended").onload = init();