<script lang="ts">
  import { goto } from "$app/navigation";

	// Определяем типы для полей ввода
	let login: string = "";
	let password: string = "";
	let errorMessage: string = ""; // реактивная переменная для ошибки

	// Функция отправки формы с указанием типа события
	export async function handleSubmit(event: Event): Promise<void> {
		event.preventDefault();

		// Проверка логина и пароля
		if (login === "admin" && password === "admin") {
			errorMessage = "";
            await goto('/profile_admin');
		} else if (login === "vol" && password === "vol"){
			errorMessage = "";
            await goto('/profile');
        }  
        else {
			errorMessage = "Введён неверный логин или пароль";
		}
	}
</script>

<!-- Обёртка страницы -->
<div class="page-wrapper">
	<div class="container">
		<h1 class="main-heading">Карта помощи</h1>

		<!-- Обёртка формы -->
		<div class="form-wrapper">
			<span class="form-heading">Вход</span>

			<!-- Форма входа (для админа или суперпользователя) -->
			<form class="login-form" on:submit={handleSubmit} method="post">
				<label class="input-label">
					<span class="input-title">Логин</span>
					<input
						required
						class="input-item"
						type="text"
						bind:value={login}
						placeholder="Введите ваш логин"
					/>
				</label>

				<label class="input-label">
					<span class="input-title">Пароль</span>
					<input
						required
						class="input-item"
						type="password"
						bind:value={password}
						placeholder="Введите ваш пароль"
					/>
				</label>

				<!-- Кнопка отправления формы -->
				<button class="submit-button" type="submit">
					<span class="button-text">Войти</span>
				</button>
			</form>
			<a class="guest-login" href="profile">Войти как гость</a>
		</div>

		<!-- Если введён неверный логин или пароль, отображается сообщение об ошибке -->
        {#if errorMessage === "profile_admin"}
            <div class="auth-error">{errorMessage}</div>
        {/if}

	</div>
</div>

<style>
	/* Обёртка страницы*/
	.page-wrapper {
		height: 100vh;

		background-color: #ffffff;

		display: flex;
		justify-content: center;
		align-items: center;
	}

	/* Контейнер??? */
	.container {
		height: 585px;

		display: flex;
		flex-direction: column;
		row-gap: 47px;
	}

	/* Выравнивание заголовков по центру блока */
	.main-heading,
	.guest-login {
		text-align: center;
	}

	/* Обёртка формы */
	.form-wrapper {
		width: 456px;
		height: 371px;

		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	/* Стили текста */
	.main-heading {
		font-size: 50px;
		font-weight: 400;
		line-height: 72px;
		color: #ff8800;
	}
	.form-heading {
		position: relative;
		left: 13px;

		font-size: 18px;
		font-weight: 600;
		line-height: 24px;
	}
	.guest-login {
		font-size: 14px;
		font-weight: 400;
		line-height: 24px;
		color: #2b273780;
		text-decoration: none;
	}

	/* Форма */
	.login-form {
		width: 400px;
		height: 228px;

		padding: 28px;

		border: 2px solid #2b27371a;
		border-radius: 25px;

		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	/* Поля ввода */
	.input-label {
		width: 350px;
		height: 70px;
        padding: auto;
        
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}
	.input-title {
		font-size: 12px;
		font-weight: 400;
		line-height: 16px;
		color: #2b2737;
	}
	.input-item {
		padding: 9px 12px;

		border: none;
		border-radius: 12px;

		background-color: #fafafa;
		font-size: 16px;
		font-weight: 400px;
		color: #000000;

		line-height: 24px;
	}
	.input-item::placeholder {
		color: #11181c80;
	}

	/* Кнопка отправления формы */
	.submit-button {
		padding: 12px;
		margin-top: 16px; /* Отступ от поля ввода пароля */

		font-size: 16px;
		font-weight: 400;
		line-height: 24px;

		border: none;
		border-radius: 12px;

		color: #ffffff;
		background-color: #ff8800;
		
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.button-text {
		text-align: center;
		width: 100%;
	}

	/* Сообщение с ошибкой */
	.auth-error {
		padding: 12px 58.5px;
		width: 283px;

		font-size: 16px;
		font-weight: 400;
		line-height: 24px;

		color: #F31260;
		background-color: #FFD5E0;
		border-radius: 12px;

		align-self: center;
	}
</style>