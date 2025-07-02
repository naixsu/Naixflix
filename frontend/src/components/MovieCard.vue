<template>
    <div class="movie-card">
        <div class="actions">
            <GenericButton
                icon="pencil"
                size="small"
                class="icon-btn left"
                @click="emit('edit')"
            />
            <GenericButton
                icon="trash-can"
                size="small"
                class="icon-btn right"
                @click="emit('delete')"
            />
        </div>
        <div class="poster">
            {{ movie.title }}
        </div>
    </div>
</template>

<script setup>
    import { defineProps, defineEmits } from 'vue';
    import GenericButton from './GenericButton.vue';

    const emit = defineEmits(['delete', 'edit']);

    defineProps({
        movie: {
            type: Object,
            required: true,
        },
    });
</script>

<style scoped>
    .movie-card {
        position: relative;
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
        text-align: center;
        padding: 0.5rem;
    }

    .actions {
        position: relative;
        width: 100%;
        height: 0;
    }

    .icon-btn {
        position: absolute;
        top: 0.3rem;
        background: rgba(0, 0, 0, 0.6);
        padding: 0.3rem;
        border-radius: 4px;
        color: white;
    }

    .icon-btn:hover {
        background: rgba(255, 255, 255, 0.2);
    }

    .icon-btn.left {
        left: 0.3rem;
    }

    .icon-btn.right {
        right: 0.3rem;
    }
</style>
