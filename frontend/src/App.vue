<template>
    <div class="app">
        <AppHeader
            @add-new-movie="handleAddNewMovie"
        />

        <main class="main">
            movies
            {{ movies }}
            <MovieRow
                title="Popular on Netflix"
                :movies="popular"
            />
            <!-- <MovieRow
                title="Trending Now"
                :movies="trending"
            /> -->
        </main>
    </div>
</template>

<script setup>
    import AppHeader from './components/AppHeader.vue';
    import MovieRow from './components/MovieRow.vue';
    import axios from 'axios';

    const popular = Array.from({ length: 20 }, (_, i) => `HD ${i + 1}`);

    async function handleAddNewMovie(data) {
        try {
            const formData = new FormData();
            formData.append('title', data.title);
            formData.append('description', data.description);
            formData.append('video_file', data.video_file); // file object

            await axios.post('http://localhost:8000/api/movies/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
        } catch (error) {
            console.error('Failed to add new movie:', error.response?.data || error.message);
        }
    }
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
