class DraggableLanguageButton {
    constructor() {
        this.button = document.getElementById('languageButton');
        this.dropdown = document.getElementById('languageDropdown');
        this.isDragging = false;
        this.isDropdownOpen = false;
        this.dragOffset = { x: 0, y: 0 };
        this.currentLanguage = 'en';
        
        this.init();
    }
    
    init() {

        if (!this.button || !this.dropdown) return;
            // События для перетаскивания
            const savedLang = this.getLanguageFromCookie();
                if (savedLang) {
                    this.setCurrentLanguage(savedLang);
            }

            this.button.addEventListener('mousedown', this.handleMouseDown.bind(this));
            document.addEventListener('mousemove', this.handleMouseMove.bind(this));
            document.addEventListener('mouseup', this.handleMouseUp.bind(this));
            
            // События для тач-устройств
            this.button.addEventListener('touchstart', this.handleTouchStart.bind(this), { passive: false });
            document.addEventListener('touchmove', this.handleTouchMove.bind(this), { passive: false });
            document.addEventListener('touchend', this.handleTouchEnd.bind(this));
            
            // Клик для открытия/закрытия dropdown (только для мыши)
            this.button.addEventListener('click', this.handleClick.bind(this));
            
            // Для тач-устройств используем отдельную логику
            this.button.addEventListener('touchend', this.handleTouchClick.bind(this));
            
            // Клик вне кнопки для закрытия dropdown
            document.addEventListener('click', this.handleOutsideClick.bind(this));
            document.addEventListener('touchend', this.handleOutsideClick.bind(this));
            
            // Выбор языка
            this.dropdown.addEventListener('click', this.handleLanguageSelect.bind(this));
            this.dropdown.addEventListener('touchend', this.handleLanguageSelect.bind(this));
            
            // Предотвращаем контекстное меню
            this.button.addEventListener('contextmenu', e => e.preventDefault());
        }
    
    getLanguageFromCookie() {
        const match = document.cookie.match(/(?:^|; )lang=([^;]*)/);
        return match ? decodeURIComponent(match[1]) : null;
    }

    handleMouseDown(e) {
        e.preventDefault();
        this.startDrag(e.clientX, e.clientY);
    }
    
    handleTouchStart(e) {
        e.preventDefault();
        const touch = e.touches[0];
        this.startDrag(touch.clientX, touch.clientY);
    }
    
    startDrag(clientX, clientY) {
        this.isDragging = true;
        this.hasMoved = false; // Флаг для отслеживания движения
        this.button.classList.add('dragging');
        document.body.classList.add('no-select');
        
        const rect = this.button.getBoundingClientRect();
        this.dragOffset.x = clientX - rect.left;
        this.dragOffset.y = clientY - rect.top;
        this.startPosition = { x: clientX, y: clientY }; // Запоминаем начальную позицию
        
        // Закрываем dropdown если он открыт
        if (this.isDropdownOpen) {
            this.closeDropdown();
        }
    }
    
    handleMouseMove(e) {
        if (!this.isDragging) return;
        this.updatePosition(e.clientX, e.clientY);
    }
    
    handleTouchMove(e) {
        if (!this.isDragging) return;
        e.preventDefault();
        const touch = e.touches[0];
        this.updatePosition(touch.clientX, touch.clientY);
    }
    
    updatePosition(clientX, clientY) {
        // Проверяем, было ли значительное движение
        const moveThreshold = 10; // пикселей
        const deltaX = Math.abs(clientX - this.startPosition.x);
        const deltaY = Math.abs(clientY - this.startPosition.y);
        
        if (deltaX > moveThreshold || deltaY > moveThreshold) {
            this.hasMoved = true;
        }
        
        const newX = clientX - this.dragOffset.x;
        const newY = clientY - this.dragOffset.y;
        
        // Ограничиваем позицию в пределах viewport
        const maxX = window.innerWidth - this.button.offsetWidth;
        const maxY = window.innerHeight - this.button.offsetHeight;
        
        const boundedX = Math.max(0, Math.min(newX, maxX));
        const boundedY = Math.max(0, Math.min(newY, maxY));
        
        this.button.style.left = boundedX + 'px';
        this.button.style.top = boundedY + 'px';
        this.button.style.right = 'auto';
        this.button.style.transform = 'none';
    }
    
    handleMouseUp() {
        this.endDrag();
    }
    
    handleTouchEnd() {
        this.endDrag();
    }
    
    endDrag() {
        if (!this.isDragging) return;
        
        this.isDragging = false;
        this.button.classList.remove('dragging');
        document.body.classList.remove('no-select');
    }
    
    handleClick(e) {
        // Только для мыши - если мы не перетаскивали, то это клик для открытия dropdown
        if (!this.isDragging) {
            e.stopPropagation();
            this.toggleDropdown();
        }
    }
    
    handleTouchClick(e) {
        // Для тач-устройств - открываем dropdown только если не было перетаскивания
        if (this.isDragging && !this.hasMoved) {
            e.preventDefault();
            e.stopPropagation();
            setTimeout(() => {
                this.toggleDropdown();
            }, 50); // Небольшая задержка для корректной обработки
        }
    }
    
    toggleDropdown() {
        if (this.isDropdownOpen) {
            this.closeDropdown();
        } else {
            this.openDropdown();
        }
    }
    
    openDropdown() {
        this.dropdown.classList.add('show');
        this.isDropdownOpen = true;
    }
    
    closeDropdown() {
        this.dropdown.classList.remove('show');
        this.isDropdownOpen = false;
    }
    
    handleOutsideClick(e) {
        if (!this.button.contains(e.target)) {
            this.closeDropdown();
        }
    }
    
    handleLanguageSelect(e) {
        const languageItem = e.target.closest('.language-item');
        if (!languageItem) return;

        const selectedLang = languageItem.dataset.lang;
        this.setCurrentLanguage(selectedLang);
        this.closeDropdown();

        // === ⬇️ Новый код: запрос на сервер вместо установки куки
        fetch(`/api/locale/${selectedLang}`, {
            method: 'POST',
            credentials: 'same-origin'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Не удалось сменить язык на сервере');
            }
            return response.json(); // ✅ дожидаемся распаковки JSON
        })
        .then(data => {
            console.log("Language set response:", data);
            window.location.reload(); // ✅ всё хорошо — перезагрузка
        })
        .catch(error => {
            console.error('Ошибка при запросе смены языка:', error);
        });


        // === ⬇️ Удалено: установка куки из JS
        // this.setLanguageCookie(selectedLang);
        // window.location.reload();
    }

    // === ⬇️ Удалённый метод (теперь не нужен)
    /*
    setLanguageCookie(lang) {
        const expires = new Date();
        expires.setFullYear(expires.getFullYear() + 1);
        document.cookie = `lang=${lang}; expires=${expires.toUTCString()}; path=/; SameSite=Lax`;
        console.log('Язык изменен на:', lang);
    }
    */
    
    setCurrentLanguage(lang) {
        // Убираем активный класс со всех элементов
        this.dropdown.querySelectorAll('.language-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // Добавляем активный класс к выбранному
        const selectedItem = this.dropdown.querySelector(`[data-lang="${lang}"]`);
        if (selectedItem) {
            selectedItem.classList.add('active');
            this.currentLanguage = lang;
        }
    }
}

// Инициализируем кнопку после загрузки страницы
document.addEventListener('DOMContentLoaded', () => {
    new DraggableLanguageButton();
});