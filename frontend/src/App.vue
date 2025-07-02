<template>
    <div class="app">
        <AppHeader @add="handleAdd"/>

        <MovieDetails
            :movie="selectedMovie"
        />

        <MovieModal
            v-if="showModal"
            :movie="editMovie"
            @close="showModal = false"
            @submit="handleSubmit"
        />

        <main class="main">
            <MovieRow
                title="Movies"
                :movies="movies"
                :selected-movie="selectedMovie"
                @delete="handleDelete"
                @edit="handleEdit"
                @handle-click="handleMovieClick"
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
    import MovieModal from './components/MovieModal.vue';
    import MovieDetails from './components/MovieDetails.vue';

    // Data
    const isFetching = ref(false);
    const movies = ref([]);
    const showModal = ref(false);
    const editMovie = ref(null);
    const selectedMovie = ref(null);

    // onMounted
    onMounted(async () => {
        fetchMovies();
    })

    // Functions
    function handleEdit(movie) {
        editMovie.value = movie;
        showModal.value = true;
    }

    function handleAdd() {
        editMovie.value = null;
        showModal.value = true;
    }

    function handleMovieClick(movie) {
        selectedMovie.value = movie;
    }

    function handleUpdateSelectedMovie() {
        if (!selectedMovie.value) {
            return;
        }

        const updated = movies.value.find(movie =>
            movie.pk === selectedMovie.value.pk
        )

        if (updated) {
            selectedMovie.value = updated;
        }
    }

    // Async functions
    async function fetchMovies() {
        isFetching.value = true;

        try {
            const response = await axios.get("http://localhost:8000/api/movies");
            movies.value = response.data;
            handleUpdateSelectedMovie()
        } catch (error) {
            console.error('Error fetching movies:', error);
        } finally {
            isFetching.value = false;
        }
    }

    async function handleSubmit(data) {
        try {
            const formData = new FormData();
            formData.append('title', data.title);
            formData.append('description', data.description);

            // Only include video_file if a new one is provided
            if (data.video_file instanceof File) {
                formData.append('video_file', data.video_file);
            }

            const config = {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            };

            if (data.pk) {
                // PATCH to update existing movie
                await axios.patch(`http://localhost:8000/api/movies/${data.pk}/`, formData, config);
            } else {
                // POST to create new movie
                await axios.post('http://localhost:8000/api/movies/', formData, config);
            }
        } catch (error) {
            console.error('Failed to save movie:', error.response?.data || error.message);
        } finally {
            await fetchMovies();
        }
    }

    async function handleDelete(movie) {
        // Note that a HARD DELETE is not implemented here
        try {
            await axios.patch(`http://localhost:8000/api/movies/${movie.pk}/`, {
                is_removed: true,
            });
        } catch (error) {
            console.error(`Failed to delete movie ${movie.pk}`, error);
        } finally {
            const index = movies.value.findIndex(movie => movie.pk === movie.pk)
            await fetchMovies();

            // Switch `selectedMovie` to an available one
            if (selectedMovie.value?.pk === movie.pk) {
                if (index > 0) {
                    selectedMovie.value = movies.value[index - 1]
                } else if (movies.value.length > 0) {
                    selectedMovie.value = movies.value[0]
                } else {
                    selectedMovie.value = null
                }
            }
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
