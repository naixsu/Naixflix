<template>
    <section class="category">
        <h2>{{ title }}</h2>
        <div class="scroll-wrapper">
            <button
                class="scroll-btn left"
                @click="scrollLeft">
                &#10094;
            </button>
            <div
                class="movie-row"
                ref="row"
            >
                <MovieCard
                    v-for="(label, i) in movies"
                    :key="i"
                    :label="label"
                />
            </div>
            <button
                class="scroll-btn right"
                @click="scrollRight"
                >
                &#10095;
            </button>
        </div>
    </section>
</template>

<script setup>
    import { ref, defineProps } from 'vue';
    import MovieCard from './MovieCard.vue';

    defineProps({
        title: String,
        movies: Array,
    });

    const row = ref(null);
    const CARD_WIDTH = 160;

    const scrollLeft = () => {
        row.value.scrollBy({ left: -CARD_WIDTH * 3, behavior: 'smooth' });
    };

    const scrollRight = () => {
        row.value.scrollBy({ left: CARD_WIDTH * 3, behavior: 'smooth' });
    };
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
