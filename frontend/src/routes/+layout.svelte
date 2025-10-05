<script>
  import '../app.css';
</script>

<div class="app">
  <header class="header">
    <nav class="nav">
      <a href="/" class="logo">Карта помощи</a>
      
      <div class="header-image">
        <img src="/header.png" alt="" />
      </div>
    </nav>
  </header>

  <main class="main">
    <slot />
  </main>
</div>