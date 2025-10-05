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

<div class="page-wrapper">
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
        </div>

        <!-- Правая колонка -->
        <div class="right">
            <!-- Оранжевый блок с информацией -->
            <div class="orange-info-block">
                <h3>Информация о волонтёре</h3>
                <div class="info-content">
                    <p><b>Опыт:</b> <span id="experience">{volunteer.experience}</span></p>
                    <p><b>Квалификация:</b> <span id="qualification">{volunteer.qualification}</span></p>
                    <p><b>Курсы:</b> <span id="courses">{volunteer.courses}</span></p>
                    <p><b>Типы поисков:</b> <span id="types">{volunteer.types}</span></p>
                </div>
            </div>

            <!-- Перенесенные элементы из левого столбца -->
            <div class="additional-info-block">
                {#if volunteer.isMedic}
                    <div class="medic-status">
                        <p>✔ Медицинский работник</p>
                    </div>
                {/if}

                <div class="availability-section">
                    <p>✓ Доступен к поискам</p>
                </div>
            </div>

            <!-- Карта с поисками -->
            <div class="map-block">
                <h3>Доступные поиски</h3>
                <img src="https://tile.openstreetmap.org/10/560/380.png" alt="Карта" />
                <!-- Убрано поле с поисками под картой -->
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
        min-height: 100vh;
    }

    .page-wrapper {
        padding: 20px;
        min-height: 100vh;
        box-sizing: border-box;
    }

    .container {
        display: grid;
        grid-template-columns: 300px 1fr;
        gap: 20px;
        margin: 0 auto;
        align-items: start;
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

    /* Правая колонка */
    .right {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    /* Оранжевый информационный блок - уменьшен */
    .orange-info-block {
        background: #ff8800;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: black;
        height: fit-content;
        min-height: 180px; /* Примерная высота левого блока */
    }

    .orange-info-block h3 {
        margin: 0 0 12px 0;
        font-size: 16px;
        color: black;
    }

    .info-content {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .info-content p {
        margin: 0;
        font-size: 13px;
        line-height: 1.3;
    }

    .info-content b {
        color: #333;
    }

    /* Дополнительная информация (перенесенная из левого столбца) */
    .additional-info-block {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .medic-status {
        background: white;
        border-radius: 15px;
        padding: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        height: fit-content;
    }

    .medic-status p {
        margin: 0;
        font-size: 13px;
        font-weight: 500;
        color: #28a745;
    }

    .availability-section {
        background: white;
        border-radius: 15px;
        padding: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        height: fit-content;
    }

    .availability-section p {
        margin: 0;
        font-size: 13px;
        font-weight: 500;
        color: #28a745;
    }

    /* Общая высота верхних блоков */
    .orange-info-block,
    .additional-info-block {
        flex-shrink: 0;
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
        margin-bottom: 0; /* Убрано, так как больше нет контента под картой */
    }

    @media (max-width: 900px) {
        .page-wrapper {
            padding: 15px;
        }
        
        .container {
            grid-template-columns: 1fr;
        }
        
        .profile {
            position: static;
        }
        
        .orange-info-block {
            min-height: auto;
        }
    }

    @media (max-width: 480px) {
        .page-wrapper {
            padding: 10px;
        }
    }
</style>