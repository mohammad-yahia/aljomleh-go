var updateBtn = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtn.length; i++) {
  updateBtn[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var image_url = this.dataset.image_url;
    var price = this.dataset.price;
    var action = this.dataset.action;
    var name = this.dataset.name;

    console.log(
      "productId",
      productId,
      "action",
      action,
      "imageURl",
      image_url,
      "price",
      price
    );

    console.log("User", User);
    if (User == "AnonymousUser") {
      addCookieItem(productId, action, image_url, price, name);
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function doSetClickButtonActions() {
  var updateBtn = document.getElementsByClassName("update-cart-button");

  for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener("click", function () {
      var productId = this.dataset.product;
      var image_url = this.dataset.image_url;
      var price = this.dataset.price;
      var action = this.dataset.action;
      var name = this.dataset.name;

      console.log(
        "productId",
        productId,
        "action",
        action,
        "imageURl",
        image_url,
        "price",
        price
      );

      console.log("User", User);
      if (User == "AnonymousUser") {
        addCookieItem(productId, action, image_url, price, name);
      } else {
        updateUserOrder(productId, action);
      }
    });
  }
}

doSetClickButtonActions();
doUpdateItems();
doUpdateCheckoutItems();

function addCookieItem(productId, action, image_url, price, name) {
  console.log("Not logged in... ");
  console.log("User is not authenticated");
  debugger;
  if (action == "addd") {
    if (cart[productId] == undefined) {
      cart[productId] = {
        quantity: 1,
        imageURL: image_url,
        price: price,
        name: name,
      };
    } else {
      cart[productId]["quantity"] += 1;
    }

    //Walid
    let cartAmountElements = document.getElementsByName("cart-amount-holder");

    for (var i = 0; i < cartAmountElements.length; i++) {
      let currentAmount = cartAmountElements[i].textContent;

      let newAmount = Number.parseFloat(
        Number.parseFloat(currentAmount) + Number.parseFloat(price)
      ).toFixed(2);
      cartAmountElements[i].textContent = newAmount;
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      console.log("Item should be deleted");
      delete cart[productId];
    }

    let cartAmountElements = document.getElementsByName("cart-amount-holder");

    for (var i = 0; i < cartAmountElements.length; i++) {
      let currentAmount = cartAmountElements[i].textContent;

      let newAmount = Number.parseFloat(
        Number.parseFloat(currentAmount) - Number.parseFloat(price)
      ).toFixed(2);
      cartAmountElements[i].textContent = newAmount;
    }
  }

  //Quantity Sum
  let cartTotalItemsCountElements = document.getElementsByName(
    "total-items-count"
  );

  for (var i = 0; i < cartTotalItemsCountElements.length; i++) {
    let itemsCount = cartTotalItemsCountElements[i].textContent;
    cartTotalItemsCountElements[i].textContent = Number.parseFloat(itemsCount) + 1;
  }

  console.log("CART:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";

  doUpdateItems();
  doUpdateCheckoutItems();
  //location.reload()
}

function updateUserOrder(productId, action) {
  console.log("User is logged in < sending data");

  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      console.log("data", data);
      // location.reload()  // refrish the page
    });
}

function getProductTotalPrice(quantity, price) {
  if (quantity && price)
    return (quantity * Number.parseFloat(price).toFixed(2)).toFixed(2);
  return 0;
}

function doUpdateItems() {
  let productsContainerElement = document.getElementById(
    "cart-product-container"
  );

  if (!productsContainerElement) return;

  productsContainerElement.innerHTML = "";

  let ItemsList = JSON.parse(getCookie("cart"));

  for (let itemId in ItemsList) {
    let item = ItemsList[itemId];
    let productElement =
      `<div class="cart-product-item">
              <div class="close-item"><i class="fas fa-times"></i></div>
              <div class="row align-items-center">
                  <div class="col-6 p-0">
                      <div class="thumb">
                          <a href="#"><img src="` +
      item.imageURL +
      `" alt="products"></a>
                      </div>
                  </div>
                  <div class="col-6">
                      <div class="product-content">
                          <a href="#" class="product-title">` +
      item.name +
      `</a>
                          <div class="product-cart-info">
                              ` +
      Number.parseFloat(item.price).toFixed(2) +
      "*" +
      item.quantity +
      "=" +
      getProductTotalPrice(item.quantity, item.price) +
      `
                          </div>
                      </div>
                  </div>
              </div>
              <div class="row align-items-center">
                  <div class="col-6">
                      <div class="price-increase-decrese-group d-flex">
                          <span class="decrease-btn">
                              <button type="button"  
                              data-image_url="` +
      item.imageURL +
      `"
                  data-price="` +
      item.price +
      `"
                  data-name="` +
      item.name +
      `" 
      data-product=` +
      itemId +
      ` data-action ="remove" class="btn quantity-left-minus update-cart update-cart-button" data-type="minus"
                              data-field="">-
                          </button>
                          </span>
                          <input type="text" name="quantity" class="form-controls input-number" value="` +
      item.quantity +
      `">
                          <span class="increase">
                              <button type="button" class="btn quantity-right-plus update-cart update-cart-button" data-type="plus"  
                              data-image_url="` +
      item.imageURL +
      `"
                  data-price="` +
      item.price +
      `"
                  data-name="` +
      item.name +
      `" 
                              data-product=` +
      itemId +
      ` data-action ="addd"
                              data-field="">+
                          </button>
                          </span>
                      </div>
                  </div>
                  <div class="col-6">
                      <div class="product-price">
                        <span class="ml-4">=` +
      getProductTotalPrice(item.quantity, item.price) +
      `</span>
                      </div>
                  </div>
              </div>
          </div>`;

    productsContainerElement.innerHTML += productElement;
  }

  doSetClickButtonActions();
}

function doUpdateCheckoutItems() {
  let productsContainerElement = document.getElementById(
    "checkout-cart-product-container"
  );

  if (!productsContainerElement) return;

  productsContainerElement.innerHTML = "";

  let ItemsList = JSON.parse(getCookie("cart"));

  for (let itemId in ItemsList) {
    let item = ItemsList[itemId];
    let productElement =
      `<div class="cart-product-item">
  <div class=" row align-items-center">
      <div class="col-6 p-0">
          <div class="thumb">
              <a onclick="openModal() "><img src="` +
      item.imageURL +
      `" alt="products"></a>
          </div>
      </div>
      <div class="col-6">
          <div class="product-content">
              <a onclick="openModal()" class="product-title">` +
      item.name +
      `</a>
              <div class="product-cart-info">
              ` +
      Number.parseFloat(item.price).toFixed(2) +
      "*" +
      item.quantity +
      "=" +
      getProductTotalPrice(item.quantity, item.price) +
      `
              </div>
          </div>
      </div>
  </div>
  <div class="row align-items-center">
      <div class="col-6">
          <div class="price-increase-decrese-group d-flex">
              <span class="decrease-btn">
                  <button type="button"
                  data-product=` +
      itemId +
      `
                  data-action ="remove" 
                  data-image_url="` +
      item.imageURL +
      `"
                  data-price="` +
      item.price +
      `"
                  data-name="` +
      item.name +
      `" 
                  class="btn quantity-left-minus update-cart update-cart-button" data-type="minus"
                      data-field="">-
                  </button>
              </span>
              <input type="text" name="quantity"  class="form-controls input-number"
                  value="` +
      item.quantity +
      `">
              <span class="increase">
                  <button type="button" class="btn quantity-right-plus update-cart update-cart-button" data-type="plus" 
                  data-image_url="` +
      item.imageURL +
      `"
                  data-price="` +
      item.price +
      `"
                  data-name="` +
      item.name +
      `" 
                  data-product=` +
      itemId +
      ` data-action ="addd"
                      data-field="">+
                  </button>
              </span>
          </div>
      </div>
      <div class="col-6">
          <div class="product-price">
          <span class="ml-4">=` +
      getProductTotalPrice(item.quantity, item.price) +
      `</span>
          </div>
      </div>
  </div>
</div>`;
    productsContainerElement.innerHTML += productElement;
  }

  doSetClickButtonActions();
}
