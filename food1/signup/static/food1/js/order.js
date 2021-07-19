var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

// add pizza

function addPizza(pid){
    //get pizza name
    pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;
    //get pizza price
    var radio = 'pizza' + pid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if(pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    }
    else {
        price = pri[1].value;
        size = 'L';
    }

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    //saving item and total in localstorage
    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders',JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total',total);

    //updating number of items in shopping cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    butto = '<div class="del" onclick="removePizza(' + cartSize + ')">x</div>';
    ptotal.innerHTML = 'Total: ' + 'Rp. ' + total;
    pcart.innerHTML += '<li>'+ name + ' ' + size + ': ' + 'Rp. ' + price + butto + '</li>';
}

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++){
        butto = '<div class="del" onclick="removePizza(' + i + ')">x</div>';
        pcart.innerHTML += '<li>'+ orders[i][0] + ' ' + orders[i][1] + ': ' + 'Rp. ' + orders[i][2] + butto + '</li>';
    }
    ptotal.innerHTML = 'Total: ' + 'Rp. ' + total;
}

pshoppingCart();

function removePizza(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');

    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);

    //updating number of items in shopping cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    localStorage.setItem('orders',JSON.stringify(orders));
    localStorage.setItem('total',total);
    
    pshoppingCart();
}