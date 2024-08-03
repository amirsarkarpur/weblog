// main.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded!');

    // Scroll-to-Top Button
    const scrollTopButton = document.createElement('button');
    scrollTopButton.textContent = 'بالا';
    scrollTopButton.classList.add('scroll-top-button');
    document.body.appendChild(scrollTopButton);

    scrollTopButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollTopButton.classList.add('show');
        } else {
            scrollTopButton.classList.remove('show');
        }
    });

    // Form Validation (example for post_detail.html)
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (event) => {
            const titleInput = form.querySelector('input[name="title"]');
            const contentInput = form.querySelector('textarea[name="content"]');
            if (titleInput && contentInput) {
                if (titleInput.value.trim() === '' || contentInput.value.trim() === '') {
                    alert('لطفاً تمام فیلدها را پر کنید.');
                    event.preventDefault(); // جلوگیری از ارسال فرم
                }
            }
        });
    }
});






