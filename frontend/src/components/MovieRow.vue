<template>
    <section class="category">
        <h2>{{ title }}</h2>
        <div class="scroll-wrapper">
            <button
                v-if="showScroll"
                class="scroll-btn left"
                @click="scrollLeft"
            >
                &#10094;
            </button>

            <div
                class="movie-row"
                ref="row"
            >
                <MovieCard
                    v-for="(movie, i) in movies"
                    :key="i"
                    :movie="movie"
                    :is-selected="movie.pk === selectedMovie?.pk"
                    @delete="emit('delete', movie)"
                    @edit="emit('edit', movie)"
                    @handle-click="emit('handle-click', movie)"
                />
            </div>

            <button
                v-if="showScroll"
                class="scroll-btn right"
                @click="scrollRight"
            >
                &#10095;
            </button>
        </div>
    </section>
</template>

<script setup>
    import { ref, defineProps, onMounted, onUpdated, defineEmits } from 'vue';
    import MovieCard from './MovieCard.vue';

    defineProps({
        title: String,
        movies: Array,
        selectedMovie: {
            type: Object,
            required: false,
        },
    });

    const emit = defineEmits(['delete', 'edit']);

    const row = ref(null);
    const showScroll = ref(false);
    const CARD_WIDTH = 160;

    const scrollLeft = () => {
        row.value.scrollBy({ left: -CARD_WIDTH * 3, behavior: 'smooth' });
    };

    const scrollRight = () => {
        row.value.scrollBy({ left: CARD_WIDTH * 3, behavior: 'smooth' });
    };

    // Check if content overflows
    const checkOverflow = () => {
        const el = row.value;
        if (el) {
            showScroll.value = el.scrollWidth > el.clientWidth;
        }
    };

    onMounted(checkOverflow);
    onUpdated(checkOverflow);
</script>

<style scoped>
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
</style>
