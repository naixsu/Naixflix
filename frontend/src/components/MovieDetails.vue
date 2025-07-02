<template>
    <div
        v-if="props.movie"
        class="movie-details"
    >
        <h2>{{ movie.title }}</h2>
        <p class="description">
            {{ movie.description }}
        </p>
        <video
            v-if="movie.video_file"
            :key="movie.video_file"
            class="video-player"
            controls
            autoplay
            playsinline
            loop
            width="100%"
        >
            <source :src="movie.video_file" type="video/mp4" />
            Your browser does not support the video tag.
        </video>
    </div>
</template>

<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        movie: {
            type: Object,
            required: true
        }
    });
</script>

<style scoped>
    .movie-details {
        background-color: #222;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        max-width: 800px;
        margin: 2rem auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    }

    .movie-details h2 {
        margin-top: 0;
        font-size: 2rem;
    }

    .description {
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .video-player {
        /* width: 100%; */
        max-height: 800px;
        min-height: 600px;
        min-width: 800px;
        max-width: 800px;
        border-radius: 8px;
        background: black;
    }
</style>
