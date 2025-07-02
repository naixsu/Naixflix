<template>
    <div class="modal-backdrop">
        <div class="modal">
            <h2>
                Add New Movie
            </h2>
            <form @submit.prevent="handleSubmit">
                <label>
                    Title:
                    <input
                        v-model="form.title"
                        required 
                    />
                </label>

                <label>
                    Description:
                    <textarea
                        v-model="form.description"
                        required
                    />
                </label>

                <label>
                    Video File:
                    <input
                        type="file"
                        @change="handleFile"
                        required
                    />
                </label>

                <div class="modal-actions">
                    <button
                        type="submit"
                    >
                        Submit
                    </button>
                    <button
                        type="button"
                        @click="handleClose"
                    >
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { reactive, defineEmits } from 'vue';

    const emit = defineEmits(['close', 'submit']);

    const form = reactive({
        title: '',
        description: '',
        video_file: null,
    });

    const handleFile = (e) => {
        form.video_file = e.target.files[0];
    };

    function handleClose() {
        emit('close');
    }

    function handleSubmit() {
        emit('submit', { ...form });
        form.title = '';
        form.description = '';
        form.video_file = '';
        handleClose();
    }

</script>

<style scoped>
    .modal-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.6);
        display: grid;
        place-items: center;
        z-index: 999;
    }

    .modal {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        width: 400px;
        max-width: 90%;
    }

    .modal h2 {
        margin-top: 0;
        color: #111;
    }

    .modal label {
        display: block;
        margin-bottom: 1rem;
        font-weight: bold;
        color: #333;
    }

    .modal input,
    .modal textarea {
        width: 100%;
        padding: 0.5rem;
        margin-top: 0.25rem;
        font-size: 1rem;
        border-radius: 4px;
        border: 1px solid #ccc;
    }

    .modal-actions {
        display: flex;
        justify-content: flex-end;
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .modal-actions button {
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
        cursor: pointer;
        border-radius: 4px;
    }

    .modal-actions button[type='submit'] {
        background-color: #e50914;
        color: white;
    }

    .modal-actions button[type='submit']:hover {
        background-color: #ff0a16;
    }

    .modal-actions button[type='button'] {
        background-color: #ddd;
    }
</style>
