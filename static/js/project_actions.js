document.addEventListener('DOMContentLoaded', () => {

    const participateButton = document.getElementById('participate-btn');
    if (participateButton) {
        participateButton.addEventListener('click', async () => {
            const url = participateButton.dataset.url;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {'X-CSRFToken': csrfToken, 'Content-Type': 'application/json'}
                });

                if (response.ok) {
                    const data = await response.json();
                    if (data.status === 'added') {
                        participateButton.textContent = 'Отказаться от участия';
                    } else if (data.status === 'removed') {
                        participateButton.textContent = 'Участвовать';
                    }
                    window.location.reload();
                } else {
                    alert('Произошла ошибка. Попробуйте снова.');
                }
            } catch (error) {
                console.error('Ошибка сети:', error);
                alert('Ошибка сети. Проверьте подключение.');
            }
        });
    }

    const shareButton = document.querySelector('.black-button-share-button');
    if (shareButton) {
        shareButton.addEventListener('click', () => {
            navigator.clipboard.writeText(window.location.href).then(() => {
                const originalContent = shareButton.innerHTML;
                shareButton.innerHTML = `<span>✔️ Скопировано!</span>`;
                shareButton.disabled = true;

                setTimeout(() => {
                    shareButton.innerHTML = originalContent;
                    shareButton.disabled = false;
                }, 2000);
            }).catch(err => {
                console.error('Не удалось скопировать ссылку: ', err);
                alert('Не удалось скопировать ссылку.');
            });
        });
    }

});
