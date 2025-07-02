<template>
    <header class="header">
        <div class="logo">NAIXFLIX</div>
        <nav class="nav">
            <GenericButton
                label="Add Movie"
                class="add-movie-btn"
                @click="emit('add')"
            />
        </nav>
    </header>

</template>

<script setup>
    import { defineEmits } from 'vue';
    import GenericButton from './GenericButton.vue';

    const emit = defineEmits(['add']);
</script>


<style scoped>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #000;
    }

    .logo {
        color: #e50914;
        font-size: 2rem;
        font-weight: bold;
    }

    .nav {
        display: flex;
        align-items: center;
    }

    .nav a {
        margin: 0 1rem;
        text-decoration: none;
        color: #fff;
    }

    .add-movie-btn {
        margin-left: 1rem;
        padding: 0.5rem 1rem;
        background-color: #e50914;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
        transition: background 0.3s;
    }

    .add-movie-btn:hover {
        background-color: #ff0a16;
    }
</style>
