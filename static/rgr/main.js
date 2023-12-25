window.onload = function () {
    var initiative=document.getElementsByClassName('initiative');
    var btn=document.getElementById('loadMore');
    for (let i=20;i<initiative.length;i++) {
        initiative[i].style.display = "none";
    }

    var countD = 20;
    btn.addEventListener("click", function() {
        var initiative=document.getElementsByClassName('initiative');
        countD += 10;
        if (countD <= initiative.length){
            for(let i=0;i<countD;i++){
                initiative[i].style.display = "block";
            }
        }

    })
}

document.addEventListener('DOMContentLoaded', function () {
    // Обработка нажатия кнопки удаления
    var deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var articleId = this.getAttribute('data-article-id');
            deleteArticle(articleId);
        });
    });

    // Функция для отправки запроса на удаление статьи
    function deleteArticle(articleId) {
        if (confirm('Вы уверены, что хотите удалить инициативу?')) {
            fetch('/delete_article/' + articleId, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(function (response) {
                if (response.ok) {
                    // Обновление страницы после успешного удаления
                    window.location.reload();
                } else {
                    console.error('Error deleting article');
                }
            })
            .catch(function (error) {
                console.error('Error deleting article:', error);
            });
        }
    }
});


