document.addEventListener("DOMContentLoaded", () => {
    console.log("Скрипт избранного успешно загружен!");

    const buttons = document.querySelectorAll('.project-fav-btn');
    console.log("Найдено сердечек на странице:", buttons.length);

    buttons.forEach(button => {
        button.addEventListener('click', async (e) => {
                e.preventDefault();
                const projectId = button.getAttribute('data-project-id');
                console.log("Клик по проекту с ID:", projectId);

                try {
                    const response = await fetch(`/${projectId}/favorite/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Content-Type': 'application/json',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    });

                    console.log("Статус ответа от сервера:", response.status);

                    if (response.ok) {
                        const data = await response.json();
                        console.log("Сервер ответил:", data);

                        if (data.status === 'added') {
                            button.classList.add('is-active');
                        } else if (data.status === 'removed') {
                            button.classList.remove('is-active');

                            if (document.body.dataset.page === "favorites") {
                                const card = button.closest('.project-card');
                                if (card) card.remove();

                                const remainingCards = document.querySelectorAll('.project-card');
                                if (remainingCards.length === 0) {

                                    window.location.reload();
                                }
                            }
                        } else {
                            console.error('Ошибка сервера! Проверь, правильный ли URL.');
                        }
                    }
                } catch
                    (error) {
                    console.error('Сетевая ошибка fetch:', error);
                }
            }
        )
        ;
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
