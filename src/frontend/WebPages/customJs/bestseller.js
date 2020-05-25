function init() {

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
      "name": "Onion Pizza[7 Inches]+Corn Pizza[7 Inches]",
      "desc": "Lots of Cheese, onion & corn",
      "price" : "₹120"
    },
    {
      "name": "Corn Pizza",
      "desc": "Lots of cheese, corn.",
      "price" : "₹65"
    },
    {
      "name": "Capsicum Pizza",
      "desc": "Lots of cheese, capsicum.",
      "price" : "₹65"
    },
    {
      "name": "Onion Pizza",
      "desc": "Lots of cheese, Onion",
      "price" : "₹65"
    },
    {
      "name": "Italian Veggie Sandwich + French Fries + Coke [300 ml]",
      "desc": "Combo",
      "price" : "₹185"
    },
    {
      "name": "Queen Margarita Pizza",
      "desc": "Fully cheesy.",
      "price" : "₹85"
    },
    {
      "name": "Chilli Paneer and Veggie Pizza",
      "desc": "Lots of cheese, tomato, onion, capsicum, paneer, green chilli.",
      "price" : "₹135"
    },
    {
      "name": "Veg Sandwich",
      "desc": "Tomato, cucumber, cabbage, carrot.",
      "price" : "₹85"
    }
  ]

  var out = "";

  var j= 1;
  for (i = 0; i < arr.length; i++) {
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
  document.getElementById("bestseller-menu").innerHTML = out;
  

}

document.getElementById("bestseller-menu").onload = init();