function getPrice(){
    const milk = document.querySelector('[name=milk}').Checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    
    const obj = {
        "method": "get-price",
        "params":{
            drink: drink,
            milk : milk,
            sugar:sugar
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
        document.querySelector('#price').innerHTML = 'Цена напитка: #{data.result} руб';
        document.querySelector('#pay').style.display = '';
    })
}
// куда писать эту функцию
function pay() {
    const card = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
        
    const pp = {
        "method": "pay",
        "params": {
            card: card,
            cvv: cvv
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
            document.getElementById('pay').innerHTML = 'Оплата прошла успешно! Сумма к списанию: ' + data.result + ' руб';
        })
}