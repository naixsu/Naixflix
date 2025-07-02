<template>
    <div class="app">
        <AppHeader
            @add-new-movie="handleAddNewMovie"
        />

        <main class="main">
            <MovieRow
                title="Movies"
                :movies="movies"
            />
        </main>
    </div>
</template>

<script setup>
    // Imports
    import axios from 'axios';
    import { ref, onMounted } from 'vue';
    import AppHeader from './components/AppHeader.vue';
    import MovieRow from './components/MovieRow.vue';

    // Data
    const isFetching = ref(false);
    const movies = ref([]);

    // onMounted
    onMounted(async () => {
        fetchMovies();
    })

    // Async functions
    async function fetchMovies() {
        isFetching.value = true;

        try {
            const response = await axios.get("http://localhost:8000/api/movies");
            movies.value = response.data;
        } catch (error) {
            console.error('Error fetching movies:', error);
        } finally {
            isFetching.value = false;
        }
    }

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
        } finally {
            await fetchMovies();
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
