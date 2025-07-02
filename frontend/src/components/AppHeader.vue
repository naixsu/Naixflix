<template>
    <header class="header">
        <div class="logo">NAIXFLIX</div>
        <nav class="nav">
            <button
                class="add-movie-btn"
                @click="emit('add')"
            >
                Add Movie
            </button>
        </nav>
    </header>

</template>

<script setup>
    import { defineEmits } from 'vue';

    const emit = defineEmits(['close', 'submit', 'add']);
</script>


<style scoped>
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
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
