<script>
  function toggleCheck(event) {
    const button = event.currentTarget;
    const isChecked = button.classList.contains('checked');
    
    if (isChecked) {
      // Убираем галочку - возвращаем серый кружочек
      button.classList.remove('checked');
      button.innerHTML = '';
      button.style.background = '#e0e0e0';
      button.style.color = 'transparent';
    } else {
      // Добавляем галочку - зеленая кнопка с белой галочкой
      button.classList.add('checked');
      button.innerHTML = '✓';
      button.style.background = '#28a745';
      button.style.color = 'white';
    }
  }
</script>

<div class="page-wrapper">
  <div class="container">
    <!-- Основной контент по центру -->
    <div class="main-content">
      <!-- Белые прямоугольники в столбец -->
      <div class="white-rectangle">
        <div class="rectangle-text">Волонтёров Волонтёр Волонтёрович</div>
      </div>
      
      <div class="white-rectangle">
        <div class="rectangle-text">Квалификация</div>
      </div>
      
      <div class="white-rectangle">
        <div class="rectangle-text">Курсы</div>
      </div>
      
      <div class="white-rectangle">
        <div class="time-search">
          <div class="search-item">
            <button class="check-btn" on:click={toggleCheck}></button>
            <span>Дневные поиски</span>
          </div>
          <div class="search-item">
            <button class="check-btn" on:click={toggleCheck}></button>
            <span>Ночные поиски</span>
          </div>
        </div>
      </div>
      
      <div class="white-rectangle">
        <div class="people-search">
          <div class="search-item">
            <button class="check-btn" on:click={toggleCheck}></button>
            <span>Поиск детей</span>
          </div>
          <div class="search-item">
            <button class="check-btn" on:click={toggleCheck}></button>
            <span>Поиск пожилых людей</span>
          </div>
          <div class="search-item">
            <button class="check-btn" on:click={toggleCheck}></button>
            <span>Поиск молодых людей</span>
          </div>
        </div>
      </div>
      
      <div class="white-rectangle">
        <div class="rectangle-text">Оборудование</div>
      </div>
      
      <div class="white-rectangle">
        <div class="rectangle-text">Контакт связи: @volunteer</div>
      </div>
    </div>
  </div>
</div>

<style>
  body {
    font-family: "Inter", sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
    color: #111;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }

  .page-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px 0;
    box-sizing: border-box;
  }

  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    flex: 1;
  }

  /* Основной контент */
  .main-content {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    align-items: center;
    justify-content: center;
    flex: 1;
  }

  /* Белые прямоугольники */
  .white-rectangle {
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    width: 100%;
    height: 120px;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
  }

  .white-rectangle:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  }

  /* Стили для обычного текста */
  .rectangle-text {
    font-size: 18px;
    font-weight: 500;
    color: #333;
    text-align: left;
    width: 100%;
  }

  /* Стили для блоков с кнопками-галками */
  .time-search,
  .people-search {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 100%;
  }

  .search-item {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .check-btn {
    background: #e0e0e0;
    color: transparent;
    border: none;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    transition: all 0.2s ease;
    flex-shrink: 0;
  }

  .check-btn:hover {
    background: #d0d0d0;
    transform: scale(1.1);
  }

  .check-btn:active {
    transform: scale(0.95);
  }

  .check-btn.checked {
    background: #28a745 !important;
    color: white !important;
  }

  .check-btn.checked:hover {
    background: #218838 !important;
  }

  .search-item span {
    font-size: 16px;
    color: #333;
    font-weight: 500;
  }

  /* Адаптивность */
  @media (max-width: 768px) {
    .page-wrapper {
      padding: 15px 0;
    }
    
    .container {
      gap: 15px;
    }
    
    .white-rectangle {
      height: auto;
      min-height: 100px;
      padding: 15px;
      border-radius: 12px;
    }
    
    .rectangle-text {
      font-size: 16px;
    }
    
    .search-item span {
      font-size: 14px;
    }
    
    .check-btn {
      width: 22px;
      height: 22px;
      font-size: 12px;
    }
    
    .time-search,
    .people-search {
      gap: 10px;
    }
  }

  @media (max-width: 480px) {
    .page-wrapper {
      padding: 10px 0;
    }
    
    .container {
      gap: 12px;
    }
    
    .white-rectangle {
      min-height: 80px;
      padding: 12px;
      border-radius: 10px;
    }
    
    .rectangle-text {
      font-size: 14px;
    }
    
    .search-item {
      gap: 8px;
    }
    
    .search-item span {
      font-size: 13px;
    }
    
    .check-btn {
      width: 20px;
      height: 20px;
    }
  }
</style>