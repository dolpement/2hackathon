<script>
  let applications = [
    { name: "Человек Человеков", date: "2024-01-15", details: "Особенности: рост, глаза, волосы, во что одет и тд" }
  ];

  let publications = [
    { title: "Публикация 1" },
    { title: "Публикация 2" },
    { title: "Публикация 3" }
  ];

  function showTips() {
    alert("Новичок\nВетеран полей\nОпора отряда\nЛегенда поисков\nСтраж ночи\nНаставник");
  }

  function startCourses() { 
    alert("Новички\nПервая помощь\nЛес\nГород\nБПЛА");
  }

  function writeArticle() {
    alert("Написание статьи");
  }

  // Функция для новой кнопки
  function createApplication() {
    alert("Создание новой заявки");
  }
</script>

<br>

<div class="container">
  <!-- Основной контент по центру -->
  <div class="main-content">
    <!-- Карта с поисками -->
    <div class="map-block">
      <h3>Карта волонтёров</h3>
      <img src="https://tile.openstreetmap.org/10/560/380.png" alt="Карта" />
      <div class="searches-list">
        {#each applications as application}
          <div class="application-card">
            <h4>{application.name}</h4>
            {#if application.date}
              <p>Дата пропажи: {application.date}</p>
            {/if}
            <p>{application.details}</p>
            {#if application.location}
              <p class="location">📍 {application.location}</p>
            {/if}
          </div>
        {/each}
      </div>
    </div>

    <!-- Работа с платформой -->
    <div class="work-platform">
      <h3>Работа с платформой</h3>
      <div class="work-buttons">
        <button on:click={showTips}>Добавить ачивки</button>
        <button on:click={startCourses}>Добавить курсы</button>
        <button on:click={writeArticle}>Написать статью</button>
      </div>
    </div>

    <!-- Заявки на вакансии -->
    <div class="applications">
      <div class="applications-header">
        <h3>Заявки на поиск</h3>
        <button class="create-application-btn" on:click={createApplication}>
          Создать заявку
        </button>
      </div>
      <div id="applicationsList">
        {#each applications as application, i}
          <div class="application-card">
            <strong>{application.name}</strong>
            {#if application.date}
              <p>Дата: {application.date}</p>
            {/if}
          </div>
        {/each}
      </div>
    </div>

    <!-- Публикации -->
    <div class="publications">
      <h3>Публикации</h3>
      <div id="publicationsGrid" class="publications-grid">
        {#each publications as publication}
          <div class="publication" on:click={() => alert(`Открыть ${publication.title}. Эта публикация про поиски в лесу`)}>
            {publication.title}
          </div>
        {/each}
      </div>
    </div>
  </div>
</div>
<br>

<style>
  body {
    font-family: "Inter", sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 20px;
    color: #111;
    display: flex;
    justify-content: center;
    min-height: 100vh;
  }

  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    max-width: 1000px; /* Увеличено с 800px до 1000px */
    width: 100%;
    margin: 0 auto;
  }

  /* Основной контент */
  .main-content {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    align-items: center;
  }

  /* Общие стили для блоков */
  .map-block,
  .work-platform,
  .applications,
  .publications {
    background: white;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    width: 100%;
    box-sizing: border-box;
  }

  .map-block {
    display: flex;
    flex-direction: column;
  }

  .map-block img {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 15px;
  }

  .searches-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .application-card {
    background: #f8f8f8;
    border-radius: 10px;
    padding: 15px;
    border-left: 4px solid #ff8800;
  }

  .application-card h4 {
    margin: 0 0 8px 0;
    color: #333;
    font-size: 16px;
  }

  .application-card p {
    margin: 4px 0;
    font-size: 14px;
    color: #666;
  }

  .location {
    color: #ff8800;
    font-weight: bold;
  }

  .work-platform {
    background: #ff8800;
    color: white;
    text-align: center;
  }

  .work-buttons {
    display: flex;
    gap: 12px;
    margin-top: 15px;
    justify-content: center;
  }

  .work-buttons button {
    flex: 1;
    background: white;
    color: #111;
    border: none;
    border-radius: 10px;
    padding: 15px;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.2s;
    max-width: 220px; /* Немного увеличена максимальная ширина кнопок */
  }

  .work-buttons button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }

  /* Стили для блока "Заявки на вакансии" */
  .applications-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }

  .applications-header h3 {
    margin: 0;
    color: #333;
    font-size: 18px;
  }

  .create-application-btn {
    background: #ff8800;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 500;
    font-size: 14px;
    transition: all 0.2s ease;
    white-space: nowrap;
  }

  .create-application-btn:hover {
    background: #e57a00;
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(255, 136, 0, 0.3);
  }

  .create-application-btn:active {
    transform: translateY(0);
  }

  .publications-grid {
    display: flex;
    gap: 12px;
    margin-top: 15px;
    justify-content: center;
  }

  .publication {
    flex: 1;
    background: #001aff;
    color: white;
    border-radius: 10px;
    padding: 25px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    max-width: 220px; /* Немного увеличена максимальная ширина публикаций */
    font-weight: 500;
  }

  .publication:hover {
    transform: translateY(-2px);
    background: #0011cc;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }

  /* Адаптивность */
  @media (max-width: 1100px) {
    .container {
      max-width: 900px; /* На средних экранах тоже увеличиваем */
    }
  }

  @media (max-width: 768px) {
    .container {
      padding: 10px;
      gap: 15px;
      max-width: 100%; /* На мобильных используем всю ширину */
    }
    
    .work-buttons {
      flex-direction: column;
      align-items: center;
    }
    
    .work-buttons button {
      max-width: 100%;
      width: 100%;
    }
    
    .publications-grid {
      flex-direction: column;
      align-items: center;
    }
    
    .publication {
      max-width: 100%;
      width: 100%;
    }
    
    .map-block,
    .work-platform,
    .applications,
    .publications {
      padding: 20px;
    }

    .applications-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }

    .create-application-btn {
      align-self: flex-end;
    }
  }

  @media (max-width: 480px) {
    .map-block,
    .work-platform,
    .applications,
    .publications {
      padding: 15px;
      border-radius: 15px;
    }
    
    .work-buttons button,
    .publication {
      padding: 12px;
    }

    .applications-header {
      flex-direction: column;
      align-items: stretch;
    }

    .create-application-btn {
      align-self: stretch;
      text-align: center;
    }
  }
</style>