<script>
  let volunteer = {
    name: "Волонтёров Волонтёр Волонтёрович",
    searches: 29,
    achievements: "3/50",
    experience: "начинающий",
    qualification: "связист, эпизод",
    courses: "первая медицинская помощь",
    types: "Дневные и ночные поиски",
    childrenSearch: "Поиск детей",
    equipment: "машина, экипировка для леса, ломпас",
    about: "учусь в университете МСИСИ, работать, люблю детей",
    contacts: "telegram",
    isMedic: true,
    accountVerified: false
  };

  let applications = [
    { name: "Человек Человеков", date: "2024-01-15", details: "Особенности: рост, глаза, волосы, во что одет и тд" }
  ];

  let publications = [
    { title: "Публикация 1" },
    { title: "Публикация 2" },
    { title: "Публикация 3" }
  ];

  function verifyAccount() {
    volunteer.accountVerified = true;
    // Здесь может быть API запрос для подтверждения
  }

  function showTips() {
    alert("Советы по работе с сервисом");
  }

  function startCourses() {
    alert("Переход к курсам");
  }

  function writeArticle() {
    alert("Написание статьи");
  }
</script>

<div class="container">
  <!-- Левая колонка - профиль -->
  <div class="profile">
    <img id="avatar" src="" alt="Фото" class="avatar" />
    <h2 id="fio">{volunteer.name}</h2>
    <p>Поиски: <b id="searches">{volunteer.searches}</b></p>
    <p>Ачивки: <b id="achievements">{volunteer.achievements}</b></p>

    <div class="achievements">
      <span>🏅</span>
      <span>🌲</span>
      <span>🎒</span>
    </div>

    {#if volunteer.isMedic}
      <p id="medicStatus">✔ Медицинский работник</p>
    {/if}

    <div class="section orange">
      <p><b>Опыт:</b> <span id="experience">{volunteer.experience}</span></p>
      <p><b>Квалификация:</b> <span id="qualification">{volunteer.qualification}</span></p>
      <p><b>Курсы:</b> <span id="courses">{volunteer.courses}</span></p>
      <p><b>Типы поисков:</b> <span id="types">{volunteer.types}</span></p>
      <p id="childrenSearch">{volunteer.childrenSearch}</p>
      <p><b>Оборудование:</b> <span id="equipment">{volunteer.equipment}</span></p>
      <p><b>О себе:</b> <span id="about">{volunteer.about}</span></p>
      <p><b>Контакты:</b> <span id="contacts">{volunteer.contacts}</span></p>
    </div>

    <div class="section white">
      <p>✓ Доступен к поискам</p>
      {#if !volunteer.accountVerified}
        <button id="verify" on:click={verifyAccount}>Подтверди аккаунт</button>
      {:else}
        <p style="color: green;">✓ Аккаунт подтверждён</p>
      {/if}
    </div>
  </div>

  <!-- Правая колонка -->
  <div class="right">
    <!-- Карта с поисками -->
    <div class="map-block">
      <h3>Доступные поиски</h3>
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
        <button on:click={showTips}>Советы по работе с сервисом</button>
        <button on:click={startCourses}>Пройди курсы</button>
        <button on:click={writeArticle}>Напиши статью</button>
      </div>
    </div>

    <!-- Заявки на вакансии -->
    <div class="applications">
      <h3>Заявки на вакансии</h3>
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

<style>
  body {
    font-family: "Inter", sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 20px;
    color: #111;
  }

  .container {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
  }

  /* Левая колонка */
  .profile {
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    height: fit-content;
    position: sticky;
    top: 20px;
    max-height: 230px;

  }

  .avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #e0e0e0;
  }

  .profile h2 {
    font-size: 16px;
    margin: 10px 0 5px;
  }

  .profile p {
    margin: 5px 0;
    font-size: 14px;
  }

  .achievements {
    display: flex;
    gap: 8px;
    margin: 10px 0;
  }

  .achievements span {
    width: 30px;
    height: 30px;
    background: #eef6ff;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
  }

  .section {
    margin-top: 10px;
    padding: 15px;
    border-radius: 10px;
    width: 100%;
  }

  .section.orange {
    background: #ff8800;
    color: black;
  }

  .section.white button {
    background: #ff8800;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    width: 100%;
    margin-top: 10px;
    font-weight: bold;
  }

  .section.white button:hover {
    background: #e57a00;
  }

  /* Правая колонка */
  .right {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .map-block {
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  .map-block img {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 15px;
  }

  .searches-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
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
    border-radius: 20px;
    padding: 20px;
    color: white;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  .work-buttons {
    display: flex;
    gap: 10px;
    margin-top: 15px;
  }

  .work-buttons button {
    flex: 1;
    background: white;
    color: #111;
    border: none;
    border-radius: 10px;
    padding: 12px;
    cursor: pointer;
    font-weight: 500;
    transition: transform 0.2s;
  }

  .work-buttons button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }

  .applications, .publications {
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  .publications-grid {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }

  .publication {
    flex: 1;
    background: #001aff;
    color: white;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: transform 0.2s;
  }

  .publication:hover {
    transform: translateY(-2px);
    background: #0011cc;
  }

  @media (max-width: 900px) {
    .container {
      grid-template-columns: 1fr;
    }
    
    .profile {
      position: static;
    }
    
    .work-buttons {
      flex-direction: column;
    }
    
    .publications-grid {
      flex-direction: column;
    }
  }
</style>