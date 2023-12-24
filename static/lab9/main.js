function showModal(){
    document.querySelector('div.modal').style.display = 'block';
}
function hideModal(){
    document.querySelector('div.modal').style.display = 'none';
}
function cancel (){
    hideModal();
}
function addCourse(){
    document.getElementById('card').value = '';
    document.getElementById('recipient_name').value = '';
    document.getElementById('sender_name').value = '';
    showModal();
}