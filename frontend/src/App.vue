<template>
    <div class="app">
        <AppHeader />

        <main class="main">
            <MovieRow
                title="Popular on Netflix"
                :movies="popular"
            />
            <MovieRow
                title="Trending Now"
                :movies="trending"
            />
        </main>
    </div>
</template>

<script setup>
    import AppHeader from './components/AppHeader.vue';
    import MovieRow from './components/MovieRow.vue';

    const popular = Array.from({ length: 20 }, (_, i) => `HD ${i + 1}`);
    const trending = Array.from({ length: 14 }, (_, i) => `HD ${i + 1}`);
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

    .main {
        flex: 1;
        padding: 2rem;
        overflow-y: auto;
    }
</style>
