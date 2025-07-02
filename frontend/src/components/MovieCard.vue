<template>
    <div
        class="movie-card"
        :class="{ selected: isSelected }"
        @click="emit('handle-click')"
    >
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

    const emit = defineEmits(['delete', 'edit', 'click',]);

    defineProps({
        movie: {
            type: Object,
            required: true,
        },

        isSelected: {
            type: Boolean,
            default: false,
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

    .movie-card:first-child {
        margin-left: 10px;
    }

    .movie-card:last-child {
        margin-right: 10px;
    }

    .movie-card.selected {
        outline: 3px solid #e50914;
        box-shadow: 0 0 10px rgba(229, 9, 20, 0.8);
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
