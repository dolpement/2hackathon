<script>
    /*let applications = [
    {
      name: "Человек Человеков",
      date: "2024-01-15",
      details: "рост, глаза, волосы, во что одет и тд",
      city: "Москва",
      telegram: "@exemp"
    }
    ];*/

    import {onMount} from "svelte";

    let applications = [];
    let loading = true;
    let error = null;

    onMount(async () => {
        try {
            const res = await fetch('http://127.0.0.1:8000/search-operations');
            applications = await res.json();
            console.log(JSON.stringify(applications));
        } catch (e) {
            error = e.message;
        } finally {
            loading = false;
        }
    })
</script>

<div class="page-container">
    <!-- Блок с заявками -->
    <div class="applications-section">
        <h2>Заявка на поиск</h2>
        <div id="applicationsList">
            {#each applications as application, i}
                <div class="application-card">
                    <strong>{application.request_info}</strong>
                    {#if application.meeting_time}
                        <p><b>📅 Дата:</b> {application.meeting_time}</p>
                    {/if}
                    {#if application.report}
                        <p><b>📋 Детали:</b> {application.report}</p>
                    {/if}
                    {#if application.meeting_place}
                        <p><b>🏙️ Город:</b> {application.meeting_place}</p>
                    {/if}
                    {#if application.participants}
                        <p><b>Участники поиска:</b></p>
                        <ul class="participants-list">
                        {#each application.participants as participant, i}
                            <li>
                                <p>{participant.full_name}</p>
                            </li>
                        {/each}
                        </ul>
                    {/if}

                    {#if application.telegram}
                        <p class="telegram-link">
                            📢 Телеграм:
                            <a href="https://t.me/{application.telegram.replace('@', '')}" target="_blank">
                                {application.telegram}
                            </a>
                        </p>
                    {/if}
                </div>
            {/each}
        </div>
    </div>

    <!-- Блок с картой для 2GIS API -->
    <div class="map-section">
        <h2>Карта поиска</h2>
        <div class="map-placeholder">
            <div class="map-frame">
                <!-- Место для будущей интеграции с 2GIS -->
                <div class="map-overlay">
                    <span>2GIS Map API</span>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .page-container {
        padding: 20px;
        font-family: Arial, sans-serif;
        display: flex;
        flex-direction: column;
        gap: 30px;
        max-width: 1000px;
        margin: 0 auto;
    }

    /* Стили для карты */
    .map-section {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .map-section h2 {
        color: #333;
        margin-bottom: 15px;
        font-size: 20px;
    }

    .map-placeholder {
        text-align: center;
        color: #666;
    }

    .map-frame {
        width: 100%;
        height: 400px;
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-radius: 10px;
        margin-top: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px dashed #90caf9;
    }

    .map-overlay {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px 40px;
        border-radius: 8px;
        font-weight: bold;
        color: #1976d2;
    }

    /* Стили для заявок */
    .applications-section {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .applications-section h2 {
        color: #333;
        margin-bottom: 20px;
        font-size: 20px;
    }

    #applicationsList {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .application-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        border-left: 4px solid #ff8800;
        cursor: default;
    }

    .application-card strong {
        font-size: 18px;
        color: #333;
        display: block;
        margin-bottom: 10px;
    }

    .application-card p {
        margin: 5px 0;
        color: #666;
        font-size: 14px;
    }

    .telegram-link {
        margin-top: 10px !important;
        padding-top: 10px;
        border-top: 1px solid #ddd;
    }

    .telegram-link a {
        color: #0088cc;
        text-decoration: none;
        font-weight: 500;
    }

    .telegram-link a:hover {
        text-decoration: underline;
    }

    @media (max-width: 768px) {
        .page-container {
            padding: 15px;
            gap: 20px;
        }

        .map-frame {
            height: 300px;
        }
    }

    .participants-list {
        margin-left: 20px;
    }
</style>