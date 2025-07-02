<template>
    <div class="app">
        <header class="header">
            <div class="logo">NETFLIX</div>
            <nav class="nav">
                <a href="#">Home</a>
                <a href="#">TV Shows</a>
                <a href="#">Movies</a>
                <a href="#">Latest</a>
            </nav>
        </header>

        <main class="main">
            <section class="category">
                <h2>Popular on Netflix</h2>
                <div class="scroll-wrapper">
                    <button class="scroll-btn left" @click="scrollLeft('popular')">&#10094;</button>
                    <div class="movie-row" ref="popular">
                        <div v-for="n in 20" :key="'popular-' + n" class="movie-card">
                            <div class="poster">HD</div>
                        </div>
                    </div>
                    <button class="scroll-btn right" @click="scrollRight('popular')">&#10095;</button>
                </div>
            </section>

            <section class="category">
                <h2>Trending Now</h2>
                <div class="scroll-wrapper">
                    <button class="scroll-btn left" @click="scrollLeft('trending')">&#10094;</button>
                    <div class="movie-row" ref="trending">
                        <div v-for="n in 14" :key="'trending-' + n" class="movie-card">
                            <div class="poster">HD</div>
                        </div>
                    </div>
                    <button class="scroll-btn right" @click="scrollRight('trending')">&#10095;</button>
                </div>
            </section>
        </main>
    </div>
</template>


<script setup>
import { ref } from 'vue';

const popular = ref(null);
const trending = ref(null);

const scrollLeft = (section) => {
    const container = section === 'popular' ? popular.value : trending.value;
    container.scrollBy({ left: -160 * 3, behavior: 'smooth' }); // 3 cards
};

const scrollRight = (section) => {
    const container = section === 'popular' ? popular.value : trending.value;
    container.scrollBy({ left: 160 * 3, behavior: 'smooth' }); // 3 cards
};
</script>

<style scoped>
html,
body,
#app,
.app {
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
}

.app {
    background-color: #141414;
    color: #fff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

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

.main {
    flex: 1;
    padding: 2rem;
    overflow-y: auto;
}

.category {
    margin-bottom: 2rem;
}

.category h2 {
    margin-bottom: 1rem;
}

.scroll-wrapper {
    position: relative;
}

.scroll-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(20, 20, 20, 0.7);
    color: white;
    border: none;
    font-size: 2rem;
    padding: 0 0.5rem;
    cursor: pointer;
    z-index: 10;
}

.scroll-btn.left {
    left: -1rem;
}

.scroll-btn.right {
    right: -1rem;
}

.movie-row {
    display: flex;
    gap: 1rem;
    overflow-x: auto;
    scroll-behavior: smooth;
    padding: 1rem 0;
}

.movie-row::-webkit-scrollbar {
    display: none;
}

.movie-card {
    background-color: #333;
    width: 150px;
    height: 220px;
    border-radius: 8px;
    overflow: hidden;
    flex-shrink: 0;
}

.poster {
    background-color: #555;
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
    color: white;
    font-weight: bold;
    font-size: 1.2rem;
}
</style>
