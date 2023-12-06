function getPrice(){
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    
    const obj = {
        "method": "get-price",
        "params":{
            drink: drink,
            milk : milk,
            sugar: sugar
        }
    };
    
    fetch ('/lab7/api/', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(obj)
    })
        .then(function (resp) {
            return resp.json();
        })
        .then(function (data) {
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб`;
        document.querySelector('#pay').style.display = '';
    })
}
function pay() {
    const card = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const drink = document.querySelector('[name=drink]').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const pp = {
        "method": "pay",
        "params": {
            card: card,
            cvv: cvv,
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };
        
    fetch('/lab7/api/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(pp)
    })
        .then(function (resp) {
            return resp.json();
        })
        .then(function (data) {
            document.getElementById('pay').innerHTML = `Оплата прошла успешно! ${data.result} `;
        })
}

function reset() {
    const card = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const drink = document.querySelector('[name=drink]').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    
    const back = {
        "method": "pay",
        "params": {
            card: card,
            cvv: cvv,
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };
        
    fetch('/lab7/api/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(back)
    })
        .then(function (resp) {
            return resp.json();
        })
        .then(function (data) {
            document.getElementById('pay').innerHTML = `Платеж отменен. Сумма к возврату: ${data.result}`;
        })
}