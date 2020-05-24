function init() {

  var arr = [
    {
      "display": "Combos",
      "list" : [
        {"name" : "Super Duper Combo",
         "desc" : "Veggie House Pizza[9 Inches]+Maharaja Burger+Paneer Sandwich+Veg Garlic Bread+Coke[300 ml]",
         "price" : "₹665"
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        }
     ]
    },
    {
      "display": "Build Your Own Pizza",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
      ]
    },
    {
      "display": "Pizza and Pasta",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
      ]
    },
    {
      "display": "Burgers and Sandwiches",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
      ]
    },
    {
      "display": "Macaroni",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
      ]
    },
    {
      "display": "Maggie",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
      ]
    },
    {
      "display": "Wraps",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
      ]
    },
    {
      "display": "Snacks",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        }
      ]
    },
    {
      "display": "Beverages",
      "list" : [
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        },
        {"name" : "",
         "desc" : "",
         "price" : ""
        }
      ]
    }
  ]

  var out = "";

  var i;
  var j =1;
  for (i = 0; i < arr.length; i++) {
    out += '<a class="nav-link" id="v-pills-' + j + '-tab" data-toggle="pill" href="#v-pills-' + j + '" role="tab" aria-controls="v-pills-' + j + '" aria-selected="true">' +
       arr[i].display +
      '</a>';
      j++;
  }
  document.getElementById("v-pills-tab").innerHTML = out;

}
document.getElementById("v-pills-tab").onload = init();