<template>
    <header class="header">
        <div class="logo">NETFLIX</div>
        <nav class="nav">
            <a href="#">Home</a>
            <a href="#">TV Shows</a>
            <a href="#">Movies</a>
            <a href="#">Latest</a>
        </nav>
    </header>
</template>

<style scoped>
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 2rem;
        background-color: #000;
    }

    .logo {
        color: #e50914;
        font-size: 2rem;
        font-weight: bold;
    }

    .nav a {
        margin: 0 1rem;
        text-decoration: none;
        color: #fff;
    }
</style>
