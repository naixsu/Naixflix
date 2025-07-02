<template>
    <div class="movie-card">
        <div class="poster">
            {{ label }}
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
    label: {
        type: String,
        required: true,
    },
});
</script>

<style scoped>
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
