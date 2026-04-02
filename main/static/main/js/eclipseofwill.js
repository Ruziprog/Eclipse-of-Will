document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelector('footer p');
    if (!footer) return;
    
    function updateFooter() {
        const urlParams = new URLSearchParams(window.location.search);
        const lang = urlParams.get('lang') || 'ja';
        const year = new Date().getFullYear();
        
        if (lang === 'ja') {
            footer.innerHTML = `© ${year} Eclipse of Will. 全著作権所有。`;
        } else {
            footer.innerHTML = `© ${year} Eclipse of Will. All rights reserved.`;
        }
    }
    
    // Обновить при загрузке
    updateFooter();
    
    // Перехватить клики по кнопкам языка
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const lang = this.dataset.lang;
            
            // Обновить URL
            const url = new URL(window.location);
            url.searchParams.set('lang', lang);
            window.history.pushState({}, '', url);
            
            // Обновить футер
            const year = new Date().getFullYear();
            const footer = document.querySelector('footer p');
            if (footer) {
                footer.innerHTML = lang === 'ja' 
                    ? `© ${year} Eclipse of Will. 全著作権所有。`
                    : `© ${year} Eclipse of Will. All rights reserved.`;
            }
            
            // Обновить активные кнопки
            document.querySelectorAll('.lang-btn').forEach(b => {
                b.classList.toggle('active', b.dataset.lang === lang);
            });
        });
    });
});