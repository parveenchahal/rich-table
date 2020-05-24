function init() {

  var arr = [
    {
      "display": "Home",
      "url": "index.html"
    },
    {
      "display": "Menu",
      "url": "menu.html"
    },
    {
      "display": "Services",
      "url": "services.html"
    },
    {
      "display": "About",
      "url": "about.html"
    },
    {
      "display": "Visit Us @Google",
      "url": "index.html"
    }
  ]

  var out = "";

  var i;
  for (i = 0; i < arr.length; i++) {
    out += '<li class="nav-item">' +
      '<a href="' + arr[i].url + '" class="nav-link">' +
      arr[i].display + '</a></li>';
  }
  document.getElementById("upper-menu").innerHTML = out;

}
document.getElementById("upper-menu").onload = init();